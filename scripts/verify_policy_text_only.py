"""Check that the current privacy edit changes text, not the existing site's layout."""
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append(('start', tag, attrs))

    def handle_endtag(self, tag):
        self.elements.append(('end', tag))


languages = json.loads((ROOT / 'scripts/watch_face_lab_policy.json').read_text(encoding='utf-8'))
for lang in languages:
    path = ('' if lang == 'en' else lang + '/') + 'watch-face-lab/privacy/index.html'
    before = subprocess.check_output(['git', 'show', 'HEAD:' + path], cwd=ROOT).decode('utf-8')
    after = (ROOT / path).read_text(encoding='utf-8')
    a, b = Structure(), Structure()
    a.feed(before)
    b.feed(after)
    assert a.elements == b.elements, (lang, 'HTML structure or attributes changed')

changed = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT).decode().splitlines()
allowed = {
    'scripts/generate_watch_face_lab.py', 'scripts/watch_face_lab_policy.json',
    'scripts/verify_watch_face_lab.py', 'scripts/verify_policy_text_only.py', 'sitemap.xml',
}
for path in changed:
    assert path in allowed or path.endswith('watch-face-lab/privacy/index.html'), path
print('PASS: all 9 privacy pages retain the exact HTML element/attribute structure; '
      'styles, scripts, navigation, home pages, support pages and other products unchanged.')
