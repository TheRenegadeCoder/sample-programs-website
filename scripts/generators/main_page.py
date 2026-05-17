import datetime
import logging

import snakemd
import subete
from markdown.front_matter import generate_front_matter
from repo.queries import get_program_datetimes

log = logging.getLogger(__name__)


def generate_main_page(repo: subete.Repo) -> None:
    """Generate the main page.

    :param subete.Repo repo: the repo to pull from.
    """
    authors: set[str] = set()
    times: list[datetime.datetime | None] = []
    num_articles = 0
    for language in repo:
        language: subete.LanguageCollection
        num_articles += 1  # 1 article per language
        authors |= language.doc_authors()
        times += [language.doc_created(), language.doc_modified()]
        program: subete.SampleProgram
        for program in language:
            authors |= program.authors() | program.doc_authors()
            times += get_program_datetimes(program)

            num_articles += 1  # 1 article per sample program

    for project in repo.approved_projects():
        num_articles += 1  # 1 article per approved project
        project: subete.Project
        authors |= project.doc_authors()
        times += [project.doc_created(), project.doc_modified()]

    log.info("Generating main page")
    main_page: snakemd.Document = snakemd.new_doc()
    generate_front_matter(
        main_page,
        "Sample Programs in Every Language",
        times=times,
    )
    main_page.add_paragraph(
        "Welcome to Sample Programs in Every Language, a collection of code snippets "
        "in as many languages as possible. Thanks for taking an interest in our collection "
        f"which currently contains {num_articles} articles written by {len(authors)} authors.",
    )
    paragraph = snakemd.Paragraph(
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
                ". If you don't find what you're look for, check out our list of related ",
            ),
            snakemd.Inline("open-source projects", link="/related"),
            snakemd.Inline(
                ". Finally, if code isn't your thing but you'd still like to help, there are plenty "
                "of other ways to ",
            ),
            snakemd.Inline(
                "support the project",
                link="https://therenegadecoder.com/updates/5-ways-you-can-support-the-renegade-coder/",
            ),
            snakemd.Inline("."),
        ],
    )
    main_page.add_paragraph(str(paragraph))
    try:
        main_page.dump("index", "docs")
    except Exception:
        log.exception("Failed to write docs/index")
