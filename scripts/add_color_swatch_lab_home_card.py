from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LOCALIZED_COPY = {
    "en": {
        "path": "index.html",
        "prefix": "",
        "tags": ("Android", "Color tools", "In development"),
        "description": (
            "Capture colors with the camera or from photos, convert color models, "
            "check contrast, build harmonies and keep palettes on your device."
        ),
        "more": "Learn more",
        "support": "Support",
        "dot": "Show Color Swatch Lab",
    },
    "uk": {
        "path": "uk/index.html",
        "prefix": "/uk",
        "tags": ("Android", "Колір", "У розробці"),
        "description": (
            "Визначайте кольори камерою та з фотографій, перетворюйте колірні моделі, "
            "перевіряйте контраст, створюйте гармонії й зберігайте палітри на пристрої."
        ),
        "more": "Докладніше",
        "support": "Підтримка",
        "dot": "Показати Color Swatch Lab",
    },
    "ru": {
        "path": "ru/index.html",
        "prefix": "/ru",
        "tags": ("Android", "Цвет", "В разработке"),
        "description": (
            "Определяйте цвета камерой и по фотографии, переводите их между цветовыми "
            "моделями, проверяйте контраст, создавайте гармонии и сохраняйте палитры на устройстве."
        ),
        "more": "Подробнее",
        "support": "Поддержка",
        "dot": "Показать Color Swatch Lab",
    },
    "es": {
        "path": "es/index.html",
        "prefix": "/es",
        "tags": ("Android", "Color", "En desarrollo"),
        "description": (
            "Captura colores con la cámara o desde fotos, convierte modelos de color, "
            "comprueba el contraste, crea armonías y guarda paletas en el dispositivo."
        ),
        "more": "Más información",
        "support": "Soporte",
        "dot": "Mostrar Color Swatch Lab",
    },
    "de": {
        "path": "de/index.html",
        "prefix": "/de",
        "tags": ("Android", "Farbe", "In Entwicklung"),
        "description": (
            "Farben mit Kamera oder Fotos erfassen, Farbmodelle umrechnen, Kontraste prüfen, "
            "Harmonien erstellen und Paletten lokal speichern."
        ),
        "more": "Mehr erfahren",
        "support": "Support",
        "dot": "Color Swatch Lab anzeigen",
    },
    "fr": {
        "path": "fr/index.html",
        "prefix": "/fr",
        "tags": ("Android", "Couleur", "En développement"),
        "description": (
            "Capturez des couleurs avec l’appareil photo ou depuis vos images, convertissez "
            "les modèles, vérifiez le contraste et créez des palettes locales."
        ),
        "more": "En savoir plus",
        "support": "Assistance",
        "dot": "Afficher Color Swatch Lab",
    },
    "pt": {
        "path": "pt/index.html",
        "prefix": "/pt",
        "tags": ("Android", "Cor", "Em desenvolvimento"),
        "description": (
            "Capture cores com a câmara ou fotografias, converta modelos de cor, verifique "
            "o contraste, crie harmonias e guarde paletas no dispositivo."
        ),
        "more": "Saiba mais",
        "support": "Suporte",
        "dot": "Mostrar Color Swatch Lab",
    },
    "it": {
        "path": "it/index.html",
        "prefix": "/it",
        "tags": ("Android", "Colore", "In sviluppo"),
        "description": (
            "Acquisisci colori dalla fotocamera o dalle foto, converti i modelli colore, "
            "verifica il contrasto, crea armonie e salva palette sul dispositivo."
        ),
        "more": "Scopri di più",
        "support": "Supporto",
        "dot": "Mostra Color Swatch Lab",
    },
    "pl": {
        "path": "pl/index.html",
        "prefix": "/pl",
        "tags": ("Android", "Kolor", "W przygotowaniu"),
        "description": (
            "Przechwytuj kolory z aparatu lub zdjęć, przeliczaj modele kolorów, sprawdzaj "
            "kontrast, twórz harmonie i zapisuj palety na urządzeniu."
        ),
        "more": "Dowiedz się więcej",
        "support": "Wsparcie",
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


def card_html(copy: dict[str, object]) -> str:
    prefix = str(copy["prefix"])
    tags = "".join(f'<span class="chip">{tag}</span>' for tag in copy["tags"])
    privacy = f"{prefix}/color-swatch-lab/privacy/"
    support = f"{prefix}/color-swatch-lab/support/"
    return (
        '<article class="product-card product-slide" data-product-slide>'
        '<div class="product-copy"><div class="product-meta">'
        f'{tags}</div><h3>Color Swatch Lab</h3><p>{copy["description"]}</p>'
        '<div class="product-actions">'
        f'<a class="button button-primary" href="{privacy}">{copy["more"]}</a>'
        f'<a class="button" href="{support}">{copy["support"]}</a>'
        '</div></div>'
        f'<a class="product-visual" href="{privacy}" aria-label="Color Swatch Lab">'
        '<img class="app-icon" src="/assets/color-swatch-lab.png" alt="Color Swatch Lab"></a>'
        '</article>'
    )


def update_page(copy: dict[str, object]) -> None:
    page = ROOT / str(copy["path"])
    html = page.read_text(encoding="utf-8")
    if "Color Swatch Lab</h3>" not in html:
        html, count = PLACEHOLDER_CARD.subn(card_html(copy), html, count=1)
        if count != 1:
            raise RuntimeError(f"Expected one upcoming-product card in {page}, found {count}")

    dots = list(SLIDER_DOT.finditer(html))
    if len(dots) != 3:
        raise RuntimeError(f"Expected three product dots in {page}, found {len(dots)}")
    third = dots[2]
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
