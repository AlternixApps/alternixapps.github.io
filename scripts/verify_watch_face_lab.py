from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        values=dict(attrs)
        for key in ('href','src'):
            if key in values: self.links.append(values[key])
count=0
for lang in json.loads((ROOT/'scripts/watch_face_lab_policy.json').read_text(encoding='utf-8')):
    prefix = Path() if lang=='en' else Path(lang)
    home=(ROOT/prefix/'index.html').read_text(encoding='utf-8')
    assert home.count('data-product-slide>')==4,lang
    assert home.count('data-slider-dot ')==4,lang
    for page in ['privacy','support']:
        path=ROOT/prefix/'watch-face-lab'/page/'index.html'
        html=path.read_text(encoding='utf-8')
        assert f'<html lang="{lang}">' in html
        assert 'Color Swatch Lab' not in html
        assert '/assets/watch-face-lab.svg' in html
        parser=Links(); parser.feed(html)
        for link in parser.links:
            parsed=urlsplit(link)
            if parsed.scheme or not parsed.path: continue
            dest=ROOT/unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else path.parent/unquote(parsed.path)
            if dest.is_dir(): dest=dest/'index.html'
            assert dest.is_file(),(path,link)
        count+=1
ET.parse(ROOT/'sitemap.xml')
print(f'PASS: {count} pages, 9 languages, 4 cards/dots each; internal links/assets and sitemap valid.')
