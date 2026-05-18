import datetime
import logging
from typing import NamedTuple

import snakemd
import subete
from markdown.front_matter import generate_front_matter
from repo.queries import get_program_datetimes
from utils.plural import pluralize

log = logging.getLogger(__name__)


class RepoMetrics(NamedTuple):
    """Container for aggregated repository metadata metrics."""

    authors: set[str]
    times: list[datetime.datetime | None]
    num_articles: int


def generate_main_page(repo: subete.Repo) -> None:
    """Orchestrates the generation and export of the master documentation main page.

    Args:
        repo: The subete Repository instance to aggregate documentation metrics from.

    """
    log.info("Generating main page")

    metrics = _collect_repo_metrics(repo)

    main_page = snakemd.new_doc()
    generate_front_matter(
        main_page,
        "Sample Programs in Every Language",
        times=metrics.times,
    )

    articles_str = pluralize(metrics.num_articles, "article")
    authors_str = pluralize(len(metrics.authors), "author")

    main_page.add_paragraph(
        "Welcome to Sample Programs in Every Language, a collection of code snippets "
        "in as many languages as possible. Thanks for taking an interest in our collection "
        f"which currently contains {articles_str} written by {authors_str}.",
    )

    welcome_links_paragraph = _build_welcome_paragraph()
    main_page.add_paragraph(str(welcome_links_paragraph))

    try:
        main_page.dump("index", "docs")
    except Exception:
        log.exception("Failed to write docs/index")


def _collect_repo_metrics(repo: subete.Repo) -> RepoMetrics:
    """Aggregates times, unique author counts, and structural article metrics in a single pass."""
    authors: set[str] = set()
    times: list[datetime.datetime | None] = []
    num_articles = 0

    for language in repo:
        num_articles += 1
        authors |= language.doc_authors()
        times.extend([language.doc_created(), language.doc_modified()])

        for program in language:
            num_articles += 1
            authors |= program.authors() | program.doc_authors()
            times.extend(get_program_datetimes(program))

    for project in repo.approved_projects():
        num_articles += 1
        authors |= project.doc_authors()
        times.extend([project.doc_created(), project.doc_modified()])

    return RepoMetrics(authors=authors, times=times, num_articles=num_articles)


def _build_welcome_paragraph() -> snakemd.Paragraph:
    """Constructs and structures the complex collection of inline documentation links."""
    return snakemd.Paragraph(
        [
            snakemd.Inline(
                "If you'd like to contribute to this growing collection, check out our ",
            ),
            snakemd.Inline(
                "contributing document",
                link="https://github.com/TheRenegadeCoder/sample-programs/blob/master/.github/CONTRIBUTING.md",
            ),
            snakemd.Inline(
                " for more information. In addition, you can explore our documentation which is organized by ",
            ),
            snakemd.Inline("project", link="/projects"),
            snakemd.Inline(" and by "),
            snakemd.Inline("language", link="/languages"),
            snakemd.Inline(
                ". If you don't find what you're looking for, check out our list of related ",
            ),
            snakemd.Inline("open-source projects", link="/related"),
            snakemd.Inline(
                ". Finally, if code isn't your thing but you'd still like to help, there are plenty of other ways to ",
            ),
            snakemd.Inline(
                "support the project",
                link="https://therenegadecoder.com/updates/5-ways-you-can-support-the-renegade-coder/",
            ),
            snakemd.Inline("."),
        ],
    )
