(function () {
  "use strict";

  const CONFIG = Object.freeze({
    ORIGINAL_WIDTH: 1200,
    ORIGINAL_HEIGHT: 628,
    TOP_Y_OFFSET: 20,
    X_SIDE_OFFSET: 20,
    BAR_HEIGHT_RATIO: 7,
    MIN_FONT: 12,
    MAX_FONT: 99,
    TITLES: 2,
  });

  function splitText(text) {
    if (!text) return [""];
    const mid = (text.length / 2) | 0;
    const left = text.lastIndexOf(" ", mid);
    const right = text.indexOf(" ", mid);

    if (left === -1 && right === -1) return [text];
    const split =
      left === -1 ? right
      : right === -1 ? left
      : mid - left <= right - mid ? left
      : right;
    return [text.slice(0, split).trim(), text.slice(split + 1).trim()];
  }

  function computeLayout({ width, height, text }) {
    const lines = splitText(text);
    const barHeight = Math.floor(height / CONFIG.BAR_HEIGHT_RATIO);
    const fontSizeRaw = (11 * barHeight) / 12 - 1.25;
    const fontSize = Math.max(
      CONFIG.MIN_FONT,
      Math.min(CONFIG.MAX_FONT, fontSizeRaw | 0),
    );
    const xPadding = (CONFIG.X_SIDE_OFFSET * width) / CONFIG.ORIGINAL_WIDTH;
    const yBase = (CONFIG.TOP_Y_OFFSET * height) / CONFIG.ORIGINAL_HEIGHT;

    return lines.map((line, i) => ({
      text: line || "",
      top: (barHeight + yBase) * i + yBase,
      fontSize,
      lineHeight: barHeight,
      paddingX: xPadding,
    }));
  }

  class TitleRenderer {
    constructor(img) {
      this.img = img;
      this.containers = Array.from({ length: CONFIG.TITLES }, (_, i) =>
        document.getElementById(`title${i + 1}`),
      ).filter(Boolean);

      this.lastW = 0;
      this.lastH = 0;
      this.initialized = false;
    }

    render() {
      const w = this.img.clientWidth;
      const h = this.img.clientHeight;

      if (
        w === 0 ||
        (Math.abs(w - this.lastW) < 1 && Math.abs(h - this.lastH) < 1)
      )
        return;

      this.lastW = w;
      this.lastH = h;

      const layout = computeLayout({
        width: w,
        height: h,
        text: this.img.alt || "",
      });

      this.containers.forEach((container, i) => {
        const block = layout[i];
        if (!block) return;

        const title = container.querySelector(".image-title");
        if (!title) return;

        container.style.top = `${block.top}px`;

        title.style.fontSize = `${block.fontSize}px`;
        title.style.lineHeight = `${block.lineHeight}px`;
        title.style.paddingLeft = `${block.paddingX}px`;
        title.style.paddingRight = `${block.paddingX}px`;

        if (title.textContent !== block.text) {
          title.textContent = block.text;
        }
      });

      // Fade in once the first valid layout is calculated
      if (!this.initialized) {
        this.initialized = true;
        this.containers.forEach((c) => (c.style.opacity = "1"));
      }
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    const img = document.querySelector(".featured-image img");
    if (!img) return;

    const renderer = new TitleRenderer(img);
    let rafPending = false;

    const schedule = () => {
      if (rafPending) return;
      rafPending = true;
      requestAnimationFrame(() => {
        renderer.render();
        rafPending = false;
      });
    };

    const observer = new ResizeObserver(schedule);
    observer.observe(img);

    // Initial check
    if (img.complete) schedule();
    img.addEventListener("load", schedule);
  });
})();
