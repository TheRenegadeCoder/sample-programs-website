def markdown_escape(s: str) -> str:
    return s.replace("*", r"\*")


def split_text(text: str) -> tuple[str, str]:
    mid = len(text) // 2
    best_index = -1
    min_dist = float("inf")

    for i, char in enumerate(text):
        if char.isspace():
            dist = abs(i - mid)
            if dist <= min_dist:
                min_dist = dist
                best_index = i
            elif i > mid:
                # Optimization: if we are past mid and distance is increasing, stop
                break

    if best_index == -1:
        return text, ""

    return text[:best_index], text[best_index + 1 :]
