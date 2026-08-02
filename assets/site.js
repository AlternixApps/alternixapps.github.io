(() => {
  const storageKey = "alternix-theme";
  const root = document.documentElement;

  const readTheme = () => {
    try {
      return window.localStorage.getItem(storageKey) === "dark" ? "dark" : "light";
    } catch {
      return "light";
    }
  };

  const saveTheme = (theme) => {
    try {
      window.localStorage.setItem(storageKey, theme);
    } catch {
      // The selected theme still works for this page when storage is unavailable.
    }
  };

  const moonIcon = `
    <svg class="theme-icon" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M20.4 15.2A8.7 8.7 0 0 1 8.8 3.6 8.7 8.7 0 1 0 20.4 15.2Z"/>
    </svg>`;
  const sunIcon = `
    <svg class="theme-icon" viewBox="0 0 24 24" aria-hidden="true">
      <circle cx="12" cy="12" r="4"/>
      <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"/>
    </svg>`;

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
  };

  applyTheme(readTheme());

  const initializeMobileNavigation = () => {
    const header = document.querySelector(".site-header");
    const nav = header?.querySelector(".site-nav");
    const actions = header?.querySelector(".header-actions");
    if (!header || !nav || !actions) return;

    const labels = {
      en: ["Open menu", "Close menu"], uk: ["Відкрити меню", "Закрити меню"],
      ru: ["Открыть меню", "Закрыть меню"], es: ["Abrir menú", "Cerrar menú"],
      de: ["Menü öffnen", "Menü schließen"], fr: ["Ouvrir le menu", "Fermer le menu"],
      pt: ["Abrir menu", "Fechar menu"], it: ["Apri menu", "Chiudi menu"],
      pl: ["Otwórz menu", "Zamknij menu"],
    };
    const language = root.lang in labels ? root.lang : "en";
    const [openLabel, closeLabel] = labels[language];
    const button = document.createElement("button");
    button.type = "button";
    button.className = "mobile-menu-toggle";
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("aria-label", openLabel);
    button.innerHTML = '<span></span><span></span><span></span>';
    actions.prepend(button);

    const setOpen = (open) => {
      header.classList.toggle("is-menu-open", open);
      button.setAttribute("aria-expanded", String(open));
      button.setAttribute("aria-label", open ? closeLabel : openLabel);
    };
    header._closeMobileMenu = () => setOpen(false);

    button.addEventListener("click", () => setOpen(!header.classList.contains("is-menu-open")));
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) setOpen(false);
    });
    document.addEventListener("click", (event) => {
      if (!header.contains(event.target)) setOpen(false);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && header.classList.contains("is-menu-open")) {
        setOpen(false);
        button.focus();
      }
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 760) setOpen(false);
    }, { passive: true });
  };

  const initializeControls = () => {
    initializeMobileNavigation();
    const button = document.querySelector("[data-theme-toggle]");
    if (!button) return;

    const updateButton = () => {
      const dark = root.dataset.theme === "dark";
      button.setAttribute(
        "aria-label",
        dark ? button.dataset.lightLabel : button.dataset.darkLabel,
      );
      button.innerHTML = dark ? sunIcon : moonIcon;
    };

    button.addEventListener("click", () => {
      const theme = root.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(theme);
      saveTheme(theme);
      updateButton();
    });

    updateButton();

    const languageMenu = document.querySelector(".language-menu");
    if (languageMenu) {
      const panel = languageMenu.querySelector(".language-panel");
      const summary = languageMenu.querySelector("summary");
      languageMenu.open = false;
      summary?.setAttribute("aria-expanded", "false");
      const clamp = (value, minimum, maximum) => Math.min(maximum, Math.max(minimum, value));
      const positionPanel = () => {
        if (!panel || !summary || !languageMenu.open) return;
        const anchor = summary.getBoundingClientRect();
        const panelWidth = Math.min(window.innerWidth <= 760 ? 286 : 172, window.innerWidth - 20);
        const left = clamp(anchor.right - panelWidth, 10, window.innerWidth - panelWidth - 10);
        panel.style.width = `${panelWidth}px`;
        panel.style.left = `${Math.round(left)}px`;
        panel.style.right = "auto";
        panel.style.top = `${Math.round(anchor.bottom + 12)}px`;
      };
      if (panel) {
        panel.hidden = true;
        document.body.append(panel);
      }
      languageMenu.addEventListener("toggle", () => {
        if (panel) panel.hidden = !languageMenu.open;
        summary?.setAttribute("aria-expanded", String(languageMenu.open));
        if (languageMenu.open) {
          document.querySelector(".site-header")?._closeMobileMenu?.();
          window.requestAnimationFrame(positionPanel);
        }
      });
      window.addEventListener("resize", positionPanel, { passive: true });
      window.addEventListener("scroll", positionPanel, { passive: true });
      document.addEventListener("click", (event) => {
        if (!languageMenu.contains(event.target) && !panel?.contains(event.target)) {
          languageMenu.open = false;
          summary?.setAttribute("aria-expanded", "false");
          if (panel) panel.hidden = true;
        }
      });
      document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && languageMenu.open) {
          languageMenu.open = false;
          summary?.setAttribute("aria-expanded", "false");
          if (panel) panel.hidden = true;
          summary?.focus();
        }
      });
    }

    document.querySelectorAll("[data-copy-email]").forEach((copyButton) => {
      copyButton.addEventListener("click", async () => {
        const email = copyButton.dataset.copyEmail;
        try {
          await navigator.clipboard.writeText(email);
          copyButton.textContent = copyButton.dataset.copiedLabel;
          window.setTimeout(() => {
            copyButton.textContent = copyButton.dataset.copyLabel;
          }, 1800);
        } catch {
          window.prompt(copyButton.dataset.copyLabel, email);
        }
      });
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeControls, { once: true });
  } else {
    initializeControls();
  }
})();
