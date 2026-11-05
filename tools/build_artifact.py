#!/usr/bin/env python3
"""把 index.html 轉成可發布為 Claude Artifact 的版本（dist/artifact.html）。

Artifact 發布時會自動包上 <!doctype html><html><head><body>，
所以這裡只移除這些外殼標籤，內容（<title>、<style>、<script>）保持不變。
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text(encoding='utf-8')
out = src
for pat in [r'<!doctype html>\s*', r'<html[^>]*>\s*', r'</html>\s*', r'<head>\s*', r'</head>\s*',
            r'<body[^>]*>\s*', r'</body>\s*', r'<meta charset="utf-8">\s*', r'<meta name="viewport"[^>]*>\s*']:
    out = re.sub(pat, '', out, flags=re.I)
dist = root / 'dist'
dist.mkdir(exist_ok=True)
(dist / 'artifact.html').write_text(out, encoding='utf-8')
print('wrote', dist / 'artifact.html', len(out), 'bytes')
