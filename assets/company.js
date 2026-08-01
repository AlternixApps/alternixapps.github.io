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

  const initLanguageMenus = () => {
    const menus = [...document.querySelectorAll("details.language-menu")];
    if (!menus.length) return;

    const clamp = (value, minimum, maximum) => Math.min(maximum, Math.max(minimum, value));
    const positionPanel = (menu) => {
      const summary = menu.querySelector("summary");
      const panel = menu._languagePanel;
      if (!summary || !panel || !menu.open) return;
      const anchor = summary.getBoundingClientRect();
      const panelWidth = Math.min(230, window.innerWidth - 28);
      const left = clamp(anchor.right - panelWidth, 14, window.innerWidth - panelWidth - 14);
      panel.style.width = `${panelWidth}px`;
      panel.style.left = `${Math.round(left)}px`;
      panel.style.top = `${Math.round(anchor.bottom + 18)}px`;
    };

    const closeMenu = (menu) => {
      menu.removeAttribute("open");
      if (menu._languagePanel) menu._languagePanel.hidden = true;
    };

    menus.forEach((menu) => {
      const panel = menu.querySelector(".language-panel");
      if (!panel) return;
      menu._languagePanel = panel;
      panel.classList.add("language-panel-portal");
      panel.hidden = true;
      document.body.append(panel);

      menu.addEventListener("toggle", () => {
        panel.hidden = !menu.open;
        if (menu.open) window.requestAnimationFrame(() => positionPanel(menu));
      });
    });

    const repositionOpenPanels = () => menus.forEach((menu) => positionPanel(menu));
    window.addEventListener("resize", repositionOpenPanels, { passive: true });
    window.addEventListener("scroll", repositionOpenPanels, { passive: true });

    document.addEventListener("click", (event) => {
      menus.forEach((menu) => {
        if (!menu.open) return;
        const panel = menu._languagePanel;
        if (!menu.contains(event.target) && !panel?.contains(event.target)) closeMenu(menu);
      });
    });

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") return;
      menus.forEach((menu) => {
        if (!menu.open) return;
        closeMenu(menu);
        menu.querySelector("summary")?.focus();
      });
    });
  };

  const initInteractiveMark = (reducedMotion) => {
    const mark = document.querySelector("[data-interactive-mark]");
    const hero = mark?.closest(".hero");
    const orbit = mark?.querySelector("[data-orbit]");
    const trigger = mark?.querySelector("[data-wave-trigger]");
    const canvas = hero?.querySelector("[data-wave-canvas]");
    const handles = mark ? [...mark.querySelectorAll("[data-orbit-handle]")] : [];
    if (!mark || !hero || !orbit || !trigger || !canvas) return;

    const context = canvas.getContext("2d", { alpha: true });
    if (!context) return;

    const baseVelocity = 360 / 22000;
    let angle = 0;
    let velocity = baseVelocity;
    let dragging = false;
    let activePointer = null;
    let previousPointerAngle = 0;
    let previousPointerTime = 0;
    let dragDistance = 0;
    let previousFrame = performance.now();
    let animationFrame = 0;
    let wave = null;
    let waveCanRewind = false;
    let canvasWidth = 0;
    let canvasHeight = 0;

    const normalizeAngle = (value) => {
      let normalized = value;
      while (normalized > 180) normalized -= 360;
      while (normalized < -180) normalized += 360;
      return normalized;
    };

    const pointerAngle = (event) => {
      const bounds = mark.getBoundingClientRect();
      const x = event.clientX - (bounds.left + bounds.width / 2);
      const y = event.clientY - (bounds.top + bounds.height / 2);
      return Math.atan2(y, x) * 180 / Math.PI;
    };

    const resizeCanvas = () => {
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvasWidth = Math.max(1, window.innerWidth);
      canvasHeight = Math.max(1, window.innerHeight);
      canvas.width = Math.round(canvasWidth * ratio);
      canvas.height = Math.round(canvasHeight * ratio);
      canvas.style.width = `${canvasWidth}px`;
      canvas.style.height = `${canvasHeight}px`;
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
    };

    const drawWave = (progress) => {
      context.clearRect(0, 0, canvasWidth, canvasHeight);
      const triggerBounds = trigger.getBoundingClientRect();
      const centerX = triggerBounds.left + triggerBounds.width / 2;
      const centerY = triggerBounds.top + triggerBounds.height / 2;
      const maxRadius = Math.max(
        Math.hypot(centerX, centerY),
        Math.hypot(canvasWidth - centerX, centerY),
        Math.hypot(centerX, canvasHeight - centerY),
        Math.hypot(canvasWidth - centerX, canvasHeight - centerY),
      ) + 170;
      const startRadius = Math.min(triggerBounds.width, triggerBounds.height) * .78;
      const leadingRadius = startRadius + progress * (maxRadius - startRadius);
      const styles = getComputedStyle(root);
      const rippleGrid = styles.getPropertyValue("--grid-ripple").trim();
      const gridSize = 64;

      const rippleOffsets = [0, 88, 176, 264, 352];
      const rippleBands = rippleOffsets
        .map((offset, index) => ({ radius: leadingRadius - offset, spread: 52 + index * 7 }))
        .filter((band) => band.radius > 0);
      if (!rippleBands.length) return;

      context.save();
      context.globalAlpha = .92;
      context.strokeStyle = rippleGrid;
      context.lineWidth = 1;

      const displacementAt = (x, y) => {
        const dx = x - centerX;
        const dy = y - centerY;
        const distance = Math.hypot(dx, dy) || 1;
        let displacement = 0;
        rippleOffsets.forEach((offset, index) => {
          const radius = leadingRadius - offset;
          if (radius <= 0) return;
          const spread = 66 + index * 13;
          const delta = distance - radius;
          const envelope = Math.exp(-(delta * delta) / (2 * spread * spread));
          const strength = 30 - index * 4.2;
          displacement += Math.cos(delta / spread * Math.PI * 1.12) * envelope * strength;
        });
        return { x: x + dx / distance * displacement, y: y + dy / distance * displacement };
      };

      const sampleLine = (vertical, coordinate) => {
        context.beginPath();
        const length = vertical ? canvasHeight : canvasWidth;
        for (let value = 0; value <= length + 6; value += 6) {
          const point = displacementAt(vertical ? coordinate : value, vertical ? value : coordinate);
          if (value === 0) context.moveTo(point.x, point.y);
          else context.lineTo(point.x, point.y);
        }
        context.stroke();
      };

      for (let x = 0; x <= canvasWidth; x += gridSize) sampleLine(true, x);
      for (let y = 0; y <= canvasHeight; y += gridSize) sampleLine(false, y);
      context.restore();

      context.save();
      context.globalCompositeOperation = "destination-in";
      const radialMask = context.createRadialGradient(centerX, centerY, 0, centerX, centerY, maxRadius);
      const maskStops = [{ offset: 0, alpha: 0 }, { offset: 1, alpha: 0 }];
      rippleBands.forEach(({ radius, spread }) => {
        maskStops.push(
          { offset: Math.max(0, (radius - spread) / maxRadius), alpha: 0 },
          { offset: Math.max(0, Math.min(1, radius / maxRadius)), alpha: .9 },
          { offset: Math.min(1, (radius + spread) / maxRadius), alpha: 0 },
        );
      });
      maskStops
        .sort((left, right) => left.offset - right.offset)
        .forEach(({ offset, alpha }, index, stops) => {
          const previous = index ? stops[index - 1].offset : -1;
          radialMask.addColorStop(Math.max(previous, offset), `rgba(255,255,255,${alpha})`);
        });
      context.fillStyle = radialMask;
      context.fillRect(0, 0, canvasWidth, canvasHeight);

      const verticalFade = context.createLinearGradient(0, 0, 0, canvasHeight);
      verticalFade.addColorStop(0, "rgba(255,255,255,0)");
      verticalFade.addColorStop(.16, "rgba(255,255,255,1)");
      verticalFade.addColorStop(.82, "rgba(255,255,255,1)");
      verticalFade.addColorStop(1, "rgba(255,255,255,0)");
      context.fillStyle = verticalFade;
      context.fillRect(0, 0, canvasWidth, canvasHeight);
      context.restore();
    };

    const startWave = (direction) => {
      if (reducedMotion) {
        mark.animate([{ opacity: 1 }, { opacity: .72 }, { opacity: 1 }], { duration: 240, easing: "ease-out" });
        return;
      }
      wave = { direction, started: performance.now(), duration: direction > 0 ? 3800 : 3150 };
      waveCanRewind = false;
      drawWave(direction > 0 ? 0 : 1);
      document.body.classList.add("is-wave-active");
      mark.dataset.waveState = direction > 0 ? "forward" : "reverse";
    };

    trigger.addEventListener("click", () => startWave(1));

    const finishDrag = (event, allowRewind) => {
      if (!dragging || event.pointerId !== activePointer) return;
      dragging = false;
      mark.classList.remove("is-dragging");
      try { event.currentTarget.releasePointerCapture(event.pointerId); } catch { /* Pointer capture may already be released. */ }
      activePointer = null;
      if (allowRewind && dragDistance < -48 && waveCanRewind && !wave) startWave(-1);
    };

    handles.forEach((handle) => {
      handle.addEventListener("pointerdown", (event) => {
        if (reducedMotion || dragging) return;
        event.preventDefault();
        dragging = true;
        activePointer = event.pointerId;
        previousPointerAngle = pointerAngle(event);
        previousPointerTime = performance.now();
        dragDistance = 0;
        velocity = 0;
        mark.classList.add("is-dragging");
        handle.setPointerCapture(event.pointerId);
      });
      handle.addEventListener("pointermove", (event) => {
        if (!dragging || event.pointerId !== activePointer) return;
        event.preventDefault();
        const now = performance.now();
        const nextPointerAngle = pointerAngle(event);
        const delta = normalizeAngle(nextPointerAngle - previousPointerAngle);
        const elapsed = Math.max(8, now - previousPointerTime);
        angle += delta;
        dragDistance += delta;
        velocity = Math.max(-.65, Math.min(.65, delta / elapsed));
        if (dragDistance < -48 && waveCanRewind && !wave) startWave(-1);
        previousPointerAngle = nextPointerAngle;
        previousPointerTime = now;
      });
      handle.addEventListener("pointerup", (event) => finishDrag(event, true));
      handle.addEventListener("pointercancel", (event) => finishDrag(event, false));
      handle.addEventListener("lostpointercapture", (event) => finishDrag(event, false));
    });

    const animate = (now) => {
      const elapsed = Math.min(34, Math.max(0, now - previousFrame));
      previousFrame = now;

      if (!reducedMotion && !dragging) {
        const returnStrength = 1 - Math.exp(-elapsed / 2600);
        velocity += (baseVelocity - velocity) * returnStrength;
        angle += velocity * elapsed;
      }
      orbit.style.setProperty("--orbit-angle", `${angle.toFixed(3)}deg`);

      if (wave) {
        const linear = Math.min(1, (now - wave.started) / wave.duration);
        const eased = 1 - Math.pow(1 - linear, 1.25);
        const progress = wave.direction > 0 ? eased : 1 - eased;
        drawWave(progress);
        if (linear >= 1) {
          const completedDirection = wave.direction;
          wave = null;
          document.body.classList.remove("is-wave-active");
          context.clearRect(0, 0, canvasWidth, canvasHeight);
          waveCanRewind = completedDirection > 0;
          mark.dataset.waveState = completedDirection > 0 ? "ready" : "idle";
        }
      }

      animationFrame = window.requestAnimationFrame(animate);
    };

    resizeCanvas();
    if ("ResizeObserver" in window) new ResizeObserver(resizeCanvas).observe(hero);
    else window.addEventListener("resize", resizeCanvas, { passive: true });
    if (reducedMotion) mark.dataset.waveState = "reduced";
    animationFrame = window.requestAnimationFrame(animate);
    window.addEventListener("pagehide", () => window.cancelAnimationFrame(animationFrame), { once: true });
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
    initLanguageMenus();
    initInteractiveMark(reducedMotion);
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
