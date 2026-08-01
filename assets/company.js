(() => {
  const root = document.documentElement;
  const storageKey = "alternix-company-theme";
  const moon = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15.5A8.5 8.5 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z"/></svg>';
  const sun = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>';

  const readTheme = () => {
    try { return localStorage.getItem(storageKey) === "light" ? "light" : "dark"; }
    catch { return "dark"; }
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

  const initSlider = () => {
    document.querySelectorAll("[data-product-slider]").forEach((slider) => {
      const track = slider.querySelector("[data-slider-track]");
      const slides = [...slider.querySelectorAll("[data-product-slide]")];
      const dots = [...slider.querySelectorAll("[data-slider-dot]")];
      const previous = slider.querySelector("[data-slider-prev]");
      const next = slider.querySelector("[data-slider-next]");
      if (!track || slides.length < 2) return;

      let current = 0;
      const setCurrent = (index, scroll = true) => {
        current = (index + slides.length) % slides.length;
        dots.forEach((dot, dotIndex) => {
          dot.classList.toggle("is-active", dotIndex === current);
          dot.setAttribute("aria-current", dotIndex === current ? "true" : "false");
        });
        if (scroll) slides[current].scrollIntoView({ behavior: "smooth", block: "nearest", inline: "start" });
      };

      previous?.addEventListener("click", () => setCurrent(current - 1));
      next?.addEventListener("click", () => setCurrent(current + 1));
      dots.forEach((dot, index) => dot.addEventListener("click", () => setCurrent(index)));
      track.addEventListener("scroll", () => {
        const width = track.clientWidth || 1;
        const index = Math.max(0, Math.min(slides.length - 1, Math.round(track.scrollLeft / width)));
        if (index !== current) setCurrent(index, false);
      }, { passive: true });
      setCurrent(0, false);
    });
  };

  const initSectionNavigation = () => {
    const links = [...document.querySelectorAll("[data-section-link]")];
    if (!links.length) return;
    const sections = links.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
    const activate = (id) => links.forEach((link) => link.classList.toggle("is-active", link.getAttribute("href") === `#${id}`));
    let frameRequested = false;
    const update = () => {
      frameRequested = false;
      const marker = Math.min(window.innerHeight * .34, 320);
      let current = sections[0];
      sections.forEach((section) => {
        if (section.getBoundingClientRect().top <= marker) current = section;
      });
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) {
        current = sections[sections.length - 1];
      }
      if (current) activate(current.id);
    };
    const scheduleUpdate = () => {
      if (frameRequested) return;
      frameRequested = true;
      window.requestAnimationFrame(update);
    };
    links.forEach((link) => link.addEventListener("click", () => {
      const id = link.getAttribute("href").slice(1);
      activate(id);
    }));
    window.addEventListener("scroll", scheduleUpdate, { passive: true });
    window.addEventListener("resize", scheduleUpdate, { passive: true });
    window.addEventListener("hashchange", scheduleUpdate);
    update();
  };

  const initCopyButtons = () => {
    document.querySelectorAll("[data-copy-email]").forEach((button) => {
      button.addEventListener("click", async () => {
        const status = document.querySelector(button.dataset.statusTarget || "[data-copy-status]");
        try {
          await navigator.clipboard.writeText("alternix.apps@gmail.com");
          if (status) status.textContent = button.dataset.copiedLabel || "Copied";
        } catch {
          if (status) status.textContent = "alternix.apps@gmail.com";
        }
      });
    });
  };

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

    document.addEventListener("click", (event) => {
      document.querySelectorAll("details.language-menu[open]").forEach((menu) => {
        if (!menu.contains(event.target)) menu.removeAttribute("open");
      });
    });

    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const preloader = document.querySelector("[data-preloader]");
    if (preloader) {
      const delay = reducedMotion ? 0 : 1650;
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

    initSlider();
    initSectionNavigation();
    initCopyButtons();
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
