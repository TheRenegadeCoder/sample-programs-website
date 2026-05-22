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

    Args:
        doc: The document to add the section to.
        repo: The subete Repo instance to pull from.
        project: The target subete Project to find associated language articles for.

    """
    log.info("Generating article section of %s", project)
    doc.add_heading("Articles", level=2)

    articles = []
    project_name = project.name()

    for lang in repo:
        try:
            program = lang[project_name]
        except KeyError:
            continue

        program_escaped = markdown_escape(str(program))
        articles.append(
            snakemd.Inline(
                program_escaped,
                link=program.documentation_url(),
            ),
        )

    if num_articles := len(articles):
        verb = is_are(num_articles)
        doc.add_paragraph(f"There {verb} {pluralize(num_articles, 'article')}:")
        doc.add_block(snakemd.MDList(articles))
    else:
        log.warning("Failed to find any articles for %s", project)
        paragraph = doc.add_paragraph("No articles available. Please consider contributing.")
        paragraph.insert_link(
            "Please consider contributing",
            "https://github.com/TheRenegadeCoder/sample-programs-website",
        )


def add_language_article_section(doc: snakemd.Document, repo: subete.Repo, language: str) -> None:
    """Generates a list of articles for each language page.

    Args:
        doc: The document to add the section to.
        repo: The subete Repo instance to pull from.
        language: The exact lookup string representation of the targeted language (e.g., "Python").

    """
    doc.add_heading("Articles", level=2)

    articles = [
        snakemd.Inline(
            markdown_escape(str(program)),
            link=program.documentation_url(),
        )
        for program in repo[language]
    ]

    num_articles = len(articles)
    verb = is_are(num_articles)

    doc.add_paragraph(f"There {verb} {pluralize(num_articles, 'article')}:")
    doc.add_block(snakemd.MDList(articles))
