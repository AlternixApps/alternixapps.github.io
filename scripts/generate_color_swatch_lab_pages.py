from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCT = "color-swatch-lab"
BASE_URL = "https://alternixapps.github.io"
LANGUAGE_NAMES = {
    "de": "Deutsch",
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "it": "Italiano",
    "pl": "Polski",
    "pt": "Português",
    "ru": "Русский",
    "uk": "Українська",
}
LANGUAGE_ORDER = tuple(LANGUAGE_NAMES)


COPY = {
    "en": {
        "code": "EN", "skip": "Skip to content", "privacy": "Privacy Policy",
        "support": "Support", "developer": "Developer", "updated": "Updated: August 23, 2026",
        "on_page": "On this page", "official": "Official Alternix website",
        "description": "Privacy Policy for Color Swatch Lab on Android.",
        "sections": [
            ("Overview", "Color Swatch Lab is an Android colour utility published by Alternix. It does not require an account and has no Alternix cloud backend. Entered colour values, camera frames, selected photos, colour calculations, contrast checks, harmonies and palettes are processed on the device. Alternix does not receive the colours, photos or palettes you work with."),
            ("Local history and settings", "The current colour, colour history, favourites, saved palettes, app language, theme and selected age category may be stored locally so they remain available. You can delete history and palettes in the app. Local data is removed when you clear the app’s data or uninstall it. Android system backup is disabled for Color Swatch Lab."),
            ("Camera and selected photos", "Camera permission is requested only when you start the camera colour scanner. The system Photo Picker gives the app access only to an image you select and does not grant broad gallery access. Camera frames and selected images are analysed locally to sample colours or extract a palette; Alternix does not upload them. Denying camera access does not prevent manual colour entry or photo selection."),
            ("Advertising and consent", "Color Swatch Lab uses Google Mobile Ads SDK (AdMob) for banner ads on several screens. A rewarded ad is offered before palette extraction from a photo and before palette export. Google and its partners may automatically process or share an IP address, approximate location inferred from IP, device or account identifiers, app and ad interactions, diagnostic information, consent choices and related signals for advertising, analytics, measurement, fraud prevention and security. Google User Messaging Platform (UMP) requests and stores privacy choices where required. App colours, photos and palette contents are not intentionally sent to AdMob."),
            ("Age-aware ad treatment", "Before the first ad request, the app asks you to choose “13–17” or “18+”. Only the category is stored locally; no birth date or exact age is requested. For ages 13–17, Google Mobile Ads receives TEEN treatment, ad personalisation is disabled, the maximum ad content rating is G, and UMP receives an under-age-of-consent signal. For 18+, treatment is UNSPECIFIED and UMP manages consent and personalisation under your choices and applicable rules. Changing the category in settings applies a new configuration before subsequent ad requests."),
            ("Exports and sharing", "Palettes can be exported as PNG, JPEG, SVG, PDF, TXT, JSON or CSS after the applicable rewarded-ad step. Android’s system document picker lets you choose where a file is saved. When you share an exported file, Android passes it only to the app or service you select. Temporary share files are kept in the app cache and are not uploaded to an Alternix server."),
            ("Permissions, libraries and providers", "The app declares camera access, Internet access and network-state access. Internet is used by AdMob and UMP, not to upload your colour work. AndroidX, Jetpack Compose, Room, CameraX and the local colour-processing code run on the device. Google Mobile Ads SDK and UMP communicate with Google for advertising and privacy choices. Firebase Analytics and Crashlytics are not used. This website is hosted by GitHub Pages, whose infrastructure may process standard web request data. See the privacy policies of <a href=\"https://policies.google.com/privacy\">Google</a> and <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Retention, security and younger users", "Alternix keeps no server-side copy of app content because Color Swatch Lab has no Alternix account or backend. Local records remain until you delete them, clear app data or uninstall the app. Advertising providers retain data under their own policies and your consent choices. Color Swatch Lab is intended for users aged 13 and over and is not directed to children under 13. Data transmitted by Google Mobile Ads is encrypted in transit using TLS according to Google’s SDK disclosure."),
            ("Your choices, changes and contact", "You can deny or revoke camera permission, use manual entry instead, delete local history and palettes, change your age category, change advertising privacy choices when the option is required, and decline optional rewarded ads. We may update this policy when the app, SDKs or legal requirements change; the current version and date remain at this public URL. Privacy questions can be sent to <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Help with Color Swatch Lab, local colour tools, advertising privacy and exports.",
        "support_cards": [
            ("Contact support", "Email <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Include the app version, Android version, phone model and the steps that reproduce the problem."),
            ("Camera and photos", "Camera access is optional and is requested only for the scanner. Photo selection uses Android Photo Picker. Check Android app permissions if the camera cannot open."),
            ("Ads and exports", "A network connection and an available rewarded ad are required for protected extraction and export actions. Privacy choices, regional availability and ad inventory can affect whether an ad is available."),
            ("Privacy", "Read what stays on the device and what the Google advertising SDK may process in the Color Swatch Lab privacy policy."),
        ],
    },
    "ru": {
        "code": "RU", "skip": "Перейти к содержанию", "privacy": "Политика конфиденциальности",
        "support": "Поддержка", "developer": "Разработчик", "updated": "Обновлено: 23 августа 2026 года",
        "on_page": "На этой странице", "official": "Официальный сайт Alternix",
        "description": "Политика конфиденциальности Color Swatch Lab для Android.",
        "sections": [
            ("Общие сведения", "Color Swatch Lab — Android-инструмент для работы с цветом, выпускаемый Alternix. Приложение не требует учётной записи и не использует облачную серверную часть Alternix. Введённые значения цвета, кадры камеры, выбранные фотографии, расчёты, проверка контраста, гармонии и палитры обрабатываются на устройстве. Alternix не получает цвета, фотографии и палитры, с которыми вы работаете."),
            ("Локальная история и настройки", "Текущий цвет, история, избранное, сохранённые палитры, язык, тема и выбранная возрастная категория могут храниться локально для повторного использования. Историю и палитры можно удалять в приложении. Локальные данные исчезают после очистки данных приложения или его удаления. Системное резервное копирование Android для Color Swatch Lab отключено."),
            ("Камера и выбранные фотографии", "Разрешение камеры запрашивается только при запуске сканера цвета. Системный Photo Picker даёт доступ только к выбранному изображению и не открывает приложению всю галерею. Кадры камеры и фотографии анализируются локально для выбора цвета или извлечения палитры; Alternix их не загружает. Отказ от камеры не мешает ручному вводу и выбору фотографии."),
            ("Реклама и согласие", "Color Swatch Lab использует Google Mobile Ads SDK (AdMob) для баннеров на нескольких экранах. Реклама с вознаграждением предлагается перед извлечением палитры из фотографии и перед экспортом палитры. Google и его партнёры могут автоматически обрабатывать или передавать IP-адрес, приблизительное местоположение по IP, идентификаторы устройства или аккаунта, взаимодействия с приложением и рекламой, диагностические сведения, выбор согласия и связанные сигналы для рекламы, аналитики, измерений, предотвращения мошенничества и безопасности. Google User Messaging Platform (UMP) запрашивает и сохраняет настройки конфиденциальности там, где это требуется. Цвета, фотографии и содержимое палитр намеренно не передаются AdMob."),
            ("Реклама с учётом возраста", "До первого рекламного запроса приложение предлагает выбрать «13–17» или «18+». Локально хранится только категория; дата рождения и точный возраст не запрашиваются. Для 13–17 в Google Mobile Ads передаётся режим TEEN, персонализация отключается, максимальный рейтинг контента ограничивается G, а UMP получает признак пользователя младше возраста согласия. Для 18+ применяется режим UNSPECIFIED, а UMP управляет согласием и персонализацией согласно вашему выбору и применимым правилам. При смене категории новая конфигурация применяется до следующих рекламных запросов."),
            ("Экспорт и отправка", "После предусмотренного шага с рекламой палитры можно экспортировать в PNG, JPEG, SVG, PDF, TXT, JSON или CSS. Место сохранения выбирается в системном окне Android. При отправке Android передаёт файл только выбранному вами приложению или сервису. Временные файлы отправки находятся в кэше приложения и не загружаются на сервер Alternix."),
            ("Разрешения, библиотеки и поставщики", "Приложение объявляет доступ к камере, Интернету и состоянию сети. Интернет нужен AdMob и UMP, а не для загрузки вашей работы с цветом. AndroidX, Jetpack Compose, Room, CameraX и обработка цвета работают на устройстве. Google Mobile Ads SDK и UMP обращаются к Google для рекламы и настроек конфиденциальности. Firebase Analytics и Crashlytics не используются. Сайт размещён на GitHub Pages, инфраструктура которого может обрабатывать стандартные данные веб-запроса. См. политики <a href=\"https://policies.google.com/privacy\">Google</a> и <a href=\"https://docs.github.com/ru/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Хранение, безопасность и младшие пользователи", "Alternix не хранит серверную копию содержимого приложения, поскольку у Color Swatch Lab нет аккаунта или серверной части Alternix. Локальные записи остаются до их удаления, очистки данных или удаления приложения. Рекламные поставщики хранят данные по своим правилам и выбранному согласию. Color Swatch Lab предназначен для пользователей от 13 лет и не ориентирован на детей младше 13 лет. По сведениям Google, данные Mobile Ads передаются с шифрованием TLS."),
            ("Ваш выбор, изменения и контакты", "Можно отклонить или отозвать разрешение камеры, использовать ручной ввод, удалить историю и палитры, изменить возрастную категорию и настройки рекламной конфиденциальности, когда такой пункт требуется, а также отказаться от необязательной рекламы с вознаграждением. Политика может обновляться при изменении приложения, SDK или требований закона; актуальная дата остаётся по этому публичному адресу. Вопросы: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Помощь по Color Swatch Lab, локальным цветовым инструментам, рекламе и экспорту.",
        "support_cards": [
            ("Связаться с поддержкой", "Напишите на <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Укажите версию приложения и Android, модель телефона и шаги, на которых повторяется проблема."),
            ("Камера и фотографии", "Камера необязательна и запрашивается только для сканера. Фотография выбирается через системный Photo Picker. Если камера не открывается, проверьте разрешение приложения в Android."),
            ("Реклама и экспорт", "Для защищённых действий извлечения и экспорта нужны Интернет и доступный ролик с вознаграждением. На доступность влияют регион, настройки конфиденциальности и наличие рекламы."),
            ("Конфиденциальность", "Что остаётся на устройстве и какие данные может обрабатывать рекламный SDK Google, описано в политике Color Swatch Lab."),
        ],
    },
    "uk": {
        "code": "UK", "skip": "Перейти до вмісту", "privacy": "Політика конфіденційності",
        "support": "Підтримка", "developer": "Розробник", "updated": "Оновлено: 23 серпня 2026 року",
        "on_page": "На цій сторінці", "official": "Офіційний сайт Alternix",
        "description": "Політика конфіденційності Color Swatch Lab для Android.",
        "sections": [
            ("Загальні відомості", "Color Swatch Lab — Android-інструмент для роботи з кольором від Alternix. Застосунок не потребує облікового запису й не має хмарної серверної частини Alternix. Уведені значення кольору, кадри камери, вибрані фотографії, розрахунки, перевірки контрасту, гармонії та палітри обробляються на пристрої. Alternix не отримує кольори, фотографії чи палітри, з якими ви працюєте."),
            ("Локальна історія та налаштування", "Поточний колір, історія, вибране, збережені палітри, мова, тема й вибрана вікова категорія можуть зберігатися локально. Історію та палітри можна видаляти в застосунку. Локальні дані зникають після очищення даних або видалення застосунку. Системне резервне копіювання Android вимкнено."),
            ("Камера та вибрані фотографії", "Дозвіл камери запитується лише під час запуску сканера кольору. Системний Photo Picker надає доступ тільки до вибраного зображення, а не до всієї галереї. Кадри й фото аналізуються локально для вибору кольору або вилучення палітри; Alternix їх не завантажує. Відмова від камери не заважає ручному вводу чи вибору фото."),
            ("Реклама та згода", "Color Swatch Lab використовує Google Mobile Ads SDK (AdMob) для банерів на кількох екранах. Реклама з винагородою пропонується перед вилученням палітри з фото та перед експортом палітри. Google і партнери можуть автоматично обробляти або передавати IP-адресу, приблизне місцезнаходження за IP, ідентифікатори пристрою чи облікового запису, взаємодії із застосунком і рекламою, діагностику, вибір згоди та пов’язані сигнали для реклами, аналітики, вимірювань, запобігання шахрайству й безпеки. Google User Messaging Platform (UMP) запитує та зберігає налаштування конфіденційності, де це потрібно. Кольори, фотографії й уміст палітр навмисно не передаються AdMob."),
            ("Реклама з урахуванням віку", "До першого рекламного запиту застосунок пропонує вибрати «13–17» або «18+». Локально зберігається лише категорія; дата народження й точний вік не запитуються. Для 13–17 Google Mobile Ads отримує режим TEEN, персоналізація вимикається, рейтинг контенту обмежується G, а UMP отримує ознаку користувача молодше віку згоди. Для 18+ застосовується UNSPECIFIED, а UMP керує згодою та персоналізацією відповідно до вашого вибору й чинних правил."),
            ("Експорт і поширення", "Після передбаченого кроку з рекламою палітри можна експортувати в PNG, JPEG, SVG, PDF, TXT, JSON або CSS. Місце збереження вибирається в системному вікні Android. Під час поширення Android передає файл лише вибраному застосунку чи сервісу. Тимчасові файли зберігаються в кеші й не завантажуються на сервер Alternix."),
            ("Дозволи, бібліотеки та постачальники", "Застосунок оголошує доступ до камери, Інтернету й стану мережі. Інтернет потрібен AdMob і UMP, а не для завантаження вашої роботи з кольором. AndroidX, Jetpack Compose, Room, CameraX та обробка кольору працюють на пристрої. Google Mobile Ads SDK і UMP звертаються до Google для реклами й налаштувань конфіденційності. Firebase Analytics і Crashlytics не використовуються. Сайт розміщений на GitHub Pages. Див. політики <a href=\"https://policies.google.com/privacy\">Google</a> і <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Зберігання, безпека й молодші користувачі", "Alternix не зберігає серверну копію вмісту, адже Color Swatch Lab не має облікового запису чи серверної частини Alternix. Локальні записи залишаються до видалення, очищення даних або видалення застосунку. Рекламні постачальники зберігають дані за власними правилами й вашим вибором згоди. Застосунок призначений для користувачів від 13 років і не орієнтований на дітей до 13 років. За даними Google, Mobile Ads передає дані із шифруванням TLS."),
            ("Ваш вибір, зміни та контакти", "Можна відхилити або відкликати дозвіл камери, користуватися ручним вводом, видалити історію й палітри, змінити вікову категорію та рекламні налаштування конфіденційності, а також відмовитися від необов’язкової реклами з винагородою. Політика може оновлюватися разом із застосунком, SDK або вимогами закону. Питання: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Допомога щодо Color Swatch Lab, інструментів кольору, реклами й експорту.",
        "support_cards": [
            ("Зв’язатися з підтримкою", "Напишіть на <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Укажіть версію застосунку й Android, модель телефона та кроки відтворення."),
            ("Камера та фотографії", "Камера необов’язкова й потрібна лише сканеру. Фото вибирається через системний Photo Picker. Якщо камера не відкривається, перевірте дозвіл у налаштуваннях Android."),
            ("Реклама та експорт", "Для захищених дій вилучення й експорту потрібні Інтернет і доступний ролик із винагородою. Доступність залежить від регіону, вибору конфіденційності та рекламного інвентарю."),
            ("Конфіденційність", "Що залишається на пристрої та які дані може обробляти рекламний SDK Google, описано в політиці Color Swatch Lab."),
        ],
    },
}


def translated_copy(language: str) -> dict:
    if language in COPY:
        return COPY[language]
    # The remaining localisations use carefully translated navigation and a concise,
    # complete policy. Keeping the same data claims across languages prevents drift.
    return OTHER_COPY[language]


OTHER_COPY = {
    "de": {
        "code": "DE", "skip": "Zum Inhalt springen", "privacy": "Datenschutzerklärung", "support": "Support", "developer": "Entwickler", "updated": "Aktualisiert: 23. August 2026", "on_page": "Auf dieser Seite", "official": "Offizielle Alternix-Website", "description": "Datenschutzerklärung für Color Swatch Lab auf Android.",
        "sections": [
            ("Überblick", "Color Swatch Lab ist ein Android-Farbwerkzeug von Alternix. Es benötigt kein Konto und hat kein Alternix-Cloud-Backend. Farbwerte, Kamerabilder, ausgewählte Fotos, Berechnungen, Kontrastprüfungen, Harmonien und Paletten werden auf dem Gerät verarbeitet. Alternix erhält diese Inhalte nicht."),
            ("Lokale Daten", "Aktuelle Farbe, Verlauf, Favoriten, Paletten, Sprache, Design und Alterskategorie können lokal gespeichert werden. Verlauf und Paletten lassen sich in der App löschen. Die Daten verschwinden beim Löschen der App-Daten oder bei der Deinstallation. Android-Systembackups sind deaktiviert."),
            ("Kamera und Fotos", "Die Kameraberechtigung wird nur für den Farbscanner angefordert. Der Android Photo Picker gewährt nur Zugriff auf das ausgewählte Bild, nicht auf die gesamte Galerie. Bilder werden lokal analysiert und nicht von Alternix hochgeladen. Manuelle Eingabe und Fotoauswahl funktionieren ohne Kameraberechtigung."),
            ("Werbung und Einwilligung", "Color Swatch Lab nutzt Google Mobile Ads SDK (AdMob) für Banner. Vor der Palettenextraktion aus einem Foto und vor dem Palettenexport wird eine optionale Rewarded Ad angeboten. Google und Partner können IP-Adresse, ungefähren Standort aus der IP, Geräte- oder Konto-IDs, App- und Anzeigeninteraktionen, Diagnose- und Einwilligungsdaten für Werbung, Analyse, Messung, Betrugsprävention und Sicherheit verarbeiten oder teilen. UMP verwaltet erforderliche Datenschutzentscheidungen. Farben, Fotos und Paletteninhalte werden nicht absichtlich an AdMob gesendet."),
            ("Altersabhängige Anzeigen", "Vor der ersten Anzeigenanfrage wird „13–17“ oder „18+“ gewählt. Nur die Kategorie wird lokal gespeichert. Für 13–17 gelten Google-TEEN-Behandlung, deaktivierte Personalisierung, Inhaltsrating G und das UMP-Signal „unter Einwilligungsalter“. Für 18+ gilt UNSPECIFIED; UMP verwaltet Einwilligung und Personalisierung. Änderungen werden vor weiteren Anzeigenanfragen angewendet."),
            ("Export und Teilen", "Paletten können nach dem vorgesehenen Werbeschritt als PNG, JPEG, SVG, PDF, TXT, JSON oder CSS exportiert werden. Speicherort und Ziel-App wählen Sie in Android. Temporäre Freigabedateien liegen im App-Cache und werden nicht auf Alternix-Server hochgeladen."),
            ("Berechtigungen und Anbieter", "Die App deklariert Kamera-, Internet- und Netzwerkstatuszugriff. Das Internet wird für AdMob und UMP verwendet. AndroidX, Compose, Room, CameraX und Farbverarbeitung laufen lokal; Firebase Analytics und Crashlytics werden nicht verwendet. Die Website läuft auf GitHub Pages. Siehe <a href=\"https://policies.google.com/privacy\">Google</a> und <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Aufbewahrung und jüngere Nutzer", "Alternix besitzt keine Serverkopie der App-Inhalte. Lokale Daten bleiben bis zur Löschung, Datenbereinigung oder Deinstallation. Werbeanbieter speichern Daten nach ihren Regeln und Ihren Einwilligungsentscheidungen. Die App ist für Nutzer ab 13 Jahren gedacht und nicht an Kinder unter 13 gerichtet. Google gibt TLS-Verschlüsselung bei der Übertragung an."),
            ("Ihre Wahl und Kontakt", "Sie können Kamerazugriff ablehnen, manuell arbeiten, lokale Daten löschen, Alterskategorie und verfügbare Werbe-Datenschutzoptionen ändern sowie Rewarded Ads ablehnen. Änderungen an App, SDK oder Recht können diese Erklärung aktualisieren. Kontakt: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Hilfe zu Color Swatch Lab, Farbwerkzeugen, Werbung und Export.",
        "support_cards": [("Support kontaktieren", "Schreiben Sie an <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> und nennen Sie App-/Android-Version, Gerät und Reproduktionsschritte."), ("Kamera und Fotos", "Die Kamera ist optional. Fotos werden über den Android Photo Picker gewählt. Prüfen Sie bei Problemen die App-Berechtigung."), ("Werbung und Export", "Geschützte Extraktions- und Exportaktionen benötigen Internet und eine verfügbare Rewarded Ad. Region, Datenschutzwahl und Anzeigenbestand beeinflussen die Verfügbarkeit."), ("Datenschutz", "Die Datenschutzerklärung beschreibt lokale Daten und die Verarbeitung durch Googles Anzeigen-SDK.")],
    },
    "es": {
        "code": "ES", "skip": "Ir al contenido", "privacy": "Política de privacidad", "support": "Soporte", "developer": "Desarrollador", "updated": "Actualizado: 23 de agosto de 2026", "on_page": "En esta página", "official": "Sitio oficial de Alternix", "description": "Política de privacidad de Color Swatch Lab para Android.",
        "sections": [
            ("Información general", "Color Swatch Lab es una herramienta de color para Android publicada por Alternix. No requiere cuenta ni usa un backend en la nube de Alternix. Los valores, fotogramas de cámara, fotos seleccionadas, cálculos, contrastes, armonías y paletas se procesan en el dispositivo. Alternix no recibe ese contenido."),
            ("Datos locales", "El color actual, historial, favoritos, paletas, idioma, tema y categoría de edad pueden guardarse localmente. Puedes borrar el historial y las paletas en la app. Los datos desaparecen al borrar los datos de la app o desinstalarla. La copia de seguridad del sistema Android está desactivada."),
            ("Cámara y fotos", "El permiso de cámara solo se solicita al abrir el escáner. Android Photo Picker da acceso únicamente a la imagen elegida, no a toda la galería. Las imágenes se analizan localmente y Alternix no las sube. La entrada manual y la selección de fotos funcionan sin permiso de cámara."),
            ("Publicidad y consentimiento", "Color Swatch Lab usa Google Mobile Ads SDK (AdMob) para banners. Se ofrece un anuncio bonificado antes de extraer una paleta de una foto y antes de exportarla. Google y sus socios pueden procesar o compartir la IP, ubicación aproximada derivada de la IP, identificadores, interacciones, diagnósticos y elecciones de consentimiento para publicidad, análisis, medición, prevención del fraude y seguridad. UMP gestiona las opciones exigidas. Los colores, fotos y contenidos de paletas no se envían intencionadamente a AdMob."),
            ("Tratamiento según la edad", "Antes de la primera solicitud de anuncio se elige “13–17” o “18+”; solo se guarda la categoría. Para 13–17 se aplica TEEN, se desactiva la personalización, se limita el contenido a G y UMP recibe la señal de menor de la edad de consentimiento. Para 18+ se usa UNSPECIFIED y UMP gestiona consentimiento y personalización. Los cambios se aplican antes de nuevas solicitudes."),
            ("Exportación y uso compartido", "Tras el paso publicitario correspondiente, las paletas se exportan como PNG, JPEG, SVG, PDF, TXT, JSON o CSS. Android permite elegir ubicación y aplicación de destino. Los archivos temporales permanecen en la caché y no se suben a Alternix."),
            ("Permisos y proveedores", "La app declara cámara, Internet y estado de red. Internet se usa para AdMob y UMP. AndroidX, Compose, Room, CameraX y el procesamiento de color funcionan localmente; no se usan Firebase Analytics ni Crashlytics. El sitio está en GitHub Pages. Consulta <a href=\"https://policies.google.com/privacy\">Google</a> y <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Conservación y usuarios jóvenes", "Alternix no conserva copia en servidor. Los datos locales permanecen hasta que los borras, limpias la app o la desinstalas. Los proveedores publicitarios conservan datos según sus políticas y tus elecciones. La app es para mayores de 13 años y no se dirige a menores de 13. Google declara cifrado TLS en tránsito."),
            ("Tus opciones y contacto", "Puedes denegar la cámara, usar entrada manual, borrar datos locales, cambiar la categoría y las opciones publicitarias disponibles y rechazar anuncios bonificados. Esta política puede cambiar con la app, los SDK o la ley. Contacto: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Ayuda sobre Color Swatch Lab, herramientas de color, anuncios y exportación.",
        "support_cards": [("Contactar", "Escribe a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> con versión de app/Android, modelo y pasos."), ("Cámara y fotos", "La cámara es opcional; las fotos usan Android Photo Picker. Revisa el permiso si no abre."), ("Anuncios y exportación", "Las acciones protegidas necesitan conexión y un anuncio bonificado disponible; región, privacidad e inventario influyen."), ("Privacidad", "La política explica qué queda en el dispositivo y qué puede procesar el SDK de Google.")],
    },
    "fr": {
        "code": "FR", "skip": "Aller au contenu", "privacy": "Politique de confidentialité", "support": "Assistance", "developer": "Développeur", "updated": "Mise à jour : 23 août 2026", "on_page": "Sur cette page", "official": "Site officiel d’Alternix", "description": "Politique de confidentialité de Color Swatch Lab pour Android.",
        "sections": [
            ("Présentation", "Color Swatch Lab est un outil de couleur Android publié par Alternix. Aucun compte ni serveur cloud Alternix n’est requis. Valeurs, images de caméra, photos choisies, calculs, contrastes, harmonies et palettes sont traités sur l’appareil. Alternix ne reçoit pas ce contenu."),
            ("Données locales", "La couleur courante, l’historique, les favoris, les palettes, la langue, le thème et la catégorie d’âge peuvent être conservés localement. Vous pouvez supprimer historique et palettes. Les données disparaissent après effacement des données ou désinstallation. La sauvegarde système Android est désactivée."),
            ("Caméra et photos", "L’autorisation caméra n’est demandée qu’au lancement du scanner. Android Photo Picker donne accès uniquement à l’image choisie. Les images sont analysées localement et ne sont pas téléversées par Alternix. La saisie manuelle et le choix d’une photo restent disponibles sans caméra."),
            ("Publicité et consentement", "Color Swatch Lab utilise Google Mobile Ads SDK (AdMob) pour des bannières. Une publicité récompensée est proposée avant l’extraction d’une palette depuis une photo et avant l’export. Google et ses partenaires peuvent traiter ou partager adresse IP, localisation approximative issue de l’IP, identifiants, interactions, diagnostics et choix de consentement pour publicité, analyse, mesure, lutte contre la fraude et sécurité. UMP gère les choix requis. Couleurs, photos et palettes ne sont pas volontairement envoyées à AdMob."),
            ("Traitement selon l’âge", "Avant la première demande publicitaire, vous choisissez « 13–17 » ou « 18+ » ; seule la catégorie est stockée. Pour 13–17, le mode TEEN s’applique, la personnalisation est désactivée, le contenu est limité à G et UMP reçoit le signal d’âge de consentement. Pour 18+, UNSPECIFIED s’applique et UMP gère consentement et personnalisation. Les changements précèdent les demandes suivantes."),
            ("Export et partage", "Après l’étape publicitaire prévue, les palettes s’exportent en PNG, JPEG, SVG, PDF, TXT, JSON ou CSS. Android permet de choisir l’emplacement et l’application destinataire. Les fichiers temporaires restent dans le cache et ne sont pas envoyés à Alternix."),
            ("Autorisations et prestataires", "L’application déclare caméra, Internet et état du réseau. Internet sert à AdMob et UMP. AndroidX, Compose, Room, CameraX et le traitement couleur fonctionnent localement ; Firebase Analytics et Crashlytics ne sont pas utilisés. Le site est hébergé par GitHub Pages. Voir <a href=\"https://policies.google.com/privacy\">Google</a> et <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Conservation et jeunes utilisateurs", "Alternix ne conserve aucune copie serveur. Les données locales restent jusqu’à leur suppression, l’effacement de l’application ou sa désinstallation. Les fournisseurs publicitaires conservent les données selon leurs règles et vos choix. L’application s’adresse aux 13 ans et plus, pas aux moins de 13 ans. Google indique un chiffrement TLS en transit."),
            ("Vos choix et contact", "Vous pouvez refuser la caméra, saisir manuellement, supprimer les données locales, modifier catégorie d’âge et choix publicitaires disponibles, et refuser les publicités récompensées. Cette politique peut évoluer avec l’application, les SDK ou la loi. Contact : <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Assistance pour Color Swatch Lab, les outils couleur, la publicité et l’export.",
        "support_cards": [("Contacter l’assistance", "Écrivez à <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> avec versions, modèle et étapes."), ("Caméra et photos", "La caméra est facultative ; les photos utilisent Android Photo Picker. Vérifiez l’autorisation si nécessaire."), ("Publicité et export", "Les actions protégées nécessitent Internet et une publicité récompensée disponible ; région, confidentialité et inventaire influencent la disponibilité."), ("Confidentialité", "La politique décrit les données locales et le traitement possible par le SDK Google.")],
    },
    "it": {
        "code": "IT", "skip": "Vai al contenuto", "privacy": "Informativa sulla privacy", "support": "Supporto", "developer": "Sviluppatore", "updated": "Aggiornata: 23 agosto 2026", "on_page": "In questa pagina", "official": "Sito ufficiale Alternix", "description": "Informativa sulla privacy di Color Swatch Lab per Android.",
        "sections": [
            ("Panoramica", "Color Swatch Lab è uno strumento colore Android pubblicato da Alternix. Non richiede account né un backend cloud Alternix. Valori, fotogrammi, foto scelte, calcoli, contrasti, armonie e tavolozze sono elaborati sul dispositivo. Alternix non riceve questi contenuti."),
            ("Dati locali", "Colore corrente, cronologia, preferiti, tavolozze, lingua, tema e categoria d’età possono essere salvati localmente. Cronologia e tavolozze sono eliminabili nell’app. I dati spariscono cancellando i dati dell’app o disinstallandola. Il backup Android è disattivato."),
            ("Fotocamera e foto", "Il permesso fotocamera è richiesto solo per lo scanner. Android Photo Picker concede accesso soltanto all’immagine scelta. Le immagini sono analizzate localmente e non caricate da Alternix. Inserimento manuale e scelta foto funzionano senza fotocamera."),
            ("Pubblicità e consenso", "Color Swatch Lab usa Google Mobile Ads SDK (AdMob) per banner. Un annuncio con premio viene proposto prima dell’estrazione da foto e dell’esportazione. Google e partner possono elaborare o condividere IP, posizione approssimativa da IP, identificatori, interazioni, diagnostica e scelte di consenso per pubblicità, analisi, misurazione, prevenzione frodi e sicurezza. UMP gestisce le scelte richieste. Colori, foto e contenuti delle tavolozze non vengono intenzionalmente inviati ad AdMob."),
            ("Trattamento per età", "Prima della prima richiesta pubblicitaria scegli “13–17” o “18+”; viene salvata solo la categoria. Per 13–17 si applicano TEEN, personalizzazione disattivata, contenuti G e segnale UMP sotto età del consenso. Per 18+ si usa UNSPECIFIED e UMP gestisce consenso e personalizzazione. Le modifiche valgono prima delle richieste successive."),
            ("Esportazione e condivisione", "Dopo il passaggio pubblicitario previsto, le tavolozze si esportano in PNG, JPEG, SVG, PDF, TXT, JSON o CSS. Android consente di scegliere posizione e app destinataria. I file temporanei restano nella cache e non sono caricati su Alternix."),
            ("Permessi e fornitori", "L’app dichiara fotocamera, Internet e stato rete. Internet serve AdMob e UMP. AndroidX, Compose, Room, CameraX ed elaborazione colore funzionano localmente; Firebase Analytics e Crashlytics non sono usati. Il sito è su GitHub Pages. Vedi <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Conservazione e utenti più giovani", "Alternix non conserva copie server. I dati locali restano fino a eliminazione, pulizia o disinstallazione. I fornitori pubblicitari trattengono dati secondo le proprie regole e le tue scelte. L’app è per utenti dai 13 anni e non è rivolta ai minori di 13. Google dichiara cifratura TLS in transito."),
            ("Scelte e contatto", "Puoi negare la fotocamera, usare l’inserimento manuale, eliminare dati locali, cambiare categoria e opzioni pubblicitarie disponibili e rifiutare annunci con premio. La policy può cambiare con app, SDK o legge. Contatto: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Assistenza per Color Swatch Lab, strumenti colore, annunci ed esportazione.",
        "support_cards": [("Contatta il supporto", "Scrivi a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> indicando versioni, modello e passaggi."), ("Fotocamera e foto", "La fotocamera è facoltativa; le foto usano Android Photo Picker. Controlla il permesso se non si apre."), ("Annunci ed esportazione", "Le azioni protette richiedono Internet e un annuncio con premio disponibile; regione, privacy e inventario incidono."), ("Privacy", "L’informativa descrive dati locali e trattamento possibile da parte dell’SDK Google.")],
    },
    "pl": {
        "code": "PL", "skip": "Przejdź do treści", "privacy": "Polityka prywatności", "support": "Pomoc", "developer": "Deweloper", "updated": "Aktualizacja: 23 sierpnia 2026", "on_page": "Na tej stronie", "official": "Oficjalna strona Alternix", "description": "Polityka prywatności Color Swatch Lab na Androida.",
        "sections": [
            ("Informacje ogólne", "Color Swatch Lab to narzędzie kolorystyczne na Androida wydawane przez Alternix. Nie wymaga konta ani chmury Alternix. Wartości, kadry aparatu, wybrane zdjęcia, obliczenia, kontrast, harmonie i palety są przetwarzane na urządzeniu. Alternix nie otrzymuje tych treści."),
            ("Dane lokalne", "Bieżący kolor, historia, ulubione, palety, język, motyw i kategoria wieku mogą być zapisane lokalnie. Historię i palety można usunąć. Dane znikają po wyczyszczeniu danych lub odinstalowaniu. Kopia systemowa Androida jest wyłączona."),
            ("Aparat i zdjęcia", "Uprawnienie aparatu jest wymagane tylko dla skanera. Android Photo Picker udostępnia wyłącznie wybrane zdjęcie. Obrazy są analizowane lokalnie i nie są wysyłane do Alternix. Ręczne wprowadzanie i wybór zdjęć działają bez aparatu."),
            ("Reklamy i zgoda", "Color Swatch Lab używa Google Mobile Ads SDK (AdMob) do banerów. Reklama z nagrodą jest proponowana przed ekstrakcją palety ze zdjęcia i eksportem. Google i partnerzy mogą przetwarzać lub udostępniać IP, przybliżoną lokalizację z IP, identyfikatory, interakcje, diagnostykę i wybory zgody dla reklam, analityki, pomiaru, zapobiegania oszustwom i bezpieczeństwa. UMP obsługuje wymagane wybory. Kolory, zdjęcia i treść palet nie są celowo wysyłane do AdMob."),
            ("Reklamy a wiek", "Przed pierwszą reklamą wybierasz „13–17” lub „18+”; zapisana jest tylko kategoria. Dla 13–17 działa TEEN, wyłączona personalizacja, rating G i sygnał UMP poniżej wieku zgody. Dla 18+ działa UNSPECIFIED, a UMP zarządza zgodą i personalizacją. Zmiany obowiązują przed kolejnymi żądaniami."),
            ("Eksport i udostępnianie", "Po przewidzianym kroku reklamowym palety eksportuje się jako PNG, JPEG, SVG, PDF, TXT, JSON lub CSS. Android pozwala wybrać miejsce i aplikację. Pliki tymczasowe są w pamięci podręcznej i nie trafiają na serwer Alternix."),
            ("Uprawnienia i dostawcy", "Aplikacja deklaruje aparat, Internet i stan sieci. Internet służy AdMob i UMP. AndroidX, Compose, Room, CameraX i obróbka kolorów działają lokalnie; Firebase Analytics i Crashlytics nie są używane. Witryna jest na GitHub Pages. Zobacz <a href=\"https://policies.google.com/privacy\">Google</a> i <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Przechowywanie i młodsi użytkownicy", "Alternix nie ma kopii serwerowej. Dane lokalne pozostają do usunięcia, wyczyszczenia lub odinstalowania. Dostawcy reklam przechowują dane według swoich zasad i wyborów zgody. Aplikacja jest dla osób od 13 lat i nie jest kierowana do dzieci poniżej 13 lat. Google deklaruje szyfrowanie TLS podczas przesyłania."),
            ("Wybory i kontakt", "Możesz odmówić aparatu, pracować ręcznie, usuwać dane lokalne, zmienić kategorię i dostępne opcje reklamowe oraz odrzucić reklamy z nagrodą. Polityka może zmieniać się z aplikacją, SDK lub prawem. Kontakt: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Pomoc dotycząca Color Swatch Lab, narzędzi kolorów, reklam i eksportu.",
        "support_cards": [("Kontakt z pomocą", "Napisz na <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>, podając wersje, model i kroki."), ("Aparat i zdjęcia", "Aparat jest opcjonalny; zdjęcia używają Android Photo Picker. Sprawdź uprawnienie, jeśli aparat się nie otwiera."), ("Reklamy i eksport", "Chronione działania wymagają Internetu i dostępnej reklamy z nagrodą; wpływają region, prywatność i zasoby reklam."), ("Prywatność", "Polityka opisuje dane lokalne i możliwe przetwarzanie przez SDK Google.")],
    },
    "pt": {
        "code": "PT", "skip": "Ir para o conteúdo", "privacy": "Política de privacidade", "support": "Suporte", "developer": "Programador", "updated": "Atualizada: 23 de agosto de 2026", "on_page": "Nesta página", "official": "Site oficial da Alternix", "description": "Política de privacidade do Color Swatch Lab para Android.",
        "sections": [
            ("Visão geral", "Color Swatch Lab é uma ferramenta de cores Android publicada pela Alternix. Não exige conta nem backend na nuvem da Alternix. Valores, imagens da câmara, fotos escolhidas, cálculos, contrastes, harmonias e paletas são processados no dispositivo. A Alternix não recebe esse conteúdo."),
            ("Dados locais", "Cor atual, histórico, favoritos, paletas, idioma, tema e categoria etária podem ficar guardados localmente. É possível apagar histórico e paletas. Os dados desaparecem ao limpar os dados ou desinstalar. A cópia de segurança Android está desativada."),
            ("Câmara e fotos", "A permissão da câmara só é pedida para o scanner. O Android Photo Picker dá acesso apenas à imagem escolhida. As imagens são analisadas localmente e não são enviadas pela Alternix. A introdução manual e escolha de fotos funcionam sem a câmara."),
            ("Publicidade e consentimento", "Color Swatch Lab usa Google Mobile Ads SDK (AdMob) para banners. Um anúncio premiado é proposto antes de extrair uma paleta de uma foto e antes de exportar. Google e parceiros podem processar ou partilhar IP, localização aproximada pelo IP, identificadores, interações, diagnósticos e escolhas de consentimento para publicidade, análise, medição, prevenção de fraude e segurança. UMP gere as escolhas exigidas. Cores, fotos e conteúdo das paletas não são enviados intencionalmente ao AdMob."),
            ("Tratamento por idade", "Antes do primeiro pedido de anúncio escolhe “13–17” ou “18+”; só a categoria é guardada. Para 13–17 aplica-se TEEN, sem personalização, conteúdo G e sinal UMP abaixo da idade de consentimento. Para 18+ aplica-se UNSPECIFIED e a UMP gere consentimento e personalização. Alterações são aplicadas antes de novos pedidos."),
            ("Exportação e partilha", "Após o passo publicitário previsto, as paletas são exportadas em PNG, JPEG, SVG, PDF, TXT, JSON ou CSS. O Android permite escolher local e aplicação. Ficheiros temporários ficam na cache e não são enviados à Alternix."),
            ("Permissões e fornecedores", "A app declara câmara, Internet e estado da rede. A Internet serve AdMob e UMP. AndroidX, Compose, Room, CameraX e processamento de cor funcionam localmente; Firebase Analytics e Crashlytics não são usados. O site está no GitHub Pages. Consulte <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Retenção e utilizadores jovens", "A Alternix não guarda cópia no servidor. Dados locais ficam até serem apagados, limpos ou a app ser desinstalada. Fornecedores de anúncios retêm dados segundo as suas regras e escolhas. A app destina-se a maiores de 13 anos e não é dirigida a menores de 13. A Google declara encriptação TLS em trânsito."),
            ("Escolhas e contacto", "Pode recusar a câmara, usar entrada manual, apagar dados locais, mudar categoria e opções publicitárias disponíveis e recusar anúncios premiados. A política pode mudar com a app, SDK ou lei. Contacto: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Ajuda sobre Color Swatch Lab, ferramentas de cor, anúncios e exportação.",
        "support_cards": [("Contactar suporte", "Escreva para <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> com versões, modelo e passos."), ("Câmara e fotos", "A câmara é opcional; fotos usam Android Photo Picker. Verifique a permissão se não abrir."), ("Anúncios e exportação", "Ações protegidas precisam de Internet e anúncio premiado disponível; região, privacidade e inventário influenciam."), ("Privacidade", "A política descreve dados locais e possível processamento pelo SDK Google.")],
    },
}


def product_path(language: str, page: str) -> str:
    prefix = "" if language == "en" else f"{language}/"
    return f"/{prefix}{PRODUCT}/{page}/"


def language_links(current: str, page: str) -> str:
    links = []
    for language in LANGUAGE_ORDER:
        current_attr = ' aria-current="page"' if language == current else ""
        links.append(
            f'<a href="{product_path(language, page)}" lang="{language}"{current_attr}>'
            f'{LANGUAGE_NAMES[language]}</a>'
        )
    return "".join(links)


def alternate_links(page: str) -> str:
    links = []
    for language in LANGUAGE_ORDER:
        links.append(
            f'<link rel="alternate" hreflang="{language}" '
            f'href="{BASE_URL}{product_path(language, page)}">'
        )
    links.append(
        f'<link rel="alternate" hreflang="x-default" '
        f'href="{BASE_URL}{product_path("en", page)}">'
    )
    return "".join(links)


def page_shell(language: str, page: str, title: str, description: str, body: str) -> str:
    copy = translated_copy(language)
    privacy_current = ' aria-current="page"' if page == "privacy" else ""
    support_current = ' aria-current="page"' if page == "support" else ""
    developer_path = "/" if language == "en" else f"/{language}"
    canonical = f"{BASE_URL}{product_path(language, page)}"
    return (
        '<!doctype html><html lang="' + language + '"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<meta name="description" content="{escape(description)}">'
        '<meta name="theme-color" content="#f7f8fb">'
        f'<link rel="canonical" href="{canonical}">{alternate_links(page)}'
        f'<title>{escape(title)} — Color Swatch Lab</title>'
        '<script>try{if(localStorage.getItem("alternix-theme")==="dark")'
        'document.documentElement.dataset.theme="dark"}catch(e){}</script>'
        '<link rel="icon" href="/assets/color-swatch-lab.svg">'
        '<link rel="stylesheet" href="/assets/site.css">'
        '<link rel="stylesheet" href="/assets/color-swatch-lab.css?v=20260823-2">'
        '<script src="/assets/site.js" defer></script></head>'
        '<body class="color-swatch-lab">'
        f'<a class="skip-link" href="#content">{escape(copy["skip"])}</a>'
        '<header class="site-header"><div class="header-inner">'
        f'<a class="brand" href="{product_path(language, "privacy")}" aria-label="Color Swatch Lab">'
        '<span class="brand-mark"><img src="/assets/color-swatch-lab.svg" alt=""></span>'
        '<span class="brand-label">Color Swatch Lab</span></a>'
        '<nav class="site-nav" aria-label="Color Swatch Lab">'
        f'<a href="{product_path(language, "privacy")}"{privacy_current}>{escape(copy["privacy"])}</a>'
        f'<a href="{product_path(language, "support")}"{support_current}>{escape(copy["support"])}</a>'
        f'<a href="{developer_path}" class="developer-link">{escape(copy["developer"])}</a></nav>'
        '<div class="header-actions"><details class="language-menu">'
        f'<summary aria-label="Language">{copy["code"]}</summary>'
        f'<div class="language-panel">{language_links(language, page)}</div></details>'
        '<button class="icon-button" type="button" data-theme-toggle '
        'data-light-label="Light" data-dark-label="Dark" aria-label="Theme"></button>'
        '</div></div></header>' + body +
        '<footer class="site-footer"><div class="footer-inner">'
        '<p>© 2026 Alternix · Color Swatch Lab</p>'
        f'<p><a href="{developer_path}">{escape(copy["official"])}</a> · '
        f'<a href="{product_path(language, "support")}">{escape(copy["support"])}</a></p>'
        '</div></footer></body></html>'
    )


def privacy_page(language: str) -> str:
    copy = translated_copy(language)
    sections = []
    toc = []
    for index, (heading, paragraph) in enumerate(copy["sections"], start=1):
        notice = ' class="age-treatment-notice"' if index == 5 else ""
        sections.append(
            f'<section class="legal-section" id="section-{index}"><h2>{escape(heading)}</h2>'
            f'<p{notice}>{paragraph}</p></section>'
        )
        toc.append(f'<li><a href="#section-{index}">{escape(heading)}</a></li>')
    body = (
        '<main class="page" id="content"><header class="legal-header">'
        '<p class="eyebrow">Color Swatch Lab · Android</p>'
        f'<h1>{escape(copy["privacy"])}</h1><p class="meta">{escape(copy["updated"])}</p>'
        '</header><div class="legal-layout"><div class="legal-content">'
        + "".join(sections) + '</div><aside class="toc">'
        f'<strong>{escape(copy["on_page"])}</strong><ol>{"".join(toc)}</ol>'
        '</aside></div></main>'
    )
    return page_shell(language, "privacy", copy["privacy"], copy["description"], body)


def support_page(language: str) -> str:
    copy = translated_copy(language)
    cards = "".join(
        f'<article class="card"><h2>{escape(title)}</h2><p>{text}</p></article>'
        for title, text in copy["support_cards"]
    )
    body = (
        '<main class="page" id="content"><header class="hero">'
        '<p class="eyebrow">Color Swatch Lab · Android</p>'
        f'<h1>{escape(copy["support"])}</h1><p class="lead">{escape(copy["support_intro"])}</p>'
        f'</header><div class="grid">{cards}</div></main>'
    )
    return page_shell(language, "support", copy["support"], copy["support_intro"], body)


def write_pages() -> None:
    for language in LANGUAGE_ORDER:
        prefix = Path() if language == "en" else Path(language)
        for page, content in (("privacy", privacy_page(language)), ("support", support_page(language))):
            destination = ROOT / prefix / PRODUCT / page / "index.html"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_pages()
