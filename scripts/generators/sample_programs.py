import logging
import shutil
from pathlib import Path

import snakemd
import subete
from assets.image_lookup import find_program_image
from constants import DOCS_PROJECTS_DIR, PROGRAM_MD_FILES
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section
from repo.queries import get_program_datetimes
from utils.files import mkdir
from utils.text import markdown_escape

log = logging.getLogger(__name__)

DATETIME_FORMAT = "%b %d %Y %H:%M:%S"


def generate_sample_programs(repo: subete.Repo) -> None:
    """Creates the language folders in each project directory.

    Args:
        repo: The subete Repository instance to pull data from.

    """
    for language in repo:
        for program in language:
            log.info("Generate sample programs for %s", program)

            project_dir = (
                DOCS_PROJECTS_DIR / program.project_pathlike_name() / language.pathlike_name()
            )
            target_path = mkdir(project_dir)

            generate_sample_program_index(program, target_path)


def generate_sample_program_index(program: subete.SampleProgram, path: Path) -> None:
    """Creates a sample program documentation file.

    Args:
        program: The sample program instance to document.
        path: The directory Path where the documentation index will be saved.

    """
    proj_path_name = program.project_pathlike_name()
    lang_path_name = program.language_pathlike_name()
    language_escaped = markdown_escape(program.language_name())
    language_docs_url = program.language_collection().lang_docs_url()

    program_root_str = str(Path("programs") / proj_path_name)
    doc = snakemd.new_doc()

    _add_front_matter_and_notes(doc, program, proj_path_name, lang_path_name, program_root_str)
    _add_welcome_paragraph(
        doc,
        program.project_name(),
        language_escaped,
        language_docs_url,
        program,
    )
    _add_solution_block(doc, program, path, language_escaped)
    _add_author_credits(doc, program, language_escaped, language_docs_url)
    _add_outdated_warning_if_needed(doc, program)

    add_section(doc, program_root_str, lang_path_name, "How to Implement the Solution")
    add_section(doc, program_root_str, lang_path_name, "How to Run the Solution")

    try:
        doc.dump("index", directory=str(path))
    except Exception:
        log.exception("Failed to write %s", path)


def _add_front_matter_and_notes(
    doc: snakemd.Document,
    program: subete.SampleProgram,
    proj_path_name: str,
    lang_path_name: str,
    program_root_str: str,
) -> None:
    """Generates the metadata front matter block and the non-editable note warning."""
    generate_front_matter(
        doc,
        str(program),
        times=get_program_datetimes(program),
        image=find_program_image(program),
        authors=program.authors() | program.doc_authors(),
        tags=[lang_path_name, proj_path_name],
    )

    generate_no_edit_note(
        doc,
        program_root_str,
        lang_path_name,
        list(PROGRAM_MD_FILES),
    )


def _add_welcome_paragraph(
    doc: snakemd.Document,
    project_name: str,
    language_escaped: str,
    language_docs_url: str,
    program: subete.SampleProgram,
) -> None:
    """Appends the standard introductory paragraph and main header."""
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


def _add_solution_block(
    doc: snakemd.Document,
    program: subete.SampleProgram,
    path: Path,
    language_escaped: str,
) -> None:
    """Renders either an embedded image asset or a raw source code logic block safely."""
    VALID_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

    project_path = Path(program.project_path())

    if program.image_type() and project_path.suffix.lower() in VALID_IMAGE_EXTENSIONS:
        image_dest = path / project_path.name
        shutil.copy(project_path, image_dest)

        image_uri = "/" + "/".join(image_dest.parts[1:])
        doc.add_block(
            snakemd.Raw(f'<img class="program-image" src="{image_uri}" alt="{program}">'),
        )
    else:
        doc.add_paragraph("{% raw %}")
        doc.add_code(
            program.code(),
            lang=language_escaped.lower().replace(" ", "_"),
        )
        doc.add_paragraph("{% endraw %}")


def _add_author_credits(
    doc: snakemd.Document,
    program: subete.SampleProgram,
    language_escaped: str,
    language_docs_url: str,
) -> None:
    """Builds lists detailing code implementation authors vs documentation contributors."""
    authors = program.authors()
    doc_authors = program.doc_authors()

    doc.add_block(
        snakemd.Paragraph(
            [
                f"{program.project_name()} in ",
                snakemd.Inline(language_escaped, link=language_docs_url),
                " was written by:",
            ],
        ),
    )
    add_authors_to_doc(doc, authors)

    if doc_authors:
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    doc.add_paragraph(
        "If you see anything you'd like to change or update, please consider contributing.",
    ).insert_link(
        "please consider contributing",
        "https://github.com/TheRenegadeCoder/sample-programs",
    )


def _add_outdated_warning_if_needed(doc: snakemd.Document, program: subete.SampleProgram) -> None:
    """Appends an outdated documentation warning block if chronological mismatches exist."""
    created_at = program.created()
    modified = program.modified()
    doc_modified = program.doc_modified()

    if (
        created_at
        and modified
        and doc_modified
        and (created_at != modified)
        and (doc_modified < modified)
    ):
        doc.add_paragraph(
            "**Note**: The solution shown above is the current solution in the Sample "
            f"Programs repository as of {modified.strftime(DATETIME_FORMAT)}. "
            f"The solution was first committed on {created_at.strftime(DATETIME_FORMAT)}. "
            f"The documentation was last updated on {doc_modified.strftime(DATETIME_FORMAT)}. "
            "As a result, documentation below may be outdated.",
        )
