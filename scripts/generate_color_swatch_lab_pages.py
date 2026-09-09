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
        "support": "Support", "developer": "Developer", "updated": "Last updated: September 9, 2026",
        "on_page": "On this page", "official": "Official Alternix website",
        "description": "Privacy Policy for Color Swatch Lab on Android.",
        "sections": [
            ("About the app", "Color Swatch Lab is an Alternix app for working with colours and palettes. No account is required."),
            ("Your data", "Colours, history, favourites, palettes and settings, including your age category, stay on your device. Alternix does not receive them. You can delete history and palettes in the app; clearing app data or uninstalling removes its remaining internal data. Cloud backup is disabled."),
            ("Camera and photos", "Camera access is requested only for colour scanning and is optional. You choose photos through Android’s system window; the app cannot browse your whole gallery. Images are processed on your device and are not sent to Alternix."),
            ("Advertising", "Google AdMob provides banners and optional rewarded ads. Google and its partners may collect and share your IP address and approximate location inferred from it, device and account identifiers (including the advertising ID), app and ad activity, performance and error reports and consent choices. These support advertising, analytics and fraud prevention. App Set ID is used only for analytics and fraud prevention. Photos, colours and palettes are not shared with advertisers."),
            ("Age and consent", "The app is intended for ages 13 and over. Before ads, you choose 13–17 or 18+, without providing your birth date. Teen ads are not personalised and have additional content restrictions. For adults, Google requests consent where required."),
            ("Saving and sharing", "You choose where to save palettes or which app receives them. Sharing creates temporary files inside the app. Files saved elsewhere or already sent remain with you or the recipient after uninstallation."),
            ("This website", "GitHub Pages hosts the site and may receive IP addresses and visit records. There is no advertising or analytics on the site. Your browser remembers language and theme until you clear site data. See <a href=\"https://policies.google.com/privacy\">Google</a>’s and <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>’s privacy policies."),
            ("Security and retention", "Android protects internal app data; advertising data is encrypted during transfer. Google and its partners, and GitHub, retain and delete data according to their own policies."),
            ("Your choices and contact", "You can change your age category and available advertising consent choices in settings. Privacy enquiries: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix uses your email and message to reply, keeping them only as needed for support or legal obligations. This policy is updated when data practices change."),
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
        "support": "Поддержка", "developer": "Разработчик", "updated": "Последнее обновление: 9 сентября 2026 года",
        "on_page": "На этой странице", "official": "Официальный сайт Alternix",
        "description": "Политика конфиденциальности Color Swatch Lab для Android.",
        "sections": [
            ("О приложении", "Color Swatch Lab — приложение Alternix для работы с цветом и палитрами. Регистрация не требуется."),
            ("Ваши данные", "Цвета, история, избранное, палитры и настройки, включая возрастную категорию, хранятся только на устройстве. Alternix их не получает. Историю и палитры можно удалить в приложении; остальные внутренние данные — очистив данные приложения или удалив его. Облачное резервное копирование отключено."),
            ("Камера и фотографии", "Камера запрашивается только для сканирования цвета, и в доступе можно отказать. Фотографию вы выбираете в системном окне Android; доступа ко всей галерее нет. Изображения обрабатываются на устройстве и не отправляются Alternix."),
            ("Реклама", "Google AdMob показывает баннеры и необязательную рекламу с вознаграждением. Google и партнёры могут собирать и передавать IP-адрес и примерное местоположение по нему, идентификаторы устройства и аккаунта (включая рекламный), сведения об использовании и работе приложения, взаимодействии с рекламой и выборе согласия. Это нужно для рекламы, статистики и защиты от мошенничества. Идентификатор приложений App Set ID используется только для статистики и защиты от мошенничества. Фотографии, цвета и палитры рекламодателям не передаются."),
            ("Возраст и согласие", "Приложение предназначено для пользователей от 13 лет. До показа рекламы вы выбираете 13–17 или 18+, без указания даты рождения. Для подростков реклама неперсонализированная, с дополнительными ограничениями содержания. У взрослых Google запрашивает согласие там, где это требуется."),
            ("Сохранение и отправка", "Вы выбираете, куда сохранить палитру или какому приложению её отправить. Для отправки создаются временные файлы внутри приложения. Сохранённые отдельно или уже отправленные файлы остаются у вас или получателя после удаления приложения."),
            ("Этот сайт", "Сайт размещён на GitHub Pages: GitHub может получать IP-адрес и сведения о посещениях. На сайте нет рекламы и аналитики. Браузер запоминает язык и тему до очистки данных сайта. Политики конфиденциальности: <a href=\"https://policies.google.com/privacy\">Google</a> и <a href=\"https://docs.github.com/ru/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Защита и сроки хранения", "Внутренние данные приложения защищены средствами Android; рекламные данные шифруются при передаче. Google и его партнёры, а также GitHub хранят и удаляют данные по своим правилам."),
            ("Ваш выбор и контакты", "В настройках можно изменить возрастную категорию и доступные настройки рекламного согласия. Вопросы о конфиденциальности: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix использует вашу почту и сообщение для ответа и хранит их только столько, сколько нужно для поддержки или по закону. При изменении работы с данными мы обновим политику."),
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
        "support": "Підтримка", "developer": "Розробник", "updated": "Останнє оновлення: 9 вересня 2026 року",
        "on_page": "На цій сторінці", "official": "Офіційний сайт Alternix",
        "description": "Політика конфіденційності Color Swatch Lab для Android.",
        "sections": [
            ("Про застосунок", "Color Swatch Lab — застосунок Alternix для роботи з кольором і палітрами. Реєстрація не потрібна."),
            ("Ваші дані", "Кольори, історія, вибране, палітри й налаштування, зокрема вікова категорія, зберігаються лише на пристрої. Alternix їх не отримує. Історію й палітри можна видалити в застосунку; решту внутрішніх даних — очистивши дані застосунку або видаливши його. Хмарне резервне копіювання вимкнено."),
            ("Камера та фотографії", "Доступ до камери запитується лише для сканування кольору, і від нього можна відмовитися. Фотографію ви вибираєте в системному вікні Android; доступу до всієї галереї немає. Зображення обробляються на пристрої й не надсилаються Alternix."),
            ("Реклама", "Google AdMob показує банери й необов’язкову рекламу з винагородою. Google та партнери можуть збирати й передавати IP-адресу та приблизне місцезнаходження за нею, ідентифікатори пристрою й облікового запису (зокрема рекламний), відомості про використання й роботу застосунку, взаємодію з рекламою та вибір згоди. Це потрібно для реклами, статистики й захисту від шахрайства. Ідентифікатор застосунків App Set ID використовується лише для статистики й захисту від шахрайства. Фотографії, кольори й палітри рекламодавцям не передаються."),
            ("Вік і згода", "Застосунок призначений для користувачів від 13 років. До показу реклами ви вибираєте 13–17 або 18+, без дати народження. Для підлітків реклама неперсоналізована, з додатковими обмеженнями вмісту. У дорослих Google запитує згоду там, де це потрібно."),
            ("Збереження й надсилання", "Ви вибираєте, куди зберегти палітру або якому застосунку її надіслати. Для надсилання створюються тимчасові файли всередині застосунку. Збережені окремо або вже надіслані файли залишаються у вас чи отримувача після видалення застосунку."),
            ("Цей сайт", "Сайт розміщено на GitHub Pages: GitHub може отримувати IP-адресу й відомості про відвідування. На сайті немає реклами й аналітики. Браузер запам’ятовує мову й тему до очищення даних сайту. Політики конфіденційності: <a href=\"https://policies.google.com/privacy\">Google</a> і <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Захист і строки зберігання", "Внутрішні дані застосунку захищені засобами Android; рекламні дані шифруються під час передавання. Google та його партнери, а також GitHub зберігають і видаляють дані за власними правилами."),
            ("Ваш вибір і контакти", "У налаштуваннях можна змінити вікову категорію й доступні налаштування рекламної згоди. Питання конфіденційності: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix використовує вашу пошту й повідомлення для відповіді та зберігає їх лише стільки, скільки потрібно для підтримки або за законом. Якщо робота з даними зміниться, ми оновимо політику."),
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
        "code": "DE", "skip": "Zum Inhalt springen", "privacy": "Datenschutzerklärung", "support": "Support", "developer": "Entwickler", "updated": "Zuletzt aktualisiert: 9. September 2026", "on_page": "Auf dieser Seite", "official": "Offizielle Alternix-Website", "description": "Datenschutzerklärung für Color Swatch Lab auf Android.",
        "sections": [
            ("Über die App", "Color Swatch Lab ist eine App von Alternix für Farben und Paletten. Ein Konto ist nicht nötig."),
            ("Ihre Daten", "Farben, Verlauf, Favoriten, Paletten und Einstellungen einschließlich Altersgruppe bleiben auf Ihrem Gerät. Alternix erhält sie nicht. Verlauf und Paletten können Sie in der App löschen; das Löschen der App-Daten oder die Deinstallation entfernt die übrigen internen Daten. Cloud-Backups sind deaktiviert."),
            ("Kamera und Fotos", "Der Kamerazugriff wird nur zum Scannen von Farben angefragt und ist freiwillig. Fotos wählen Sie im Android-Systemfenster aus; die App kann nicht auf die gesamte Galerie zugreifen. Bilder werden auf dem Gerät verarbeitet und nicht an Alternix gesendet."),
            ("Werbung", "Google AdMob zeigt Banner und freiwillige Anzeigen mit Belohnung. Google und Partner können IP-Adresse und daraus abgeleiteten ungefähren Standort, Geräte- und Konto-IDs (einschließlich Werbe-ID), App- und Anzeigenaktivität, Leistungs- und Fehlerberichte sowie Einwilligungsentscheidungen erfassen und weitergeben. Dies dient Werbung, Statistik und Betrugsprävention. App Set ID dient ausschließlich Statistik und Betrugsprävention. Fotos, Farben und Paletten werden nicht an Werbetreibende weitergegeben."),
            ("Alter und Einwilligung", "Die App richtet sich an Personen ab 13 Jahren. Vor der Werbung wählen Sie 13–17 oder 18+, ohne Geburtsdatum. Für Jugendliche sind Anzeigen nicht personalisiert und inhaltlich zusätzlich eingeschränkt. Bei Erwachsenen fragt Google die Einwilligung ab, wo erforderlich."),
            ("Speichern und Teilen", "Sie wählen den Speicherort oder die Empfänger-App für Paletten. Beim Teilen entstehen temporäre Dateien innerhalb der App. Anderswo gespeicherte oder bereits versendete Dateien bleiben nach der Deinstallation bei Ihnen oder beim Empfänger."),
            ("Diese Website", "GitHub Pages stellt die Website bereit und kann IP-Adressen und Besuchsdaten erhalten. Die Website enthält keine Werbung oder Analysefunktionen. Ihr Browser merkt sich Sprache und Design, bis Sie die Websitedaten löschen. Datenschutzhinweise: <a href=\"https://policies.google.com/privacy\">Google</a> und <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Schutz und Aufbewahrung", "Android schützt interne App-Daten; Werbedaten werden bei der Übertragung verschlüsselt. Google und seine Partner sowie GitHub speichern und löschen Daten nach ihren eigenen Richtlinien."),
            ("Ihre Wahl und Kontakt", "Altersgruppe und verfügbare Werbeeinwilligungen können Sie in den Einstellungen ändern. Datenschutzfragen: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix nutzt Ihre E-Mail-Adresse und Nachricht zur Antwort und bewahrt sie nur auf, solange Support oder Gesetz es erfordern. Bei Änderungen der Datenverarbeitung aktualisieren wir diese Erklärung."),
        ],
        "support_intro": "Hilfe zu Color Swatch Lab, Farbwerkzeugen, Werbung und Export.",
        "support_cards": [("Support kontaktieren", "Schreiben Sie an <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> und nennen Sie App-/Android-Version, Gerät und Reproduktionsschritte."), ("Kamera und Fotos", "Die Kamera ist optional. Fotos werden über den Android Photo Picker gewählt. Prüfen Sie bei Problemen die App-Berechtigung."), ("Werbung und Export", "Geschützte Extraktions- und Exportaktionen benötigen Internet und eine verfügbare Rewarded Ad. Region, Datenschutzwahl und Anzeigenbestand beeinflussen die Verfügbarkeit."), ("Datenschutz", "Die Datenschutzerklärung beschreibt lokale Daten und die Verarbeitung durch Googles Anzeigen-SDK.")],
    },
    "es": {
        "code": "ES", "skip": "Ir al contenido", "privacy": "Política de privacidad", "support": "Soporte", "developer": "Desarrollador", "updated": "Última actualización: 9 de septiembre de 2026", "on_page": "En esta página", "official": "Sitio oficial de Alternix", "description": "Política de privacidad de Color Swatch Lab para Android.",
        "sections": [
            ("Sobre la app", "Color Swatch Lab es una app de Alternix para trabajar con colores y paletas. No requiere una cuenta."),
            ("Tus datos", "Colores, historial, favoritos, paletas y ajustes, incluida la categoría de edad, permanecen en tu dispositivo. Alternix no los recibe. Puedes borrar el historial y las paletas en la app; borrar sus datos o desinstalarla elimina los demás datos internos. La copia en la nube está desactivada."),
            ("Cámara y fotos", "El acceso a la cámara solo se solicita para escanear colores y es opcional. Eliges las fotos en la ventana del sistema Android; la app no accede a toda la galería. Las imágenes se procesan en el dispositivo y no se envían a Alternix."),
            ("Publicidad", "Google AdMob muestra banners y anuncios opcionales con recompensa. Google y sus socios pueden recopilar y compartir IP y ubicación aproximada derivada de ella, identificadores del dispositivo y de la cuenta (incluido el publicitario), actividad en la app y los anuncios, informes de rendimiento y errores y elecciones de consentimiento. Se usan para publicidad, estadísticas y prevención del fraude. App Set ID se usa solo para estadísticas y prevención del fraude. No se comparten fotos, colores ni paletas con anunciantes."),
            ("Edad y consentimiento", "La app está destinada a personas de 13 años o más. Antes de los anuncios eliges 13–17 o 18+, sin dar tu fecha de nacimiento. Para adolescentes, los anuncios no se personalizan y tienen restricciones adicionales de contenido. Google solicita consentimiento a los adultos cuando corresponde."),
            ("Guardar y compartir", "Eliges dónde guardar las paletas o qué app las recibe. Compartir crea archivos temporales dentro de la app. Los archivos guardados fuera o ya enviados permanecen contigo o con el destinatario tras desinstalarla."),
            ("Este sitio web", "GitHub Pages aloja el sitio y puede recibir direcciones IP y registros de visitas. No hay publicidad ni analítica en el sitio. El navegador recuerda idioma y tema hasta que borras los datos del sitio. Políticas de privacidad: <a href=\"https://policies.google.com/privacy\">Google</a> y <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Protección y conservación", "Android protege los datos internos de la app; los publicitarios se cifran al transmitirse. Google y sus socios, así como GitHub, conservan y eliminan datos según sus propias políticas."),
            ("Tus opciones y contacto", "Puedes cambiar la categoría de edad y las opciones disponibles de consentimiento publicitario en los ajustes. Consultas de privacidad: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix usa tu correo y mensaje para responder y los conserva solo mientras sean necesarios para el soporte o por ley. Actualizaremos esta política si cambia el tratamiento de datos."),
        ],
        "support_intro": "Ayuda sobre Color Swatch Lab, herramientas de color, anuncios y exportación.",
        "support_cards": [("Contactar", "Escribe a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> con versión de app/Android, modelo y pasos."), ("Cámara y fotos", "La cámara es opcional; las fotos usan Android Photo Picker. Revisa el permiso si no abre."), ("Anuncios y exportación", "Las acciones protegidas necesitan conexión y un anuncio bonificado disponible; región, privacidad e inventario influyen."), ("Privacidad", "La política explica qué queda en el dispositivo y qué puede procesar el SDK de Google.")],
    },
    "fr": {
        "code": "FR", "skip": "Aller au contenu", "privacy": "Politique de confidentialité", "support": "Assistance", "developer": "Développeur", "updated": "Dernière mise à jour : 9 septembre 2026", "on_page": "Sur cette page", "official": "Site officiel d’Alternix", "description": "Politique de confidentialité de Color Swatch Lab pour Android.",
        "sections": [
            ("À propos de l’app", "Color Swatch Lab est une app d’Alternix pour travailler avec les couleurs et les palettes. Aucun compte n’est nécessaire."),
            ("Vos données", "Couleurs, historique, favoris, palettes et réglages, dont la catégorie d’âge, restent sur votre appareil. Alternix ne les reçoit pas. Vous pouvez supprimer l’historique et les palettes dans l’app ; effacer ses données ou la désinstaller supprime les autres données internes. La sauvegarde cloud est désactivée."),
            ("Caméra et photos", "L’accès à la caméra est demandé uniquement pour scanner une couleur et reste facultatif. Vous choisissez les photos dans la fenêtre système Android ; l’app n’accède pas à toute la galerie. Les images sont traitées sur l’appareil et ne sont pas envoyées à Alternix."),
            ("Publicité", "Google AdMob affiche des bannières et des annonces récompensées facultatives. Google et ses partenaires peuvent recueillir et partager l’adresse IP et la localisation approximative qui en découle, les identifiants d’appareil et de compte (dont l’identifiant publicitaire), l’activité dans l’app et les annonces, les rapports de performance et d’erreurs et les choix de consentement. Cela sert à la publicité, aux statistiques et à la prévention des fraudes. App Set ID sert uniquement aux statistiques et à la prévention des fraudes. Photos, couleurs et palettes ne sont pas transmises aux annonceurs."),
            ("Âge et consentement", "L’app est destinée aux personnes de 13 ans et plus. Avant les annonces, vous choisissez 13–17 ou 18+, sans date de naissance. Pour les adolescents, les annonces ne sont pas personnalisées et leur contenu est davantage restreint. Google demande le consentement des adultes lorsque nécessaire."),
            ("Enregistrer et partager", "Vous choisissez où enregistrer les palettes ou quelle app les reçoit. Le partage crée des fichiers temporaires dans l’app. Les fichiers enregistrés ailleurs ou déjà envoyés restent chez vous ou chez le destinataire après la désinstallation."),
            ("Ce site", "GitHub Pages héberge le site et peut recevoir des adresses IP et des données de visite. Le site ne contient ni publicité ni outil d’analyse. Le navigateur mémorise langue et thème jusqu’à l’effacement des données du site. Politiques de confidentialité : <a href=\"https://policies.google.com/privacy\">Google</a> et <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Protection et conservation", "Android protège les données internes de l’app ; les données publicitaires sont chiffrées pendant le transfert. Google et ses partenaires, ainsi que GitHub, conservent et suppriment les données selon leurs propres politiques."),
            ("Vos choix et contact", "Vous pouvez modifier la catégorie d’âge et les choix de consentement publicitaire disponibles dans les réglages. Questions de confidentialité : <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix utilise votre adresse e-mail et votre message pour répondre et les conserve uniquement selon les besoins de l’assistance ou de la loi. Cette politique évoluera si nos pratiques changent."),
        ],
        "support_intro": "Assistance pour Color Swatch Lab, les outils couleur, la publicité et l’export.",
        "support_cards": [("Contacter l’assistance", "Écrivez à <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> avec versions, modèle et étapes."), ("Caméra et photos", "La caméra est facultative ; les photos utilisent Android Photo Picker. Vérifiez l’autorisation si nécessaire."), ("Publicité et export", "Les actions protégées nécessitent Internet et une publicité récompensée disponible ; région, confidentialité et inventaire influencent la disponibilité."), ("Confidentialité", "La politique décrit les données locales et le traitement possible par le SDK Google.")],
    },
    "it": {
        "code": "IT", "skip": "Vai al contenuto", "privacy": "Informativa sulla privacy", "support": "Supporto", "developer": "Sviluppatore", "updated": "Ultimo aggiornamento: 9 settembre 2026", "on_page": "In questa pagina", "official": "Sito ufficiale Alternix", "description": "Informativa sulla privacy di Color Swatch Lab per Android.",
        "sections": [
            ("L’app", "Color Swatch Lab è un’app di Alternix per colori e tavolozze. Non richiede un account."),
            ("I tuoi dati", "Colori, cronologia, preferiti, tavolozze e impostazioni, inclusa la fascia d’età, restano sul dispositivo. Alternix non li riceve. Puoi eliminare cronologia e tavolozze nell’app; cancellare i dati dell’app o disinstallarla rimuove gli altri dati interni. Il backup cloud è disattivato."),
            ("Fotocamera e foto", "La fotocamera è facoltativa e viene richiesta solo per scansionare colori. Scegli le foto nella finestra di sistema Android; l’app non accede all’intera galleria. Le immagini sono elaborate sul dispositivo e non inviate ad Alternix."),
            ("Pubblicità", "Google AdMob mostra banner e annunci con premio facoltativi. Google e partner possono raccogliere e condividere IP e posizione approssimativa ricavata dall’IP, identificatori di dispositivo e account (incluso quello pubblicitario), attività nell’app e negli annunci, dati su prestazioni ed errori e scelte di consenso. Servono a pubblicità, statistiche e prevenzione frodi. App Set ID serve solo a statistiche e prevenzione frodi. Foto, colori e tavolozze non sono condivisi con gli inserzionisti."),
            ("Età e consenso", "L’app è destinata a chi ha almeno 13 anni. Prima degli annunci scegli 13–17 o 18+, senza data di nascita. Per gli adolescenti gli annunci non sono personalizzati e hanno ulteriori limiti sui contenuti. Google richiede il consenso degli adulti dove necessario."),
            ("Salvare e condividere", "Scegli dove salvare le tavolozze o quale app le riceve. La condivisione crea file temporanei nell’app. I file salvati altrove o già inviati restano a te o al destinatario dopo la disinstallazione."),
            ("Questo sito", "GitHub Pages ospita il sito e può ricevere IP e dati sulle visite. Il sito non contiene pubblicità o strumenti di analisi. Il browser ricorda lingua e tema finché non cancelli i dati del sito. Informative sulla privacy: <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Protezione e conservazione", "Android protegge i dati interni dell’app; i dati pubblicitari sono cifrati durante il trasferimento. Google e partner, così come GitHub, conservano ed eliminano i dati secondo le proprie politiche."),
            ("Scelte e contatto", "Puoi modificare fascia d’età e opzioni disponibili di consenso pubblicitario nelle impostazioni. Domande sulla privacy: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix usa e-mail e messaggio per rispondere e li conserva solo per le esigenze dell’assistenza o di legge. Aggiorneremo l’informativa se cambierà il trattamento dei dati."),
        ],
        "support_intro": "Assistenza per Color Swatch Lab, strumenti colore, annunci ed esportazione.",
        "support_cards": [("Contatta il supporto", "Scrivi a <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a> indicando versioni, modello e passaggi."), ("Fotocamera e foto", "La fotocamera è facoltativa; le foto usano Android Photo Picker. Controlla il permesso se non si apre."), ("Annunci ed esportazione", "Le azioni protette richiedono Internet e un annuncio con premio disponibile; regione, privacy e inventario incidono."), ("Privacy", "L’informativa descrive dati locali e trattamento possibile da parte dell’SDK Google.")],
    },
    "pl": {
        "code": "PL", "skip": "Przejdź do treści", "privacy": "Polityka prywatności", "support": "Pomoc", "developer": "Deweloper", "updated": "Ostatnia aktualizacja: 9 września 2026", "on_page": "Na tej stronie", "official": "Oficjalna strona Alternix", "description": "Polityka prywatności Color Swatch Lab na Androida.",
        "sections": [
            ("O aplikacji", "Color Swatch Lab to aplikacja Alternix do pracy z kolorami i paletami. Nie wymaga konta."),
            ("Twoje dane", "Kolory, historia, ulubione, palety i ustawienia, w tym grupa wiekowa, pozostają na urządzeniu. Alternix ich nie otrzymuje. Historię i palety możesz usunąć w aplikacji; wyczyszczenie jej danych lub odinstalowanie usuwa pozostałe dane wewnętrzne. Kopia w chmurze jest wyłączona."),
            ("Aparat i zdjęcia", "Dostęp do aparatu jest opcjonalny i wymagany tylko do skanowania kolorów. Zdjęcia wybierasz w oknie systemowym Androida; aplikacja nie ma dostępu do całej galerii. Obrazy są przetwarzane na urządzeniu i nie trafiają do Alternix."),
            ("Reklamy", "Google AdMob wyświetla banery i opcjonalne reklamy z nagrodą. Google i partnerzy mogą zbierać i udostępniać adres IP i przybliżoną lokalizację na jego podstawie, identyfikatory urządzenia i konta (w tym reklamowy), aktywność w aplikacji i reklamach, dane o wydajności i błędach oraz wybory dotyczące zgody. Służą one reklamom, statystykom i zapobieganiu oszustwom. App Set ID służy wyłącznie statystykom i zapobieganiu oszustwom. Zdjęcia, kolory i palety nie są przekazywane reklamodawcom."),
            ("Wiek i zgoda", "Aplikacja jest przeznaczona dla osób od 13 lat. Przed reklamami wybierasz 13–17 lub 18+, bez daty urodzenia. Reklamy dla nastolatków nie są personalizowane i mają dodatkowe ograniczenia treści. Google prosi dorosłych o zgodę tam, gdzie jest wymagana."),
            ("Zapisywanie i udostępnianie", "Wybierasz miejsce zapisu palet lub aplikację, która je otrzyma. Udostępnianie tworzy pliki tymczasowe w aplikacji. Pliki zapisane gdzie indziej lub już wysłane pozostają u Ciebie lub odbiorcy po odinstalowaniu."),
            ("Ta witryna", "GitHub Pages udostępnia witrynę i może otrzymywać adresy IP oraz dane o wizytach. Witryna nie zawiera reklam ani analityki. Przeglądarka pamięta język i motyw do wyczyszczenia danych witryny. Polityki prywatności: <a href=\"https://policies.google.com/privacy\">Google</a> i <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Ochrona i przechowywanie", "Android chroni wewnętrzne dane aplikacji; dane reklamowe są szyfrowane podczas przesyłania. Google i partnerzy oraz GitHub przechowują i usuwają dane według własnych zasad."),
            ("Twój wybór i kontakt", "W ustawieniach możesz zmienić grupę wiekową i dostępne zgody reklamowe. Pytania o prywatność: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. Alternix używa Twojego adresu e-mail i wiadomości do odpowiedzi, przechowując je tylko tak długo, jak wymaga pomoc lub prawo. Zaktualizujemy politykę przy zmianie sposobu przetwarzania danych."),
        ],
        "support_intro": "Pomoc dotycząca Color Swatch Lab, narzędzi kolorów, reklam i eksportu.",
        "support_cards": [("Kontakt z pomocą", "Napisz na <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>, podając wersje, model i kroki."), ("Aparat i zdjęcia", "Aparat jest opcjonalny; zdjęcia używają Android Photo Picker. Sprawdź uprawnienie, jeśli aparat się nie otwiera."), ("Reklamy i eksport", "Chronione działania wymagają Internetu i dostępnej reklamy z nagrodą; wpływają region, prywatność i zasoby reklam."), ("Prywatność", "Polityka opisuje dane lokalne i możliwe przetwarzanie przez SDK Google.")],
    },
    "pt": {
        "code": "PT", "skip": "Ir para o conteúdo", "privacy": "Política de privacidade", "support": "Suporte", "developer": "Programador", "updated": "Última atualização: 9 de setembro de 2026", "on_page": "Nesta página", "official": "Site oficial da Alternix", "description": "Política de privacidade do Color Swatch Lab para Android.",
        "sections": [
            ("Sobre a aplicação", "Color Swatch Lab é uma aplicação da Alternix para cores e paletas. Não exige uma conta."),
            ("Os seus dados", "Cores, histórico, favoritos, paletas e definições, incluindo a faixa etária, ficam no dispositivo. A Alternix não os recebe. Pode apagar histórico e paletas na aplicação; limpar os dados ou desinstalar remove os restantes dados internos. A cópia na nuvem está desativada."),
            ("Câmara e fotos", "O acesso à câmara é opcional e pedido apenas para identificar cores. Escolhe as fotos na janela do sistema Android; a aplicação não acede à galeria inteira. As imagens são processadas no dispositivo e não enviadas à Alternix."),
            ("Publicidade", "O Google AdMob mostra banners e anúncios premiados opcionais. A Google e os parceiros podem recolher e partilhar IP e localização aproximada derivada do IP, identificadores do dispositivo e da conta (incluindo o de publicidade), atividade na aplicação e nos anúncios, dados de desempenho e erros e escolhas de consentimento. Servem para publicidade, estatísticas e prevenção de fraude. O App Set ID serve apenas para estatísticas e prevenção de fraude. Fotos, cores e paletas não são partilhadas com anunciantes."),
            ("Idade e consentimento", "A aplicação destina-se a pessoas a partir dos 13 anos. Antes dos anúncios escolhe 13–17 ou 18+, sem data de nascimento. Para adolescentes, os anúncios não são personalizados e têm restrições adicionais de conteúdo. A Google pede consentimento aos adultos quando necessário."),
            ("Guardar e partilhar", "Escolhe onde guardar as paletas ou que aplicação as recebe. A partilha cria ficheiros temporários dentro da aplicação. Ficheiros guardados noutro local ou já enviados ficam consigo ou com o destinatário após a desinstalação."),
            ("Este site", "O GitHub Pages aloja o site e pode receber endereços IP e registos de visitas. O site não contém publicidade nem ferramentas de análise. O navegador memoriza idioma e tema até limpar os dados do site. Políticas de privacidade: <a href=\"https://policies.google.com/privacy\">Google</a> e <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub</a>."),
            ("Proteção e conservação", "O Android protege os dados internos da aplicação; os dados publicitários são encriptados durante a transmissão. A Google e os parceiros, bem como o GitHub, conservam e apagam dados segundo as suas próprias políticas."),
            ("Escolhas e contacto", "Pode alterar a faixa etária e as opções disponíveis de consentimento publicitário nas definições. Questões de privacidade: <a href=\"mailto:alternix.apps@gmail.com\">alternix.apps@gmail.com</a>. A Alternix usa o seu e-mail e mensagem para responder e conserva-os apenas enquanto necessário para suporte ou por lei. Atualizaremos a política se o tratamento de dados mudar."),
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
