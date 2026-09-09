from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import sys
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from generate_watch_face_lab import APP, POLICY_DATE, original_copy
ROOT = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        values=dict(attrs)
        for key in ('href','src'):
            if key in values: self.links.append(values[key])
count=0
policy = json.loads((ROOT/'scripts/watch_face_lab_policy.json').read_text(encoding='utf-8'))
assert set(policy) == {'en', 'ru', 'uk', 'de', 'es', 'fr', 'it', 'pt', 'pl'}
for lang, sections in policy.items():
    assert len(sections) == 8 and all(len(section) == 2 and all(section) for section in sections), lang
    offline = (APP/'app/src/main/assets/legal'/f'privacy_{lang}.txt').read_text(encoding='utf-8')
    assert offline.startswith(original_copy(lang)['privacy'] + '\nWatch Face Lab · Alternix\n' + POLICY_DATE), lang
    for title, paragraph in sections:
        assert title + '\n' + paragraph in offline, (lang, title, 'offline mismatch')
    assert 'alternix.apps@gmail.com' in offline
    assert all(provider in offline for provider in ('Google', 'AdMob', 'App Set ID', 'GitHub', '13–17', '18+'))
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
        if page == 'privacy':
            assert POLICY_DATE in html
            for title, paragraph in sections:
                assert paragraph in html, (lang, title, 'web mismatch')
            assert '<h1>' + original_copy(lang)['privacy'] + '</h1>' in html
        if '--live' in sys.argv:
            url = 'https://alternixapps.github.io/' + (prefix/'watch-face-lab'/page).as_posix() + '/'
            with urlopen(url, timeout=20) as response:
                assert response.status == 200, url
                live = response.read().decode('utf-8')
            assert live.strip() == html.strip(), (url, 'published content differs')
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
