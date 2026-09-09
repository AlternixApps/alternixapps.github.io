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
        "support": "Support", "developer": "Developer", "updated": "Updated: September 9, 2026",
        "on_page": "On this page", "official": "Official Alternix website",
        "description": "Privacy Policy for Color Swatch Lab on Android.",
        "sections": [
            ("Overview", "Color Swatch Lab is an Android app by Alternix for working with colours, photos and palettes. No account is required. Colour tools and app content are processed on your device; Alternix has no server that receives them."),
            ("Local data", "The app may store your current colour, history, favourites, palettes and settings, including language, theme and age category, on your device. You can delete history and palettes in the app. Clearing app data or uninstalling removes all local data. Android cloud backup is disabled."),
            ("Camera and photos", "Camera permission is requested only when you open the colour scanner. Photos are chosen through Android Photo Picker, so the app receives only the image you select, not your whole gallery. Images are processed on the device and are not uploaded by Alternix. You can still use manual colour tools if you deny camera access."),
            ("Advertising and consent", "Color Swatch Lab uses Google AdMob for banners and optional rewarded ads. Google and its advertising partners may collect or share IP address, approximate location inferred from IP, device or account identifiers, app and ad interactions, diagnostics and consent choices for advertising, analytics and fraud prevention. Identifiers may include the Android advertising ID and App Set ID; App Set ID is used for analytics and fraud prevention, not ad personalisation or measurement. Google User Messaging Platform (UMP) manages consent where required. Advertising data is encrypted in transit. Alternix does not provide your photos, colours or palette contents to AdMob."),
            ("Age and advertising", "Before any ad request, you choose an age category: 13–17 or 18+. No birth date or exact age is requested. For ages 13–17, personalised advertising is disabled and Google applies teen safeguards and G-rated ad content. For adults, UMP manages available consent choices where required. Color Swatch Lab is not intended for children under 13."),
            ("Export and sharing", "You can save or share palettes in the formats supported by the app. Android lets you choose the save location or receiving app. Temporary share files may remain in the app cache until Android removes them. Alternix does not upload exported files to its own server."),
            ("Third-party services and website", "Google provides AdMob and UMP. This site is hosted by GitHub Pages, which may receive IP addresses and request logs to operate the site. Alternix uses no advertising or analytics scripts on this site. See the privacy policies of <a href=\"https://policies.google.com/privacy\">Google</a> and <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Storage and security", "Local app data remains until you delete it, clear app data or uninstall the app, and is protected by Android app storage. Google and its partners retain advertising data under their own policies. If you contact support, Alternix uses your email address and message to reply and keeps them only as needed for support or legal obligations."),
            ("Your choices and contact", "You can deny or revoke camera access, choose which photos to open, delete history and palettes, decline rewarded ads, and change your age category or available advertising privacy choices. We update this policy when our practices change. Privacy questions: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
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
        "support": "Поддержка", "developer": "Разработчик", "updated": "Обновлено: 9 сентября 2026 года",
        "on_page": "На этой странице", "official": "Официальный сайт Alternix",
        "description": "Политика конфиденциальности Color Swatch Lab для Android.",
        "sections": [
            ("Общие сведения", "Color Swatch Lab — приложение Alternix для работы с цветом, фотографиями и палитрами. Регистрация не нужна. Цветовые инструменты и содержимое приложения обрабатываются на устройстве; у Alternix нет сервера, который получает эти данные."),
            ("Локальные данные", "На устройстве могут сохраняться текущий цвет, история, избранное, палитры и настройки, включая язык, тему и возрастную категорию. Историю и палитры можно удалить в приложении. Очистка данных или удаление приложения стирает все локальные данные. Облачное резервное копирование Android отключено."),
            ("Камера и фотографии", "Разрешение камеры запрашивается только при открытии сканера цвета. Фотографии выбираются через системный Photo Picker Android, поэтому приложение получает только выбранное изображение, а не доступ ко всей галерее. Изображения обрабатываются на устройстве и не загружаются Alternix. При отказе от камеры остаются доступны ручные инструменты цвета."),
            ("Реклама и согласие", "Color Swatch Lab использует Google AdMob для баннеров и необязательной рекламы с вознаграждением. Google и его рекламные партнёры могут собирать или передавать IP-адрес, приблизительное местоположение по IP, идентификаторы устройства или аккаунта, взаимодействия с приложением и рекламой, диагностические сведения и выбор согласия для рекламы, аналитики и предотвращения мошенничества. К идентификаторам могут относиться рекламный ID Android и App Set ID; последний используется для аналитики и защиты от мошенничества, а не для персонализации или измерения рекламы. Google User Messaging Platform (UMP) управляет согласием там, где это требуется. Рекламные данные шифруются при передаче. Alternix не передаёт AdMob ваши фотографии, цвета или содержимое палитр."),
            ("Возраст и реклама", "До первого рекламного запроса вы выбираете категорию 13–17 или 18+. Дата рождения и точный возраст не запрашиваются. Для пользователей 13–17 лет персонализированная реклама отключена, а Google применяет защитные ограничения для подростков и рейтинг рекламы G. Для взрослых UMP предлагает доступные настройки согласия там, где это требуется. Color Swatch Lab не предназначен для детей младше 13 лет."),
            ("Экспорт и отправка", "Палитры можно сохранять и отправлять в форматах, поддерживаемых приложением. Место сохранения или приложение-получатель выбирается через системные средства Android. Временные файлы могут оставаться в кэше до их удаления системой. Alternix не загружает экспортированные файлы на свой сервер."),
            ("Сторонние сервисы и сайт", "Google предоставляет сервисы AdMob и UMP. Сайт размещён на GitHub Pages: GitHub может получать IP-адрес и журналы запросов для работы сайта. Alternix не использует на сайте собственные рекламные или аналитические скрипты. См. политики <a href=\"https://policies.google.com/privacy\">Google</a> и <a href=\"https://docs.github.com/ru/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Хранение и безопасность", "Локальные данные хранятся до их удаления, очистки данных приложения или его удаления и защищены средствами Android. Google и его партнёры хранят рекламные данные по своим правилам. Если вы обращаетесь в поддержку, Alternix использует адрес электронной почты и текст сообщения для ответа и хранит их только столько, сколько нужно для поддержки или выполнения требований закона."),
            ("Ваш выбор и контакты", "Вы можете запретить доступ к камере, выбирать открываемые фотографии, удалять историю и палитры, отказаться от рекламы с вознаграждением, а также изменить возрастную категорию и доступные настройки рекламной конфиденциальности. При изменении способов обработки данных мы обновим эту политику. Вопросы о конфиденциальности: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
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
        "support": "Підтримка", "developer": "Розробник", "updated": "Оновлено: 9 вересня 2026 року",
        "on_page": "На цій сторінці", "official": "Офіційний сайт Alternix",
        "description": "Політика конфіденційності Color Swatch Lab для Android.",
        "sections": [
            ("Загальні відомості", "Color Swatch Lab — застосунок Alternix для роботи з кольором, фотографіями та палітрами. Реєстрація не потрібна. Інструменти кольору й уміст застосунку обробляються на пристрої; Alternix не має сервера, який отримує ці дані."),
            ("Локальні дані", "На пристрої можуть зберігатися поточний колір, історія, вибране, палітри й налаштування, зокрема мова, тема та вікова категорія. Історію й палітри можна видалити в застосунку. Очищення даних або видалення застосунку стирає всі локальні дані. Хмарне резервне копіювання Android вимкнено."),
            ("Камера та фотографії", "Дозвіл камери запитується лише під час відкриття сканера кольору. Фотографії вибираються через системний Photo Picker Android, тому застосунок отримує лише вибране зображення, а не доступ до всієї галереї. Зображення обробляються на пристрої й не завантажуються Alternix. Якщо відмовити в доступі до камери, ручні інструменти кольору залишаються доступними."),
            ("Реклама та згода", "Color Swatch Lab використовує Google AdMob для банерів і необов’язкової реклами з винагородою. Google та його рекламні партнери можуть збирати або передавати IP-адресу, приблизне місцезнаходження за IP, ідентифікатори пристрою чи облікового запису, взаємодії із застосунком і рекламою, діагностичні відомості та вибір згоди для реклами, аналітики й запобігання шахрайству. До ідентифікаторів можуть належати рекламний ID Android і App Set ID; останній використовується для аналітики й захисту від шахрайства, а не для персоналізації чи вимірювання реклами. Google User Messaging Platform (UMP) керує згодою там, де це потрібно. Рекламні дані шифруються під час передавання. Alternix не передає AdMob ваші фотографії, кольори чи вміст палітр."),
            ("Вік і реклама", "До першого рекламного запиту ви вибираєте категорію 13–17 або 18+. Дата народження й точний вік не запитуються. Для користувачів 13–17 років персоналізовану рекламу вимкнено, а Google застосовує захисні обмеження для підлітків і рейтинг реклами G. Для дорослих UMP пропонує доступні налаштування згоди там, де це потрібно. Color Swatch Lab не призначений для дітей до 13 років."),
            ("Експорт і поширення", "Палітри можна зберігати й поширювати у форматах, які підтримує застосунок. Місце збереження або застосунок-отримувач вибирається через системні засоби Android. Тимчасові файли можуть залишатися в кеші, доки система їх не видалить. Alternix не завантажує експортовані файли на свій сервер."),
            ("Сторонні сервіси та сайт", "Google надає сервіси AdMob і UMP. Сайт розміщено на GitHub Pages: GitHub може отримувати IP-адресу й журнали запитів для роботи сайту. Alternix не використовує на сайті власні рекламні чи аналітичні скрипти. Див. політики <a href=\"https://policies.google.com/privacy\">Google</a> і <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Зберігання та безпека", "Локальні дані зберігаються до їх видалення, очищення даних застосунку або його видалення й захищені засобами Android. Google і його партнери зберігають рекламні дані за власними правилами. Якщо ви звертаєтеся до підтримки, Alternix використовує адресу електронної пошти й текст повідомлення для відповіді та зберігає їх лише стільки, скільки потрібно для підтримки або виконання вимог закону."),
            ("Ваш вибір і контакти", "Ви можете заборонити доступ до камери, вибирати фотографії, які відкриватиме застосунок, видаляти історію й палітри, відмовитися від реклами з винагородою, а також змінити вікову категорію та доступні налаштування рекламної конфіденційності. Якщо способи обробки даних зміняться, ми оновимо цю політику. Питання щодо конфіденційності: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
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
        "code": "DE", "skip": "Zum Inhalt springen", "privacy": "Datenschutzerklärung", "support": "Support", "developer": "Entwickler", "updated": "Aktualisiert: 9. September 2026", "on_page": "Auf dieser Seite", "official": "Offizielle Alternix-Website", "description": "Datenschutzerklärung für Color Swatch Lab auf Android.",
        "sections": [
            ("Überblick", "Color Swatch Lab ist eine Android-App von Alternix für Farben, Fotos und Paletten. Kein Konto ist nötig. App-Inhalte werden auf dem Gerät verarbeitet und nicht an Alternix gesendet."),
            ("Lokale Daten", "Farbe, Verlauf, Favoriten, Paletten und Einstellungen einschließlich Sprache, Design und Altersgruppe werden lokal gespeichert. Verlauf und Paletten sind in der App löschbar. Datenbereinigung oder Deinstallation entfernt alles; Cloud-Backups sind deaktiviert."),
            ("Kamera und Fotos", "Die Kamera wird nur für den Farbscanner angefordert. Android Photo Picker öffnet ausschließlich das gewählte Bild. Bilder werden lokal verarbeitet und nicht hochgeladen. Manuelle Farbwerkzeuge funktionieren ohne Kamera."),
            ("Werbung und Einwilligung", "Color Swatch Lab nutzt Google AdMob für Banner und optionale Rewarded Ads. Google und Werbepartner können IP-Adresse, ungefähren Standort aus der IP, Geräte- oder Konto-IDs, App- und Anzeigeninteraktionen, Diagnosedaten und Einwilligungsentscheidungen für Werbung, Analyse und Betrugsprävention erheben oder teilen. Zu den IDs können Android-Werbe-ID und App Set ID gehören; App Set ID dient Analyse und Betrugsprävention, nicht Anzeigenpersonalisierung oder -messung. UMP verwaltet erforderliche Einwilligungen. Werbedaten werden bei der Übertragung verschlüsselt. Alternix übermittelt AdMob keine Fotos, Farben oder Paletteninhalte."),
            ("Alter und Werbung", "Vor Anzeigen wählen Sie 13–17 oder 18+, nicht Ihr Geburtsdatum. Für 13–17 sind personalisierte Anzeigen aus; Google nutzt Jugendschutz und Rating G. Erwachsene erhalten UMP-Optionen, wenn nötig. Die App ist nicht für unter 13-Jährige bestimmt."),
            ("Export und Teilen", "Android lässt Sie Speicherort oder Ziel-App wählen. Temporäre Freigabedateien bleiben eventuell bis zur Systembereinigung im Cache. Alternix lädt Exporte nicht auf einen eigenen Server."),
            ("Drittanbieter und Website", "Google betreibt AdMob und UMP. GitHub Pages hostet diese Website und kann IP-Adressen und Anfrageprotokolle erhalten. Eigene Werbe- oder Analyseskripte gibt es hier nicht. Siehe <a href=\"https://policies.google.com/privacy\">Google</a> und <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Speicherung und Sicherheit", "Lokale Daten bleiben bis zur Löschung, Datenbereinigung oder Deinstallation und sind durch Android geschützt. Google und Partner speichern Werbedaten nach ihren Richtlinien. Support-E-Mails nutzt Alternix nur zur Antwort und solange Support oder Recht es erfordern."),
            ("Ihre Wahl und Kontakt", "Sie können Kamera ablehnen, Fotos auswählen, Verlauf und Paletten löschen, Rewarded Ads ablehnen sowie Altersgruppe und verfügbare Werbeoptionen ändern. Bei Änderungen aktualisieren wir diese Erklärung. Datenschutzfragen: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Hilfe zu Color Swatch Lab, Farbwerkzeugen, Werbung und Export.",
        "support_cards": [("Support kontaktieren", "Schreiben Sie an <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> und nennen Sie App-/Android-Version, Gerät und Reproduktionsschritte."), ("Kamera und Fotos", "Die Kamera ist optional. Fotos werden über den Android Photo Picker gewählt. Prüfen Sie bei Problemen die App-Berechtigung."), ("Werbung und Export", "Geschützte Extraktions- und Exportaktionen benötigen Internet und eine verfügbare Rewarded Ad. Region, Datenschutzwahl und Anzeigenbestand beeinflussen die Verfügbarkeit."), ("Datenschutz", "Die Datenschutzerklärung beschreibt lokale Daten und die Verarbeitung durch Googles Anzeigen-SDK.")],
    },
    "es": {
        "code": "ES", "skip": "Ir al contenido", "privacy": "Política de privacidad", "support": "Soporte", "developer": "Desarrollador", "updated": "Actualizado: 9 de septiembre de 2026", "on_page": "En esta página", "official": "Sitio oficial de Alternix", "description": "Política de privacidad de Color Swatch Lab para Android.",
        "sections": [
            ("Información general", "Color Swatch Lab es una app Android de Alternix para colores, fotos y paletas. No requiere cuenta. El contenido se procesa en el dispositivo y no se envía a Alternix."),
            ("Datos locales", "El color actual, historial, favoritos, paletas y ajustes —idioma, tema y categoría de edad— se guardan localmente. Puedes borrar historial y paletas. Limpiar los datos o desinstalar elimina todo; la copia en la nube está desactivada."),
            ("Cámara y fotos", "La cámara solo se solicita para el escáner. Android Photo Picker abre únicamente la imagen elegida. Las imágenes se procesan localmente y no se suben. Las herramientas manuales funcionan sin cámara."),
            ("Publicidad y consentimiento", "Color Swatch Lab usa Google AdMob para banners y anuncios bonificados opcionales. Google y sus socios pueden recopilar o compartir dirección IP, ubicación aproximada derivada de la IP, identificadores, interacciones, diagnósticos y elecciones de consentimiento para publicidad, análisis y prevención del fraude. Los identificadores pueden incluir el ID publicitario de Android y App Set ID; este último se usa para análisis y prevención del fraude, no para personalizar o medir anuncios. UMP gestiona el consentimiento cuando se exige. Los datos publicitarios se cifran al transmitirse. Alternix no proporciona a AdMob fotos, colores ni contenido de paletas."),
            ("Edad y publicidad", "Antes de los anuncios eliges 13–17 o 18+, no tu fecha de nacimiento. Para 13–17 se desactiva la personalización y Google aplica protección para adolescentes y clasificación G. Los adultos reciben opciones UMP cuando corresponde. La app no es para menores de 13."),
            ("Exportación y uso compartido", "Android permite elegir dónde guardar una paleta o con qué app compartirla. Los archivos temporales pueden quedar en la caché hasta que el sistema los elimine. Alternix no sube las exportaciones a un servidor propio."),
            ("Servicios externos y sitio web", "Google presta AdMob y UMP. GitHub Pages aloja este sitio y puede recibir IP y registros de solicitudes. No usamos scripts propios de publicidad o análisis. Consulta <a href=\"https://policies.google.com/privacy\">Google</a> y <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Almacenamiento y seguridad", "Los datos locales permanecen hasta que los borras, limpias la app o la desinstalas y están protegidos por Android. Google y sus socios conservan datos publicitarios según sus políticas. Alternix usa los correos de soporte solo para responder y mientras lo exijan el soporte o la ley."),
            ("Tus opciones y contacto", "Puedes denegar la cámara, elegir fotos, borrar historial y paletas, rechazar anuncios bonificados y cambiar la edad o las opciones publicitarias disponibles. Actualizaremos esta política si cambian nuestras prácticas. Privacidad: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Ayuda sobre Color Swatch Lab, herramientas de color, anuncios y exportación.",
        "support_cards": [("Contactar", "Escribe a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> con versión de app/Android, modelo y pasos."), ("Cámara y fotos", "La cámara es opcional; las fotos usan Android Photo Picker. Revisa el permiso si no abre."), ("Anuncios y exportación", "Las acciones protegidas necesitan conexión y un anuncio bonificado disponible; región, privacidad e inventario influyen."), ("Privacidad", "La política explica qué queda en el dispositivo y qué puede procesar el SDK de Google.")],
    },
    "fr": {
        "code": "FR", "skip": "Aller au contenu", "privacy": "Politique de confidentialité", "support": "Assistance", "developer": "Développeur", "updated": "Mise à jour : 9 septembre 2026", "on_page": "Sur cette page", "official": "Site officiel d’Alternix", "description": "Politique de confidentialité de Color Swatch Lab pour Android.",
        "sections": [
            ("Présentation", "Color Swatch Lab est une app Android d’Alternix pour les couleurs, photos et palettes. Aucun compte n’est requis. Le contenu est traité sur l’appareil et n’est pas envoyé à Alternix."),
            ("Données locales", "Couleur actuelle, historique, favoris, palettes et réglages — langue, thème et catégorie d’âge — sont stockés localement. Vous pouvez supprimer historique et palettes. Effacer les données ou désinstaller supprime tout ; la sauvegarde cloud est désactivée."),
            ("Caméra et photos", "La caméra n’est demandée que pour le scanner. Android Photo Picker ouvre uniquement l’image choisie. Les images sont traitées localement, sans téléversement. Les outils manuels fonctionnent sans caméra."),
            ("Publicité et consentement", "Color Swatch Lab utilise Google AdMob pour des bannières et des publicités récompensées facultatives. Google et ses partenaires peuvent collecter ou partager adresse IP, localisation approximative issue de l’IP, identifiants, interactions, diagnostics et choix de consentement pour publicité, analyse et prévention de la fraude. Les identifiants peuvent inclure l’identifiant publicitaire Android et App Set ID ; ce dernier sert à l’analyse et à la prévention de la fraude, pas à personnaliser ou mesurer les annonces. UMP gère le consentement lorsque nécessaire. Les données publicitaires sont chiffrées pendant le transfert. Alternix ne fournit pas à AdMob photos, couleurs ou palettes."),
            ("Âge et publicité", "Avant les annonces, vous choisissez 13–17 ou 18+, pas votre date de naissance. Pour 13–17, la personnalisation est désactivée et Google applique les protections adolescents et la catégorie G. Les adultes reçoivent les options UMP si nécessaire. L’app n’est pas destinée aux moins de 13 ans."),
            ("Export et partage", "Android permet de choisir où enregistrer une palette ou avec quelle app la partager. Les fichiers temporaires peuvent rester en cache jusqu’à leur suppression par le système. Alternix ne téléverse pas les exports sur son serveur."),
            ("Services tiers et site", "Google fournit AdMob et UMP. GitHub Pages héberge ce site et peut recevoir IP et journaux de requêtes. Nous n’utilisons aucun script publicitaire ou analytique propre. Voir <a href=\"https://policies.google.com/privacy\">Google</a> et <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Stockage et sécurité", "Les données locales restent jusqu’à leur suppression, l’effacement de l’app ou sa désinstallation et sont protégées par Android. Google et ses partenaires conservent les données publicitaires selon leurs politiques. Alternix utilise les e-mails d’assistance uniquement pour répondre et tant que l’assistance ou la loi l’exige."),
            ("Vos choix et contact", "Vous pouvez refuser la caméra, choisir les photos, supprimer historique et palettes, refuser les annonces récompensées et modifier l’âge ou les options publicitaires disponibles. Nous actualiserons cette politique si nos pratiques changent. Confidentialité : <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Assistance pour Color Swatch Lab, les outils couleur, la publicité et l’export.",
        "support_cards": [("Contacter l’assistance", "Écrivez à <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> avec versions, modèle et étapes."), ("Caméra et photos", "La caméra est facultative ; les photos utilisent Android Photo Picker. Vérifiez l’autorisation si nécessaire."), ("Publicité et export", "Les actions protégées nécessitent Internet et une publicité récompensée disponible ; région, confidentialité et inventaire influencent la disponibilité."), ("Confidentialité", "La politique décrit les données locales et le traitement possible par le SDK Google.")],
    },
    "it": {
        "code": "IT", "skip": "Vai al contenuto", "privacy": "Informativa sulla privacy", "support": "Supporto", "developer": "Sviluppatore", "updated": "Aggiornata: 9 settembre 2026", "on_page": "In questa pagina", "official": "Sito ufficiale Alternix", "description": "Informativa sulla privacy di Color Swatch Lab per Android.",
        "sections": [
            ("Panoramica", "Color Swatch Lab è un’app Android di Alternix per colori, foto e tavolozze. Non richiede account. I contenuti sono elaborati sul dispositivo e non inviati ad Alternix."),
            ("Dati locali", "Colore, cronologia, preferiti, tavolozze e impostazioni — lingua, tema ed età — sono salvati localmente. Cronologia e tavolozze sono eliminabili. Cancellare i dati o disinstallare rimuove tutto; il backup cloud è disattivato."),
            ("Fotocamera e foto", "La fotocamera è richiesta solo per lo scanner. Android Photo Picker apre soltanto l’immagine scelta. Le immagini sono elaborate localmente, senza caricamento. Gli strumenti manuali funzionano senza fotocamera."),
            ("Pubblicità e consenso", "Color Swatch Lab usa Google AdMob per banner e annunci con premio facoltativi. Google e i partner possono raccogliere o condividere indirizzo IP, posizione approssimativa dall’IP, identificatori, interazioni, diagnostica e scelte di consenso per pubblicità, analisi e prevenzione frodi. Gli identificatori possono includere l’ID pubblicitario Android e App Set ID; quest’ultimo serve per analisi e prevenzione frodi, non per personalizzare o misurare annunci. UMP gestisce il consenso dove richiesto. I dati pubblicitari sono cifrati durante il trasferimento. Alternix non fornisce ad AdMob foto, colori o tavolozze."),
            ("Età e pubblicità", "Prima degli annunci scegli 13–17 o 18+, non la data di nascita. Per 13–17 la personalizzazione è disattivata e Google applica protezioni adolescenti e categoria G. Gli adulti ricevono opzioni UMP se necessarie. L’app non è destinata ai minori di 13."),
            ("Esportazione e condivisione", "Android permette di scegliere dove salvare una tavolozza o con quale app condividerla. I file temporanei possono restare nella cache fino alla pulizia del sistema. Alternix non carica gli export su un proprio server."),
            ("Servizi esterni e sito", "Google fornisce AdMob e UMP. GitHub Pages ospita il sito e può ricevere IP e registri delle richieste. Non usiamo script propri per pubblicità o analisi. Vedi <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Conservazione e sicurezza", "I dati locali restano fino all’eliminazione, alla pulizia dell’app o alla disinstallazione e sono protetti da Android. Google e partner conservano dati pubblicitari secondo le loro politiche. Alternix usa le e-mail di assistenza solo per rispondere e finché assistenza o legge lo richiedono."),
            ("Scelte e contatto", "Puoi negare la fotocamera, scegliere foto, eliminare cronologia e tavolozze, rifiutare annunci con premio e cambiare età o opzioni pubblicitarie disponibili. Aggiorneremo l’informativa se cambiano le pratiche. Privacy: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Assistenza per Color Swatch Lab, strumenti colore, annunci ed esportazione.",
        "support_cards": [("Contatta il supporto", "Scrivi a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> indicando versioni, modello e passaggi."), ("Fotocamera e foto", "La fotocamera è facoltativa; le foto usano Android Photo Picker. Controlla il permesso se non si apre."), ("Annunci ed esportazione", "Le azioni protette richiedono Internet e un annuncio con premio disponibile; regione, privacy e inventario incidono."), ("Privacy", "L’informativa descrive dati locali e trattamento possibile da parte dell’SDK Google.")],
    },
    "pl": {
        "code": "PL", "skip": "Przejdź do treści", "privacy": "Polityka prywatności", "support": "Pomoc", "developer": "Deweloper", "updated": "Aktualizacja: 9 września 2026", "on_page": "Na tej stronie", "official": "Oficjalna strona Alternix", "description": "Polityka prywatności Color Swatch Lab na Androida.",
        "sections": [
            ("Informacje ogólne", "Color Swatch Lab to aplikacja Alternix na Androida do kolorów, zdjęć i palet. Nie wymaga konta. Treści są przetwarzane na urządzeniu i nie trafiają do Alternix."),
            ("Dane lokalne", "Kolor, historia, ulubione, palety i ustawienia — język, motyw i wiek — są przechowywane lokalnie. Historię i palety można usunąć. Wyczyszczenie danych lub odinstalowanie usuwa wszystko; kopia w chmurze jest wyłączona."),
            ("Aparat i zdjęcia", "Aparat jest wymagany tylko dla skanera. Android Photo Picker otwiera wyłącznie wybrany obraz. Zdjęcia są przetwarzane lokalnie, bez przesyłania. Narzędzia ręczne działają bez aparatu."),
            ("Reklamy i zgoda", "Color Swatch Lab używa Google AdMob do banerów i opcjonalnych reklam z nagrodą. Google i partnerzy mogą zbierać lub udostępniać adres IP, przybliżoną lokalizację z IP, identyfikatory, interakcje, diagnostykę i wybory zgody do reklam, analityki i zapobiegania oszustwom. Identyfikatory mogą obejmować Android advertising ID i App Set ID; ten drugi służy analityce i zapobieganiu oszustwom, nie personalizacji ani pomiarowi reklam. UMP zarządza zgodą, gdy jest wymagana. Dane reklamowe są szyfrowane podczas przesyłania. Alternix nie przekazuje AdMob zdjęć, kolorów ani palet."),
            ("Wiek i reklamy", "Przed reklamami wybierasz 13–17 lub 18+, nie datę urodzenia. Dla 13–17 personalizacja jest wyłączona, a Google stosuje ochronę nastolatków i kategorię G. Dorośli otrzymują opcje UMP, gdy są wymagane. Aplikacja nie jest dla dzieci poniżej 13 lat."),
            ("Eksport i udostępnianie", "Android pozwala wybrać miejsce zapisu palety lub aplikację do udostępniania. Pliki tymczasowe mogą pozostać w pamięci podręcznej do usunięcia przez system. Alternix nie przesyła eksportów na własny serwer."),
            ("Usługi zewnętrzne i witryna", "Google dostarcza AdMob i UMP. GitHub Pages hostuje witrynę i może otrzymywać IP oraz dzienniki żądań. Nie używamy własnych skryptów reklamowych ani analitycznych. Zobacz <a href=\"https://policies.google.com/privacy\">Google</a> i <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Przechowywanie i bezpieczeństwo", "Dane lokalne pozostają do usunięcia, wyczyszczenia aplikacji lub odinstalowania i są chronione przez Androida. Google i partnerzy przechowują dane reklamowe według swoich zasad. Alternix używa e-maili do pomocy tylko w celu odpowiedzi i tak długo, jak wymaga pomoc lub prawo."),
            ("Wybory i kontakt", "Możesz odmówić aparatu, wybierać zdjęcia, usuwać historię i palety, odrzucać reklamy z nagrodą oraz zmieniać wiek lub dostępne opcje reklamowe. Zaktualizujemy politykę, jeśli zmienią się praktyki. Prywatność: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
        ],
        "support_intro": "Pomoc dotycząca Color Swatch Lab, narzędzi kolorów, reklam i eksportu.",
        "support_cards": [("Kontakt z pomocą", "Napisz na <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>, podając wersje, model i kroki."), ("Aparat i zdjęcia", "Aparat jest opcjonalny; zdjęcia używają Android Photo Picker. Sprawdź uprawnienie, jeśli aparat się nie otwiera."), ("Reklamy i eksport", "Chronione działania wymagają Internetu i dostępnej reklamy z nagrodą; wpływają region, prywatność i zasoby reklam."), ("Prywatność", "Polityka opisuje dane lokalne i możliwe przetwarzanie przez SDK Google.")],
    },
    "pt": {
        "code": "PT", "skip": "Ir para o conteúdo", "privacy": "Política de privacidade", "support": "Suporte", "developer": "Programador", "updated": "Atualizada: 9 de setembro de 2026", "on_page": "Nesta página", "official": "Site oficial da Alternix", "description": "Política de privacidade do Color Swatch Lab para Android.",
        "sections": [
            ("Visão geral", "Color Swatch Lab é uma aplicação Android da Alternix para cores, fotos e paletas. Não exige conta. O conteúdo é processado no dispositivo e não é enviado à Alternix."),
            ("Dados locais", "Cor, histórico, favoritos, paletas e definições — idioma, tema e idade — são guardados localmente. Pode apagar histórico e paletas. Limpar os dados ou desinstalar remove tudo; a cópia na nuvem está desativada."),
            ("Câmara e fotos", "A câmara só é pedida para o scanner. O Android Photo Picker abre apenas a imagem escolhida. As imagens são processadas localmente, sem carregamento. As ferramentas manuais funcionam sem câmara."),
            ("Publicidade e consentimento", "Color Swatch Lab usa Google AdMob para banners e anúncios premiados opcionais. Google e parceiros podem recolher ou partilhar endereço IP, localização aproximada pelo IP, identificadores, interações, diagnósticos e escolhas de consentimento para publicidade, análise e prevenção de fraude. Os identificadores podem incluir o ID de publicidade Android e App Set ID; este serve para análise e prevenção de fraude, não para personalizar ou medir anúncios. A UMP gere o consentimento quando necessário. Os dados publicitários são encriptados em trânsito. A Alternix não fornece ao AdMob fotos, cores ou paletas."),
            ("Idade e publicidade", "Antes dos anúncios escolhe 13–17 ou 18+, não a data de nascimento. Para 13–17 a personalização é desativada e a Google aplica proteção para adolescentes e classificação G. Adultos recebem opções UMP quando necessário. A aplicação não é para menores de 13."),
            ("Exportação e partilha", "O Android permite escolher onde guardar uma paleta ou com que aplicação a partilhar. Ficheiros temporários podem ficar na cache até à limpeza do sistema. A Alternix não envia exportações para um servidor próprio."),
            ("Serviços externos e site", "A Google fornece AdMob e UMP. O GitHub Pages aloja o site e pode receber IP e registos de pedidos. Não usamos scripts próprios de publicidade ou análise. Consulte <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Armazenamento e segurança", "Os dados locais ficam até serem apagados, a aplicação ser limpa ou desinstalada e são protegidos pelo Android. Google e parceiros guardam dados publicitários segundo as suas políticas. A Alternix usa e-mails de suporte apenas para responder e enquanto o suporte ou a lei exigir."),
            ("Escolhas e contacto", "Pode negar a câmara, escolher fotos, apagar histórico e paletas, recusar anúncios premiados e mudar a idade ou opções publicitárias disponíveis. Atualizaremos a política se as práticas mudarem. Privacidade: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>."),
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
            with destination.open("w", encoding="utf-8", newline="\n") as output:
                output.write(content + "\n")


if __name__ == "__main__":
    write_pages()
