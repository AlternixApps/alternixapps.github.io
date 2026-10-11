"""Verify that the Color Swatch Lab policy edit changes copy, not site design."""

from html.parser import HTMLParser
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

from generate_color_swatch_lab_pages import LANGUAGE_ORDER, POLICY_DATE, privacy_page, translated_copy
from add_color_swatch_lab_home_card import LOCALIZED_COPY, PLAY_URL, PRODUCT_CARD, SLIDER_DOT, card_html


ROOT = Path(__file__).resolve().parents[1]


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append(("start", tag, attrs))

    def handle_endtag(self, tag):
        self.elements.append(("end", tag))


def policy_path(language: str) -> str:
    prefix = "" if language == "en" else f"{language}/"
    return f"{prefix}color-swatch-lab/privacy/index.html"


for language in LANGUAGE_ORDER:
    path = policy_path(language)
    before = subprocess.check_output(["git", "show", f"HEAD:{path}"], cwd=ROOT).decode("utf-8")
    after = (ROOT / path).read_text(encoding="utf-8")

    old_structure, new_structure = Structure(), Structure()
    old_structure.feed(before)
    new_structure.feed(after)
    assert old_structure.elements == new_structure.elements, (
        language,
        "HTML structure or attributes changed",
    )
    assert after == privacy_page(language) + "\n", (language, "page differs from generator")
    assert len(translated_copy(language)["sections"]) == 9, language
    for required in ("Color Swatch Lab", "Alternix", "AdMob", "App Set ID", "GitHub", "13–17", "18+", "alternix.apps@gmail.com"):
        assert required in after, (language, required)

for language, copy in LOCALIZED_COPY.items():
    path = copy["path"]
    before = subprocess.check_output(["git", "show", f"HEAD:{path}"], cwd=ROOT).decode("utf-8")
    after = (ROOT / path).read_text(encoding="utf-8")
    old_cards = [match.group() for match in PRODUCT_CARD.finditer(before)]
    new_cards = [match.group() for match in PRODUCT_CARD.finditer(after)]
    target = '<h3>Color Swatch Lab</h3>'
    assert len(old_cards) == len(new_cards), (language, "product count changed")
    assert [card for card in old_cards if target not in card] == [card for card in new_cards if target not in card], (language, "other products changed")
    colour_cards = [card for card in new_cards if target in card]
    assert colour_cards == [card_html(copy)], (language, "card differs from generator")
    assert PLAY_URL in colour_cards[0] and 'class="store-link"' in colour_cards[0], language
    assert 'class="chip"' not in colour_cards[0] and '/support/' not in colour_cards[0], language
    assert len(list(SLIDER_DOT.finditer(after))) == len(new_cards), language
    # The card is the only allowed change to each homepage.
    old_colour = next(card for card in old_cards if target in card)
    assert before.replace(old_colour, colour_cards[0], 1) == after, (language, "homepage changed outside colour card")

changed = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=ROOT).decode().splitlines()
allowed = {
    "scripts/generate_color_swatch_lab_pages.py",
    "scripts/verify_color_swatch_policy_text_only.py",
    "scripts/add_color_swatch_lab_home_card.py",
    "sitemap.xml",
}
for path in changed:
    assert path in allowed or path in {copy["path"] for copy in LOCALIZED_COPY.values()} or path.endswith("color-swatch-lab/privacy/index.html"), path

sitemap = ET.parse(ROOT / "sitemap.xml")
namespace = {"site": "http://www.sitemaps.org/schemas/sitemap/0.9"}
color_policy_entries = [
    entry
    for entry in sitemap.findall("site:url", namespace)
    if entry.findtext("site:loc", namespaces=namespace).endswith("color-swatch-lab/privacy/")
]
assert len(color_policy_entries) == 9
assert all(entry.findtext("site:lastmod", namespaces=namespace) == POLICY_DATE for entry in color_policy_entries)

print(
    "PASS: all 9 Color Swatch Lab privacy pages match the generator and retain "
    "the exact HTML element/attribute structure; all 9 home cards use the correct "
    "Google Play link and one localized privacy action. Styles, browser scripts, "
    "support pages and other products are unchanged."
)
