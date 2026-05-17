import logging

import snakemd
import subete
from utils.plural import is_are, pluralize
from utils.text import markdown_escape

log = logging.getLogger(__name__)


def add_project_article_section(
    doc: snakemd.Document,
    repo: subete.Repo,
    project: subete.Project,
) -> None:
    """Generates a list of articles for each project page.

    :param snakemd.Document doc: the document to add the section to.
    :param subete.Repo repo: the repo to pull from.
    :param subete.Project project: the project to add to the document.
    """
    log.info(f"Generating article section of {project}")
    doc.add_heading("Articles", level=2)
    articles = []
    for lang in repo:
        try:
            program: subete.SampleProgram = lang[project.name()]
        except KeyError:
            continue

        program_escaped = markdown_escape(str(program))
        link = snakemd.Inline(
            program_escaped,
            link=program.documentation_url(),
        )
        articles.append(link)

    num_articles = len(articles)
    if num_articles > 0:
        verb = is_are(num_articles)
        word = pluralize(num_articles, "article")
        doc.add_paragraph(f"There {verb} {num_articles} {word}:")
        doc.add_block(snakemd.MDList(articles))
    else:
        log.warning(f"Failed to find any articles for {project}")
        doc.add_paragraph(
            "No articles available. Please consider contributing.",
        ).insert_link(
            "Please consider contributing",
            "https://github.com/TheRenegadeCoder/sample-programs-website",
        )


def add_language_article_section(doc: snakemd.Document, repo: subete.Repo, language: str) -> None:
    """Generates a list of articles for each language page.

    :param snakemd.Document doc: the document to add the section to.
    :param subete.Repo repo: the repo to pull from.
    :param str language: the language to add to the document in its lookup form (e.g., Python).
    """
    doc.add_heading("Articles", level=2)
    num_articles = len(list(repo[language]))
    verb = is_are(num_articles)
    word = pluralize(num_articles, "article")
    doc.add_paragraph(f"There {verb} {num_articles} {word}:")

    articles = []
    for program in repo[language]:
        program_escaped = markdown_escape(str(program))
        link = snakemd.Inline(
            program_escaped,
            link=program._sample_program_doc_url,
        )
        articles.append(link)
    doc.add_block(snakemd.MDList(articles))
