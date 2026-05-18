import datetime
import logging
from collections.abc import Iterable

import snakemd
import yaml
from utils.text import split_text

log = logging.getLogger(__name__)


def generate_front_matter(
    doc: snakemd.Document,
    title: str,
    times: Iterable[datetime.datetime | None] | None = None,
    image: str | None = None,
    authors: Iterable[str] | None = None,
    tags: Iterable[str] | None = None,
) -> None:
    """Generates YAML front matter block and appends it to the SnakeMD document.

    Args:
        doc: The snakemd Document instance to add the front matter to.
        title: The master title text string of the document page.
        times: An optional sequence of datetime markers used to derive
            creation and modification thresholds.
        image: Optional asset path filename for the page's featured banner image.
        authors: An optional collection of authors to sort and embed.
        tags: An optional collection of category tags to sort and embed.

    """
    top_title, bottom_title = split_text(title)

    front_matter: dict[str, object] = {
        "title": title,
        "title1": top_title,
        "title2": bottom_title,
        "layout": "default",
    }

    if times and (filtered_times := [t for t in times if t is not None]):
        sorted_times = sorted(filtered_times)
        front_matter["date"] = sorted_times[0].date()
        front_matter["last-modified"] = sorted_times[-1].date()

    if image:
        front_matter["featured-image"] = image

    if authors:
        front_matter["authors"] = sorted(authors, key=str.casefold)

    if tags:
        front_matter["tags"] = sorted(tags, key=str.casefold)

    try:
        yaml_block = yaml.safe_dump(
            front_matter,
            sort_keys=True,
            allow_unicode=True,
            default_flow_style=False,
        )
        doc.add_raw(f"---\n{yaml_block}---")
    except Exception:
        log.exception("Failed to safely serialize or dump Markdown front matter metadata block.")
