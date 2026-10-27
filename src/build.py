"""Embed template.docx into app.html.
Writes ../artifact.html (page body for publishing) and ../index.html (standalone page for GitHub Pages)."""
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
app = open(os.path.join(here, "app.html"), encoding="utf8").read()
b64 = base64.b64encode(open(os.path.join(here, "template.docx"), "rb").read()).decode()
page = app.replace("__TEMPLATE_B64__", b64)
open(os.path.join(here, "..", "artifact.html"), "w", encoding="utf8").write(page)
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n')
open(os.path.join(here, "..", "index.html"), "w", encoding="utf8").write(head + page + "\n</body></html>\n")
print("built", len(page), "bytes")
