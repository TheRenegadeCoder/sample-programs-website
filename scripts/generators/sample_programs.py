import datetime
import logging
import shutil
from pathlib import Path

import snakemd
import subete
from assets.images import get_program_image
from constants import PROGRAM_MD_FILENAMES
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section
from repo.queries import get_program_datetimes
from utils.text import markdown_escape

log = logging.getLogger(__name__)


def generate_sample_programs(repo: subete.Repo) -> None:
    """Creates the language folders in each project directory.

    :param subete.Repo repo: the repo to pull from.
    """
    for language in repo:
        language: subete.LanguageCollection
        for program in language:
            log.info("Generate sample programs for %s", str(program))
            program: subete.SampleProgram
            path = Path(
                f"docs/projects/{program.project_pathlike_name()}/{language.pathlike_name()}",
            )
            path.mkdir(exist_ok=True, parents=True)
            generate_sample_program_index(program, path)


def generate_sample_program_index(program: subete.SampleProgram, path: Path) -> None:
    """Creates a sample program documentation file.

    :param subete.SampleProgram program: the sample program to create the documentation for.
    :param pathlib.Path path: the path to the documentation file.
    """
    doc: snakemd.Document = snakemd.new_doc()
    root_path = Path(
        f"programs/{program.project_pathlike_name()}/{program.language_pathlike_name()}",
    )
    authors: set[str] = program.authors()
    doc_authors: set[str] = program.doc_authors()
    generate_front_matter(
        doc,
        str(program),
        times=get_program_datetimes(program),
        image=get_program_image(program),
        authors=authors | doc_authors,
        tags=[program.language_pathlike_name(), program.project_pathlike_name()],
    )
    generate_no_edit_note(
        doc,
        str(root_path.parent),
        program.language_pathlike_name(),
        PROGRAM_MD_FILENAMES,
    )

    project_name = program.project_name()
    language_escaped = markdown_escape(program.language_name())
    language_docs_url = program.language_collection().lang_docs_url()
    doc.add_block(
        snakemd.Paragraph(
            [
                "Welcome to the ",
                snakemd.Inline(project_name, link=program.project().requirements_url()),
                " in ",
                snakemd.Inline(language_escaped, link=language_docs_url),
                " page! Here, you'll find the source code for this program as well as a description ",
                "of how the program works.",
            ],
        ),
    )
    doc.add_heading("Current Solution", level=2)

    if program.image_type():
        image_dest = path / Path(program.project_path()).name
        shutil.copy(program.project_path(), image_dest)
        image_uri = "/" + "/".join(image_dest.parts[1:])
        doc.add_block(
            snakemd.Raw(
                f"""<img class="program-image" src="{image_uri}" alt="{program}">""",
            ),
        )
    else:
        doc.add_paragraph("{% raw %}")
        doc.add_code(program.code(), lang=language_escaped.lower().replace(" ", "_"))
        doc.add_paragraph("{% endraw %}")

    doc.add_block(
        snakemd.Paragraph(
            [
                f"{project_name} in ",
                snakemd.Inline(language_escaped, link=language_docs_url),
                " was written by:",
            ],
        ),
    )
    add_authors_to_doc(doc, authors)

    doc_authors: set[str] = program.doc_authors()
    if doc_authors:
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    doc.add_paragraph(
        "If you see anything you'd like to change or update, please consider contributing.",
    ).insert_link(
        "please consider contributing",
        "https://github.com/TheRenegadeCoder/sample-programs",
    )

    created_at: datetime.datetime | None = program.created()
    modified: datetime.datetime | None = program.modified()
    doc_modified: datetime.datetime | None = program.doc_modified()
    if (
        created_at
        and modified
        and created_at != modified
        and doc_modified
        and doc_modified < modified
    ):
        datetime_format = "%b %d %Y %H:%M:%S"
        doc.add_paragraph(
            "**Note**: The solution shown above is the current solution in the Sample "
            f"Programs repository as of {modified.strftime(datetime_format)}. "
            f"The solution was first committed on {created_at.strftime(datetime_format)}. "
            f"The documentation was last updated on {doc_modified.strftime(datetime_format)}. "
            "As a result, documentation below may be outdated.",
        )

    add_section(
        doc,
        str(root_path.parent),
        program.language_pathlike_name(),
        "How to Implement the Solution",
    )
    add_section(
        doc,
        str(root_path.parent),
        program.language_pathlike_name(),
        "How to Run the Solution",
    )
    try:
        doc.dump("index", directory=str(path))
    except Exception:
        log.exception(f"Failed to write {path}")
