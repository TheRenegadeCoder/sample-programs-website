import datetime
from collections.abc import Iterable

import snakemd
import yaml
from utils.text import split_text


def generate_front_matter(
    doc: snakemd.Document,
    title: str,
    times: list[datetime.datetime | None] | None = None,
    image: str | None = None,
    authors: set[str] | None = None,
    tags: Iterable[str] | None = None,
) -> None:
    """Generates front matter and adds it to the document.

    :param snakemd.Document doc: the document to add the front matter to.
    :param str title: the title of the document.
    :param Optional[List[Optional[datetime.datetime]]] times: optional list of
        date/times that may be `None`.
    :param str image: optional filename of the image.
    :param Set[str] authors: optional list of authors
    :param Iterable[str] tags: optional list of tags
    """
    top_title, bottom_title = split_text(title)

    front_matter: dict[str, object] = {
        "title": title,
        "title1": top_title,
        "title2": bottom_title,
        "layout": "default",
    }

    filtered_times = list(filter(None, times or []))
    if filtered_times:
        front_matter["date"] = min(filtered_times).date()
        front_matter["last-modified"] = max(filtered_times).date()

    if image:
        front_matter["featured-image"] = image

    if authors:
        front_matter["authors"] = sorted(authors, key=str.casefold)

    if tags:
        front_matter["tags"] = sorted(tags, key=str.casefold)

    yaml_block = yaml.safe_dump(front_matter, sort_keys=True, allow_unicode=True)
    doc.add_raw(f"---\n{yaml_block}---")
