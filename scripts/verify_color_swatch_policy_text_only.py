"""Verify that the Color Swatch Lab policy edit changes copy, not site design."""

from html.parser import HTMLParser
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

from generate_color_swatch_lab_pages import LANGUAGE_ORDER, privacy_page, translated_copy


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
    for required in ("Color Swatch Lab", "Alternix", "AdMob", "UMP", "GitHub", "13–17", "18+", "alternix.apps@gmail.com"):
        assert required in after, (language, required)

changed = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=ROOT).decode().splitlines()
allowed = {
    "scripts/generate_color_swatch_lab_pages.py",
    "scripts/verify_color_swatch_policy_text_only.py",
    "sitemap.xml",
}
for path in changed:
    assert path in allowed or path.endswith("color-swatch-lab/privacy/index.html"), path

sitemap = ET.parse(ROOT / "sitemap.xml")
namespace = {"site": "http://www.sitemaps.org/schemas/sitemap/0.9"}
color_policy_entries = [
    entry
    for entry in sitemap.findall("site:url", namespace)
    if entry.findtext("site:loc", namespaces=namespace).endswith("color-swatch-lab/privacy/")
]
assert len(color_policy_entries) == 9
assert all(entry.findtext("site:lastmod", namespaces=namespace) == "2026-09-09" for entry in color_policy_entries)

print(
    "PASS: all 9 Color Swatch Lab privacy pages match the generator and retain "
    "the exact HTML element/attribute structure; styles, scripts, support pages "
    "and other products are unchanged."
)
