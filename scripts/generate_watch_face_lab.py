"""Reuse the current Alternix legal layout/navigation, without editing other products."""
from pathlib import Path
import copy
import json
import re
import shutil
from html import escape
import generate_color_swatch_lab_pages as template
import add_color_swatch_lab_home_card as home

ROOT = Path(__file__).resolve().parents[1]
APP = Path(r'D:\18. Watch Face Lab')
POLICY = json.loads((ROOT / 'scripts/watch_face_lab_policy.json').read_text(encoding='utf-8'))
original_copy = template.translated_copy
def translated(language):
    result = copy.deepcopy(original_copy(language))
    result['sections'] = POLICY[language]
    result['updated'] = result['updated'].split(':')[0] + ': 2026-09-03'
    result['description'] = result['description'].replace('Color Swatch Lab', 'Watch Face Lab')
    result['support_intro'] = POLICY[language][0][1]
    result['support_cards'] = [
        ('Android 9+ · Wear OS 6+', 'Watch Face Push · Android 16+ (watch).'),
        POLICY[language][2], POLICY[language][4], POLICY[language][-1],
    ]
    return result

def branded(html):
    html = html.replace('Color Swatch Lab', 'Watch Face Lab').replace('color-swatch-lab', 'watch-face-lab')
    html = html.replace('</head>', '<meta property="og:type" content="website"><meta property="og:title" content="Watch Face Lab · Alternix"><meta property="og:image" content="https://alternixapps.github.io/assets/watch-face-lab.png"></head>')
    providers = '<p class="meta"><a href="https://policies.google.com/privacy">Google Privacy</a> · <a href="https://developers.google.com/admob/android/privacy/play-data-disclosure">Google Mobile Ads data disclosure</a> · <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy</a></p>'
    return html.replace('</main>', providers + '</main>')

def main():
    template.PRODUCT = 'watch-face-lab'
    template.translated_copy = translated
    shutil.copyfile(APP / 'branding/watch-face-lab-logo.svg', ROOT / 'assets/watch-face-lab.svg')
    shutil.copyfile(APP / 'app/src/main/res/drawable-nodpi/watch_face_lab_logo.png', ROOT / 'assets/watch-face-lab.png')
    css = (ROOT / 'assets/color-swatch-lab.css').read_text(encoding='utf-8')
    css = css.replace('color-swatch-lab', 'watch-face-lab')
    for before, after in {'#0b9f94':'#1771c7','#6742dc':'#d84e08','#58d4c9':'#72baff','#967cf0':'#ff9d67',
        '4, 193, 179':'23, 113, 199','100, 64, 218':'255, 104, 20','#5330d6':'#125ea7','#b5a3f4':'#91caff'}.items():
        css = css.replace(before, after)
    (ROOT / 'assets/watch-face-lab.css').write_text(css, encoding='utf-8')
    sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    for lang in template.LANGUAGE_ORDER:
        prefix = Path() if lang == 'en' else Path(lang)
        for page, body in [('privacy', template.privacy_page(lang)), ('support', template.support_page(lang))]:
            path = ROOT / prefix / 'watch-face-lab' / page / 'index.html'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(branded(body)+'\n', encoding='utf-8')
            url = f'https://alternixapps.github.io/{(prefix / "watch-face-lab" / page).as_posix()}/'
            if f'<loc>{url}</loc>' not in sitemap:
                sitemap = sitemap.replace('</urlset>', f'<url><loc>{url}</loc><lastmod>2026-09-03</lastmod></url></urlset>')
        page = ROOT / prefix / 'index.html'
        html = page.read_text(encoding='utf-8')
        if '<h3>Watch Face Lab</h3>' not in html:
            info = copy.deepcopy(home.LOCALIZED_COPY[lang])
            info['tags'] = ('Android · Wear OS', 'Watch Face Lab', info['tags'][2])
            info['description'] = POLICY[lang][0][1].split('. ')[0] + '.'
            card = home.card_html(info).replace('Color Swatch Lab','Watch Face Lab').replace('color-swatch-lab','watch-face-lab')
            cards = list(re.finditer(r'<article class="product-card product-slide" data-product-slide>.*?</article>', html))
            assert len(cards) == 3, (lang, len(cards))
            at = cards[-1].end()
            html = html[:at] + card + html[at:]
            dots = list(home.SLIDER_DOT.finditer(html))
            assert len(dots) == 3
            at = dots[-1].end()
            dot = '<button class="slider-dot" data-slider-dot aria-label="Watch Face Lab"></button>'
            html = html[:at] + dot + html[at:]
            page.write_text(html, encoding='utf-8', newline='')
    (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print('Generated 18 legal/support pages and added the fourth card on 9 homepages.')

if __name__ == '__main__':
    main()
