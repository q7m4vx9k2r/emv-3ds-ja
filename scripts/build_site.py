#!/usr/bin/env python3
"""Build relative-path-safe static HTML from the Markdown source using Pandoc."""
import concurrent.futures
import html
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'

def split_front(text):
    if text.startswith('---\n'):
        front, sep, body = text[4:].partition('\n---\n')
        if sep:
            def field(key, default):
                match = re.search(r'^'+key+r':\s*(.+)$', front, re.M)
                return match.group(1).strip().strip('"\'') if match else default
            return body, field('title', 'EMV 3-D Secure'), field('lang', 'ja')
    return text, 'EMV 3-D Secure', 'ja'

def render(path):
    relative = path.relative_to(ROOT)
    body, title, lang = split_front(path.read_text(encoding='utf-8'))
    result = subprocess.run(['pandoc', '--from=gfm+raw_html', '--to=html5', '--wrap=none'],
                            input=body, text=True, capture_output=True, check=True)
    article = re.sub(r'(href="[^"#?]*?)\.md(?=[#?"])', r'\1.html', result.stdout)
    prefix = '../' * (len(relative.parts)-1)
    page = f'''<!doctype html>
<html lang="{html.escape(lang)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><header class="site-header"><a href="{prefix}index.html">EMV 3DS 2.3.1.1</a><span>日本語参考訳・作業途中</span></header>
<main><article>{article}</article></main>
<footer>非公式の日本語参考訳。全文翻訳は未完了です。<br>© 2016–2023 EMVCo, LLC. All rights reserved. 複製・配布その他の利用は適用契約に従う場合に限られます。</footer>
<script>document.querySelectorAll('table').forEach(t=>{{const w=document.createElement('div');w.className='table-scroll';t.parentNode.insertBefore(w,t);w.appendChild(t);}});</script>
</body></html>'''
    target = OUT / relative.with_suffix('.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page, encoding='utf-8')
    return relative

def main():
    if not shutil.which('pandoc'):
        raise SystemExit('Pandoc is required. Install Pandoc 3 or later.')
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/'assets', OUT/'assets')
    shutil.copytree(ROOT/'data', OUT/'data')
    (OUT/'.nojekyll').touch()
    sources = [ROOT/x for x in ['index.md','pages.md','figures.md','README.md']]
    sources += sorted((ROOT/'en').rglob('*.md'))
    sources += sorted((ROOT/'ja').rglob('*.md'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        completed = list(pool.map(render, sources))
    print(f'Built {len(completed)} HTML pages in {OUT}')

if __name__ == '__main__':
    main()
