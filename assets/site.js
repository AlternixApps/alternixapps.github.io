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

  const initializeControls = () => {
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
      document.addEventListener("click", (event) => {
        if (!languageMenu.contains(event.target)) languageMenu.removeAttribute("open");
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
