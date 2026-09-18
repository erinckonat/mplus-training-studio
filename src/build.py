"""Şablondan index.html üretir: fontları ve Phosphor ikonlarını satır içine gömer.
Kullanım: python3 src/build.py"""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "src/template.html").read_text(encoding="utf-8")
fonts = (root / "assets/fonts/faces.css").read_text(encoding="utf-8")

def icon(m):
    svg = (root / f"assets/icons/{m.group(1)}.svg").read_text(encoding="utf-8").strip()
    return svg.replace("<svg ", '<svg class="ico" aria-hidden="true" focusable="false" ', 1)

out = tpl.replace("{{fonts}}", fonts)
out = re.sub(r"\{\{icon:([a-z0-9-]+)\}\}", icon, out)
left = re.findall(r"\{\{[^}]+\}\}", out)
assert not left, f"çözülmemiş yer tutucu: {left}"
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html yazıldı: {len(out)//1024} KB, {out.count('class=\"ico\"')} ikon")
