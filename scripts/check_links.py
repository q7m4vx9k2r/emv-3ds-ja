#!/usr/bin/env python3
"""Check all local href/src targets and fragment identifiers in the built site."""
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / '_site'
class Scan(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
        if 'id' in a:self.ids.add(a['id'])
        if tag=='a' and 'name' in a:self.ids.add(a['name'])

def main():
    files=sorted(ROOT.rglob('*.html'))
    if not files:raise SystemExit('Run build_site.py first.')
    scans={}
    for file in files:
        scan=Scan();scan.feed(file.read_text());scans[file.resolve()]=scan
    errors=[];count=0
    for file,scan in scans.items():
        for link in scan.links:
            u=urlsplit(link)
            if u.scheme or u.netloc:continue
            count+=1
            target=(file.parent/unquote(u.path)).resolve() if u.path else file
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{file.relative_to(ROOT)}: missing {link}')
            elif u.fragment and target in scans and unquote(u.fragment) not in scans[target].ids:
                errors.append(f'{file.relative_to(ROOT)}: missing fragment {link}')
    for e in errors:print(e)
    if errors:raise SystemExit(f'{len(errors)} broken local links')
    print(f'Checked {len(files)} pages and {count} local links: no broken targets.')

if __name__ == '__main__':main()
