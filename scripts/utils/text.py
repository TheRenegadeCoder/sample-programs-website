def markdown_escape(text: str) -> str:
    """Escape Markdown special characters in text.

    Args:
        text: Input string.

    Returns:
        Escaped string safe for Markdown rendering.

    """
    return text.replace("\\", "\\\\").replace("*", r"\*").replace("_", r"\_").replace("`", r"\`")


def split_text(text: str) -> tuple[str, str]:
    """Split text into two parts at a space nearest the midpoint.

    The algorithm searches outward from the center of the string and selects
    the first whitespace character encountered. If two candidates are equally
    distant from the midpoint, the right-side split is preferred.

    Args:
        text: Input string to split.

    Returns:
        A tuple (left, right) where:
            - left is the substring before the split point
            - right is the substring after the split point

        If no whitespace is found, returns (text, "").

    """
    mid = len(text) // 2

    # expand outward from middle
    for offset in range(len(text)):
        right = mid + offset
        left = mid - offset

        # check RIGHT first (tie preference)
        if right < len(text) and text[right].isspace():
            return text[:right], text[right + 1 :]

        # then LEFT
        if left >= 0 and text[left].isspace():
            return text[:left], text[left + 1 :]

    return text, ""
