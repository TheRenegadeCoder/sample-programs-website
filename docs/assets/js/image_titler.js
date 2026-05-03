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

  /**
   * Converts image dimensions into scalable title layout.
   */
  function computeLayout({ width, height, lines }) {
    // Each title "band" height
    const barHeight = Math.floor(height / CONFIG.BAR_HEIGHT_RATIO);

    // Font scaling based on bar height
    const rawFontSize = (11 * barHeight) / 12 - 1.25;
    const fontSize = Math.max(
      CONFIG.MIN_FONT,
      Math.min(CONFIG.MAX_FONT, rawFontSize | 0),
    );

    // Horizontal padding scales with width
    const paddingX = (CONFIG.X_SIDE_OFFSET * width) / CONFIG.ORIGINAL_WIDTH;

    // Vertical offset scales with height
    const baseYOffset = (CONFIG.TOP_Y_OFFSET * height) / CONFIG.ORIGINAL_HEIGHT;

    return lines.map((line, i) => ({
      text: line || "",

      // Stack lines vertically
      top: (barHeight + baseYOffset) * i + baseYOffset,

      fontSize,
      lineHeight: barHeight,
      paddingX,
    }));
  }

  /**
   * Handles rendering title overlays on top of an image.
   * Keeps DOM updates minimal and responds to resize/font load changes.
   */
  class TitleRenderer {
    constructor(img) {
      this.img = img;

      /**
       * Cache DOM references once.
       * Each item holds:
       * - container element
       * - title element
       * - last applied state (to avoid redundant DOM writes)
       */
      this.items = Array.from({ length: CONFIG.TITLES }, (_, i) => {
        const container = document.getElementById(`title${i + 1}`);
        if (!container) return null;

        const title = container.querySelector(".image-title");
        if (!title) return null;

        return {
          container,
          title,
          text: title.textContent.trim(),
          last: { top: null, fontSize: null, lineHeight: null, paddingX: null },
        };
      }).filter(Boolean);

      this.lastWidth = 0;
      this.lastHeight = 0;
      this.initialized = false;
    }

    /**
     * Main render loop:
     * - runs only when image size changes
     * - updates DOM minimally
     */
    render() {
      const img = this.img;

      const width = img.clientWidth;
      const height = img.clientHeight;

      // Ignore invalid layouts
      if (width === 0 || height === 0) return;

      // Skip if size didn't meaningfully change
      const isSameSize =
        Math.abs(width - this.lastWidth) < 1 &&
        Math.abs(height - this.lastHeight) < 1;

      if (isSameSize) return;

      this.lastWidth = width;
      this.lastHeight = height;

      const layout = computeLayout({
        width,
        height,
        lines: this.items.map((item) => item.text),
      });

      this.items.forEach((item, i) => {
        const block = layout[i];
        if (!block) return;

        const { container, title, last } = item;

        // Update only if value changed (prevents layout thrashing)
        if (last.top !== block.top) {
          container.style.top = `${block.top}px`;
          last.top = block.top;
        }

        if (last.fontSize !== block.fontSize) {
          title.style.fontSize = `${block.fontSize}px`;
          last.fontSize = block.fontSize;
        }

        if (last.lineHeight !== block.lineHeight) {
          title.style.lineHeight = `${block.lineHeight}px`;
          last.lineHeight = block.lineHeight;
        }

        if (last.paddingX !== block.paddingX) {
          const px = `${block.paddingX}px`;
          title.style.paddingLeft = px;
          title.style.paddingRight = px;
          last.paddingX = block.paddingX;
        }
      });

      // First-time reveal
      if (!this.initialized) {
        this.initialized = true;

        this.items.forEach((item) => (item.container.style.opacity = "1"));
      }
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    const img = document.querySelector(".featured-image img");
    if (!img) return;

    const renderer = new TitleRenderer(img);

    let rafPending = false;

    /**
     * Throttled render scheduling via requestAnimationFrame
     */
    const scheduleRender = () => {
      if (rafPending) return;

      rafPending = true;

      requestAnimationFrame(() => {
        renderer.render();
        rafPending = false;
      });
    };

    // React to size changes
    const resizeObserver = new ResizeObserver(scheduleRender);
    resizeObserver.observe(img);

    // Initial render triggers
    if (img.complete) scheduleRender();
    img.addEventListener("load", scheduleRender);

    // Ensure correct layout after fonts load
    if (document.fonts?.ready) {
      document.fonts.ready.then(scheduleRender);
    }
  });
})();
