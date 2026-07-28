(() => {
  const root = document.documentElement;
  const button = document.querySelector("[data-theme-toggle]");
  if (!button) return;

  const updateLabel = () => {
    const dark = root.dataset.theme === "dark" ||
      (!root.dataset.theme && window.matchMedia("(prefers-color-scheme: dark)").matches);
    button.setAttribute("aria-label", dark ? button.dataset.lightLabel : button.dataset.darkLabel);
    button.textContent = dark ? "☀" : "☾";
  };

  button.addEventListener("click", () => {
    const dark = root.dataset.theme === "dark" ||
      (!root.dataset.theme && window.matchMedia("(prefers-color-scheme: dark)").matches);
    root.dataset.theme = dark ? "light" : "dark";
    updateLabel();
  });

  updateLabel();
})();
