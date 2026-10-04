---
title: "公開・編集手順"
lang: ja
---

# EMV 3DS 2.3.1.1 — Markdown / PNG パッケージ

[目次](index.md)

## 翻訳範囲

**全文翻訳は未完了です。** 原本は410ページあり、日本語参考訳は第1章（17–34ページ）、第2章（35–48ページ）、第3章（49–93ページ）、第4章（94–144ページ）、第5章（145–171ページ）、第6章（172–184ページ）、前付け1–3ページ、附属書Aの185–216ページの合計203ページです。附属書Aの217–376ページ、附属書B〜D、索引と前付け4–16ページは英語の抽出結果のみを収録しています。

原本の英語本文410ページをページ別・章別のMarkdownとして収録しています。図69点と表紙ロゴ1点はPNGです。図内の英語は翻訳していません。表208個はMarkdownで再構成しています。ページをまたぐ表はページ単位で分割され、結合セルは空欄として残る場合があります。抽出全文の目視校正は未実施です。

## GitHub Pagesへの掲載

1. ZIPを展開し、`emv-3ds-ja/` の**中身**をGitHubリポジトリのルートに配置します。`.github/` も含めてください。
2. リポジトリの **Settings → Pages → Build and deployment → Source** を **GitHub Actions** に設定します。
3. `main` ブランチへpushします。別のブランチを使う場合は `.github/workflows/pages.yml` の `branches` を変更します。
4. Actionsの `Build and deploy documentation` が成功すると、PagesのURLで目次を開けます。

収録のワークフローはMarkdownを静的HTMLに変換して公開します。編集対象は `.md` とPNGで、HTMLを手作業で修正する必要はありません。相対リンクを使うため、`https://ユーザー名.github.io/リポジトリ名/` のようなサブパスにも対応します。GitHubへのアップロード・実際の公開は、このパッケージの作成には含まれていません。

公式手順：[GitHub Pagesのカスタムワークフロー](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## ローカル確認

Python 3.11以上とPandoc 3以上を用意し、リポジトリのルートで実行します。

```sh
python3 scripts/build_site.py
python3 scripts/check_links.py
python3 -m http.server 8000 --directory _site
```

ブラウザで `http://localhost:8000/` を開きます。`_site` は生成物なのでGitに登録する必要はありません。

## フォルダ構成

| パス | 内容 |
| --- | --- |
| `index.md` | 章別目次と翻訳状況 |
| `ja/chapters/` | 翻訳済みの章（前付けは一部） |
| `ja/pages/` | 原本ページ別の日本語参考訳 |
| `en/chapters/` | 英語の章別Markdown |
| `en/pages/` | 英語のページ別Markdown（410ページ） |
| `assets/images/` | 原図PNG、表紙ロゴ（70ファイル） |
| `assets/style.css` | 表・図を含むWeb表示のスタイル |
| `data/` | 原本目次、画像座標、抽出結果、翻訳状況 |
| `scripts/` | サイト生成、内部リンク検査、PDF再抽出 |
| `.github/workflows/pages.yml` | GitHub Actions公開設定 |

## 編集と翻訳の継続

日本語の章ファイルとページファイルは独立したMarkdownです。修正時は両方を更新してください。追加の章を翻訳する場合は、対応する英語の章・ページファイルを参照し、`ja/` に追加します。`index.md`、`pages.md`、`data/translation-status.json` も翻訳範囲に合わせて更新してください。未翻訳の英語を日本語訳として表示しないようにしてください。

図のファイル名は `figure-2-1.png` のように原本の図番号に対応します。附属書の図は `figure-A-1.png` です。3RIの図と附属書のUI図は、PDF上の文字・線・画像部品をまとめて切り出しています。

原本PDFはZIPに含めていません。抽出をやり直す場合はPyMuPDFをインストールし、次を実行します。出力先には新しい空フォルダを指定してください。

```sh
python3 -m pip install 'PyMuPDF>=1.26,<1.27'
python3 scripts/extract_pdf.py /path/to/EMV_3DS_CoreSpec_v2.3.1.1_20230530.pdf /path/to/new-output
```

再抽出スクリプトはこの版のページ構成に合わせたものです。日本語訳やサイト設定を生成するものではありません。

## 著作権と参考訳

原本：EMV® 3-D Secure Protocol and Core Functions Specification, Version 2.3.1.1, May 2023。

© 2016–2023 EMVCo, LLC. All rights reserved. 原本の通知は、複製・配布その他の利用を利用者とEMVCo間の適用契約に従う場合に限っています。一般公開する前に、適用契約の公開・翻訳に関する条件を確認してください。原文と法的通知は `en/pages/002.md`、参考訳は `ja/pages/002.md` に収録しています。

日本語訳は非公式の参考訳です。仕様解釈には英語原本を照合してください。
