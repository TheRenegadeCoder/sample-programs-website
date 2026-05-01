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
   * Splits a string into two visually balanced lines.
   * Strategy:
   * - Find midpoint
   * - Try nearest space to split at word boundary
   * - Fallback to midpoint if needed
   */
  function splitText(text) {
    if (!text) return [""];

    const midpoint = (text.length / 2) | 0;

    const leftSpace = text.lastIndexOf(" ", midpoint);
    const rightSpace = text.indexOf(" ", midpoint);

    // If no spaces exist, don't split
    if (leftSpace === -1 && rightSpace === -1) {
      return [text];
    }

    let splitIndex;
    if (leftSpace === -1) {
      splitIndex = rightSpace;
    } else if (rightSpace === -1) {
      splitIndex = leftSpace;
    }
    // Check whether the midpoint is closer to the left side than the right side
    else if (midpoint - leftSpace <= rightSpace - midpoint) {
      splitIndex = leftSpace;
    } else {
      splitIndex = rightSpace;
    }

    return [
      text.slice(0, splitIndex).trim(),
      text.slice(splitIndex + 1).trim(),
    ];
  }

  /**
   * Computes layout metrics for each text line based on image size.
   * Everything scales proportionally from original design dimensions.
   */
  function computeLayout({ width, height, text }) {
    const lines = splitText(text);

    // Height of each title bar section
    const barHeight = Math.floor(height / CONFIG.BAR_HEIGHT_RATIO);

    // Derived font size with clamping
    const fontSizeRaw = (11 * barHeight) / 12 - 1.25;
    const fontSize = Math.max(
      CONFIG.MIN_FONT,
      Math.min(CONFIG.MAX_FONT, fontSizeRaw | 0),
    );

    // Horizontal padding scales with image width
    const paddingX = (CONFIG.X_SIDE_OFFSET * width) / CONFIG.ORIGINAL_WIDTH;

    // // Vertical offset scales with image height
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

      // Grab title containers (title1, title2, ...)
      this.containers = Array.from({ length: CONFIG.TITLES }, (_, i) =>
        document.getElementById(`title${i + 1}`),
      ).filter(Boolean);

      this.lastWidth = 0;
      this.lastHeight = 0;
      this.initialized = false;
    }

    /**
     * Recalculate layout only when image size changes.
     * Updates DOM efficiently.
     */
    render() {
      const width = this.img.clientWidth;
      const height = this.img.clientHeight;

      // Skip invalid or unchanged frames
      if (width === 0) return;
      if (
        Math.abs(width - this.lastWidth) < 1 &&
        Math.abs(height - this.lastHeight) < 1
      ) {
        return;
      }

      this.lastWidth = width;
      this.lastHeight = height;

      const layout = computeLayout({
        width: width,
        height: height,
        text: this.img.alt || "",
      });

      // Apply computed layout to each title container
      for (let i = 0; i < this.containers.length; i++) {
        const container = this.containers[i];
        const block = layout[i];

        if (!container || !block) continue;

        const titleEl = container.querySelector(".image-title");
        if (!titleEl) continue;

        // Position container vertically
        container.style.top = `${block.top}px`;

        // Batch these text/font updates
        titleEl.style.fontSize = `${block.fontSize}px`;
        titleEl.style.lineHeight = `${block.lineHeight}px`;
        titleEl.style.paddingLeft = `${block.paddingX}px`;
        titleEl.style.paddingRight = `${block.paddingX}px`;

        // Update text only if changed (avoids layout thrash)
        if (titleEl.textContent !== block.text) {
          titleEl.textContent = block.text;
        }
      }

      // First-time reveal
      if (!this.initialized) {
        this.initialized = true;
        for (let i = 0; i < this.containers.length; i++) {
          this.containers[i].style.opacity = "1";
        }
      }
    }
  }

  /**
   * Entry point:
   * - Wait for DOM
   * - Attach ResizeObserver
   * - Sync with font loading and image load events
   */
  document.addEventListener("DOMContentLoaded", () => {
    const img = document.querySelector(".featured-image img");
    if (!img) return;

    const renderer = new TitleRenderer(img);

    let rafPending = false;

    // Throttle rendering via requestAnimationFrame
    const scheduleRender = () => {
      if (rafPending) return;

      rafPending = true;
      requestAnimationFrame(() => {
        renderer.render();
        rafPending = false;
      });
    };

    // React to size changes
    const observer = new ResizeObserver(scheduleRender);
    observer.observe(img);

    // Initial render triggers
    if (img.complete) scheduleRender();
    img.addEventListener("load", scheduleRender);

    // Ensure correct layout after fonts are ready
    if (document.fonts) {
      document.fonts.ready.then(scheduleRender);
    }
  });
})();
