(function () {
  "use strict";

  const CONFIG = {
    ORIGINAL_WIDTH: 1200,
    ORIGINAL_HEIGHT: 628,
    TOP_Y_OFFSET: 20,
    X_SIDE_OFFSET: 20,
    BAR_HEIGHT_RATIO: 7,
    MIN_FONT: 12,
    MAX_FONT: 99,
  };

  let previousSize = { w: 0, h: 0 };

  // Cache title containers once
  const titleContainers = Array.from({ length: 2 }, (_, i) =>
    document.getElementById(`title${i + 1}`),
  );

  /**
   * Split text around center
   */
  const splitAtMiddle = (text) => {
    if (!text || !text.includes(" ")) return [text];

    const mid = Math.floor(text.length / 2);

    // Look for nearest space on the left and on the right of the middle
    // and remove invalid results (-1 meaning no space found).
    const candidates = [
      text.lastIndexOf(" ", mid),
      text.indexOf(" ", mid),
    ].filter((i) => i !== -1);

    // Pick the closest candidate to the center
    const splitIndex = candidates.reduce((best, i) =>
      Math.abs(i - mid) < Math.abs(best - mid) ? i : best,
    );

    return [text.slice(0, splitIndex), text.slice(splitIndex + 1)];
  };

  /**
   * Font size directly from bar height
   */
  const calculateFontSize = (barH) => {
    const size = Math.floor((11 * barH) / 12 - 1.25);
    return Math.max(CONFIG.MIN_FONT, Math.min(CONFIG.MAX_FONT, size));
  };

  /**
   * Main render
   */
  const render = () => {
    const img = document.querySelector(".featured-image img");
    if (!img) return;

    const w = img.clientWidth;
    const h = img.clientHeight;

    if (Math.abs(w - previousSize.w) < 1 && Math.abs(h - previousSize.h) < 1)
      return;

    previousSize = { w, h };

    const altText = img.alt || "";
    const lines = splitAtMiddle(altText);

    const barHeight = Math.floor(h / CONFIG.BAR_HEIGHT_RATIO);
    const fontSize = calculateFontSize(barHeight);

    const xPaddding = (CONFIG.X_SIDE_OFFSET * w) / CONFIG.ORIGINAL_WIDTH;
    const yStart = (CONFIG.TOP_Y_OFFSET * h) / CONFIG.ORIGINAL_HEIGHT;

    let y = yStart;

    for (let i = 0; i < lines.length; i++) {
      const container = titleContainers[i];
      if (!container) continue;

      const title = container.querySelector(".image-title");

      container.style.top = `${y}px`;

      title.style.padding = `0 ${xPaddding}px`;
      title.style.fontSize = `${fontSize}px`;
      title.style.lineHeight = `${barHeight}px`;
      title.textContent = lines[i];

      y += barHeight + yStart;
    }
  };

  document.addEventListener("DOMContentLoaded", () => {
    const img = document.querySelector(".featured-image img");
    if (!img) return;

    render();

    const observer = new ResizeObserver(() => requestAnimationFrame(render));

    observer.observe(img);

    img.addEventListener("load", render);
  });
})();
