// Previous image size
var prev_image_width = 0;
var prev_image_height = 0;

// Image titler constants
const ORIG_IMAGE_WIDTH = 1200;
const ORIG_IMAGE_HEIGHT = 628;
const TOP_RECTANGLE_Y = 20;
const X_OFFSET = TOP_RECTANGLE_Y;
const FONT = "Bernard HC";
const RECTANGLE_FILL = "#c90229";
const FONT_HEIGHTS = {
    12: 14, 13: 16, 14: 17, 15: 18, 16: 19, 17: 20, 18: 21, 19: 22,
    20: 23, 21: 25, 22: 26, 23: 27, 24: 28, 25: 29, 26: 30, 27: 31, 28: 32, 29: 34,
    30: 35, 31: 36, 32: 37, 33: 37, 34: 38, 35: 39, 36: 40, 37: 41, 38: 43, 39: 44,
    40: 45, 41: 46, 42: 47, 43: 48, 44: 49, 45: 50, 46: 52, 47: 53, 48: 54, 49: 55,
    50: 56, 51: 57, 52: 58, 53: 59, 54: 61, 55: 62, 56: 63, 57: 64, 58: 65, 59: 66,
    60: 67, 61: 68, 62: 69, 63: 71, 64: 72, 65: 73, 66: 73, 67: 74, 68: 75, 69: 76,
    70: 77, 71: 79, 72: 80, 73: 81, 74: 82, 75: 83, 76: 84, 77: 85, 78: 86, 79: 88,
    80: 89, 81: 90, 82: 91, 83: 92, 84: 93, 85: 94, 86: 95, 87: 97, 88: 98, 89: 99,
    90: 100, 91: 101, 92: 102, 93: 103, 94: 104, 95: 105, 96: 107, 97: 108, 98: 109, 99: 109
};

function image_titler() {
    // Current current image size
    const image = $(".featured-image img");
    const image_width = image.width();
    const image_height = image.height();

    // Exit if image size did not change
    if (image_width == prev_image_width && image_height == prev_image_height) {
        return;
    }

    console.log(`image_size = ${image_width}x${image_height}`);

    // Save image size
    prev_image_width = image_width;
    prev_image_height = image_height;

    // Draw image title
    const image_text = image.attr("alt");
    _draw_image_title(image_text, image_width, image_height);
}

function _draw_image_title(image_text, image_width, image_height) {
    // Get height of title bar
    const bar_height = _get_bar_height(image_height);

    // Get font size and font height
    const font_size = _get_appropriate_font_size(image_height);
    console.log(`font_size=${font_size}`);

    // Split up image text into individual lines around middle (if more than one word)
    const image_lines = _split_string_by_nearest_middle_space(image_text);

    // Calculate x- and y-offset and spacing between lines
    var x_offset = X_OFFSET * image_width / ORIG_IMAGE_WIDTH;
    var y_offset = TOP_RECTANGLE_Y * image_height / ORIG_IMAGE_HEIGHT;
    const y_spacing = y_offset;

    // For each image line
    var line_num = 1;
    for (var image_line of image_lines) {
        // Set top position for image container
        $(`#title${line_num}`).css("top", `${y_offset}px`);

        // Set styling and text for image title
        $(`#title${line_num} .image-title`).css(
            {
                "padding-left": `${x_offset}px`,
                "padding-right": `${x_offset}px`,
                "font-size": `${font_size}px`,
                "line-height": `${bar_height}px`
            }
        ).text(image_line);

        // Set up for next image line
        line_num += 1;
        y_offset += bar_height + y_spacing;
    }
}

function _get_appropriate_font_size(image_height) {
    // Successive try larger font size until proper size is found
    const text_height = (
        _get_bar_height(image_height) -
        Math.floor(TOP_RECTANGLE_Y * image_height / (2 * ORIG_IMAGE_HEIGHT))
    );
    var font_size;
    for (font_size in FONT_HEIGHTS) {
        if (FONT_HEIGHTS[font_size] >= text_height) {
            break;
        }
    }
    return font_size;
}

function _get_bar_height(image_height) {
    return Math.floor(image_height / 7);
}

function _split_string_by_nearest_middle_space(text) {
    if (text.split(" ").length < 2) {
        return [text]
    }

    var index = Math.floor(text.length / 2);
    var count = 1;
    var sign = 1;
    while (index >= 0 && index < text.length && text[index] != " ") {
        index += sign * count;
        count += 1;
        sign = -sign;
    }
    return [text.substring(0, index), text.substring(index + 1)];
}

// Run image titler under the following conditions:
// - Web page is ready
// - Image is loaded
// - Web page is resized
$(function() {
    image_titler();
    $(".featured-image img").on("load", image_titler);
    $(window).on("resize", image_titler);
});
