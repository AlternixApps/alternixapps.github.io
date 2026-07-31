(() => {
  const root = document.documentElement;
  const storageKey = "alternix-company-theme";
  const moon = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15.5A8.5 8.5 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z"/></svg>';
  const sun = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>';

  const readTheme = () => {
    try {
      return localStorage.getItem(storageKey) === "light" ? "light" : "dark";
    } catch {
      return "dark";
    }
  };

  const setTheme = (theme) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    const themeColor = document.querySelector('meta[name="theme-color"]');
    if (themeColor) themeColor.setAttribute("content", theme === "light" ? "#f2f2f0" : "#050505");
    const toggle = document.querySelector("[data-theme-toggle]");
    if (toggle) {
      const light = theme === "light";
      toggle.innerHTML = light ? moon : sun;
      toggle.setAttribute("aria-label", light ? toggle.dataset.darkLabel : toggle.dataset.lightLabel);
      toggle.setAttribute("title", light ? toggle.dataset.darkLabel : toggle.dataset.lightLabel);
    }
  };

  setTheme(readTheme());

  const init = () => {
    const toggle = document.querySelector("[data-theme-toggle]");
    if (toggle) {
      setTheme(readTheme());
      toggle.addEventListener("click", () => {
        const next = root.dataset.theme === "light" ? "dark" : "light";
        setTheme(next);
        try { localStorage.setItem(storageKey, next); } catch { /* Keep the session theme. */ }
      });
    }

    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const preloader = document.querySelector("[data-preloader]");
    if (preloader) {
      const delay = reducedMotion ? 0 : 850;
      window.setTimeout(() => {
        preloader.classList.add("is-hidden");
        window.setTimeout(() => preloader.remove(), reducedMotion ? 0 : 520);
      }, delay);
    }

    const revealItems = document.querySelectorAll(".reveal");
    if (reducedMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach((item) => item.classList.add("is-visible"));
    } else {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -7%" });
      revealItems.forEach((item) => observer.observe(item));
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
