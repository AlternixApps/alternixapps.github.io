from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LOCALIZED_COPY = {
    "en": {
        "path": "index.html",
        "prefix": "",
        "store_label": "Color Swatch Lab on Google Play",
        "description": (
            "Find colours around you and in photos, explore combinations and shades, "
            "and check contrast. Save and export palettes for your projects."
        ),
        "more": "Learn more",
        "dot": "Show Color Swatch Lab",
    },
    "uk": {
        "path": "uk/index.html",
        "prefix": "/uk",
        "store_label": "Color Swatch Lab у Google Play",
        "description": (
            "Знаходьте кольори навколо себе й на фотографіях, добирайте поєднання та "
            "відтінки, перевіряйте контраст. Зберігайте й експортуйте палітри для своїх проєктів."
        ),
        "more": "Дізнатися більше",
        "dot": "Показати Color Swatch Lab",
    },
    "ru": {
        "path": "ru/index.html",
        "prefix": "/ru",
        "store_label": "Color Swatch Lab в Google Play",
        "description": (
            "Находите цвета вокруг себя и на фотографиях, подбирайте сочетания и оттенки, "
            "проверяйте контраст. Сохраняйте и экспортируйте палитры для своих проектов."
        ),
        "more": "Узнать больше",
        "dot": "Показать Color Swatch Lab",
    },
    "es": {
        "path": "es/index.html",
        "prefix": "/es",
        "store_label": "Color Swatch Lab en Google Play",
        "description": (
            "Encuentra colores a tu alrededor y en tus fotos, explora combinaciones y tonos "
            "y comprueba el contraste. Guarda y exporta paletas para tus proyectos."
        ),
        "more": "Más información",
        "dot": "Mostrar Color Swatch Lab",
    },
    "de": {
        "path": "de/index.html",
        "prefix": "/de",
        "store_label": "Color Swatch Lab bei Google Play",
        "description": (
            "Entdecke Farben in deiner Umgebung und auf Fotos, finde Kombinationen und "
            "Farbtöne und prüfe den Kontrast. Speichere und exportiere Paletten für deine Projekte."
        ),
        "more": "Mehr erfahren",
        "dot": "Color Swatch Lab anzeigen",
    },
    "fr": {
        "path": "fr/index.html",
        "prefix": "/fr",
        "store_label": "Color Swatch Lab sur Google Play",
        "description": (
            "Repérez les couleurs autour de vous et dans vos photos, explorez les associations "
            "et les nuances, puis vérifiez le contraste. Enregistrez et exportez des palettes pour vos projets."
        ),
        "more": "En savoir plus",
        "dot": "Afficher Color Swatch Lab",
    },
    "pt": {
        "path": "pt/index.html",
        "prefix": "/pt",
        "store_label": "Color Swatch Lab no Google Play",
        "description": (
            "Descubra cores à sua volta e nas fotografias, explore combinações e tons "
            "e verifique o contraste. Guarde e exporte paletas para os seus projetos."
        ),
        "more": "Saiba mais",
        "dot": "Mostrar Color Swatch Lab",
    },
    "it": {
        "path": "it/index.html",
        "prefix": "/it",
        "store_label": "Color Swatch Lab su Google Play",
        "description": (
            "Trova i colori intorno a te e nelle foto, esplora combinazioni e sfumature "
            "e verifica il contrasto. Salva ed esporta palette per i tuoi progetti."
        ),
        "more": "Scopri di più",
        "dot": "Mostra Color Swatch Lab",
    },
    "pl": {
        "path": "pl/index.html",
        "prefix": "/pl",
        "store_label": "Color Swatch Lab w Google Play",
        "description": (
            "Odkrywaj kolory wokół siebie i na zdjęciach, dobieraj zestawienia i odcienie "
            "oraz sprawdzaj kontrast. Zapisuj i eksportuj palety do swoich projektów."
        ),
        "more": "Dowiedz się więcej",
        "dot": "Pokaż Color Swatch Lab",
    },
}

PLACEHOLDER_CARD = re.compile(
    r'<article class="product-card product-slide" data-product-slide>'
    r'<div class="product-copy"><div class="product-meta">'
    r'<span class="chip">Alternix</span>.*?'
    r'<img class="upcoming-mark".*?</div></article>',
)

SLIDER_DOT = re.compile(
    r'<button class="slider-dot(?: is-active)?" data-slider-dot '
    r'aria-label="[^"]+"(?: aria-current="true")?></button>'
)

PRODUCT_CARD = re.compile(
    r'<article class="product-card product-slide" data-product-slide>.*?</article>'
)
PLAY_URL = "https://play.google.com/store/apps/details?id=com.alternix.colorswatchlab"


def card_html(copy: dict[str, object]) -> str:
    prefix = str(copy["prefix"])
    privacy = f"{prefix}/color-swatch-lab/privacy/"
    return (
        '<article class="product-card product-slide" data-product-slide>'
        '<div class="product-copy"><div class="product-meta">'
        f'<a class="store-link" href="{PLAY_URL}" target="_blank" '
        f'rel="noopener noreferrer" aria-label="{copy["store_label"]}">'
        '<img src="/assets/google-play.svg" alt="">Google Play</a>'
        f'</div><h3>Color Swatch Lab</h3><p>{copy["description"]}</p>'
        '<div class="product-actions">'
        f'<a class="button button-primary" href="{privacy}">{copy["more"]}</a>'
        '</div></div>'
        f'<a class="product-visual" href="{privacy}" aria-label="Color Swatch Lab">'
        '<img class="app-icon" src="/assets/color-swatch-lab.png" alt="Color Swatch Lab"></a>'
        '</article>'
    )


def update_page(copy: dict[str, object]) -> None:
    page = ROOT / str(copy["path"])
    html = page.read_text(encoding="utf-8")
    cards = list(PRODUCT_CARD.finditer(html))
    colour_cards = [card for card in cards if '<h3>Color Swatch Lab</h3>' in card.group()]
    if len(colour_cards) == 1:
        card = colour_cards[0]
        html = html[:card.start()] + card_html(copy) + html[card.end():]
        colour_index = cards.index(card)
    elif not colour_cards:
        html, count = PLACEHOLDER_CARD.subn(card_html(copy), html, count=1)
        if count != 1:
            raise RuntimeError(f"Expected one upcoming-product card in {page}, found {count}")
        cards = list(PRODUCT_CARD.finditer(html))
        colour_index = next(i for i, card in enumerate(cards) if '<h3>Color Swatch Lab</h3>' in card.group())
    else:
        raise RuntimeError(f"Expected one Color Swatch Lab card in {page}")

    dots = list(SLIDER_DOT.finditer(html))
    if len(dots) != len(cards):
        raise RuntimeError(f"Expected one dot per product in {page}, found {len(dots)} for {len(cards)} cards")
    third = dots[colour_index]
    replacement = (
        '<button class="slider-dot" data-slider-dot '
        f'aria-label="{copy["dot"]}"></button>'
    )
    html = html[: third.start()] + replacement + html[third.end() :]
    page.write_text(html, encoding="utf-8", newline="")


def main() -> None:
    for localized_copy in LOCALIZED_COPY.values():
        update_page(localized_copy)


if __name__ == "__main__":
    main()
