import logging

import snakemd
from constants import GENERATED_DIR, SOURCE_DIR

log = logging.getLogger(__name__)


def add_section(
    doc: snakemd.Document,
    source: str,
    source_instance: str,
    section: str,
    level: int = 2,
) -> None:
    """Adds a heading and file contents (or a fallback message) to the document.

    Args:
        doc: The snakemd Document instance to modify.
        source: The top-level source folder name (e.g., "languages").
        source_instance: The sub-folder instance name (e.g., "c-plus-plus").
        section: The section title name to append (e.g., "Description").
        level: The Markdown heading depth level. Defaults to 2.

    """
    doc.add_heading(section, level=level)

    filename = f"{section.lower().replace(' ', '-')}.md"
    file_path = SOURCE_DIR / source / source_instance / filename

    if file_path.exists():
        log.info("Adding %s section to document from source: %s", section, file_path)
        doc.add_raw(file_path.read_text(encoding="utf-8"))
    else:
        log.warning("Failed to find %s in %s", section, file_path)
        paragraph = doc.add_paragraph(
            f"No '{section}' section available. Please consider contributing.",
        )
        paragraph.insert_link(
            "Please consider contributing",
            "https://github.com/TheRenegadeCoder/sample-programs-website",
        )


def add_testing_section(doc: snakemd.Document, source: str, source_instance: str) -> None:
    """Appends a contextual testing section based on file availability.

    Args:
        doc: The snakemd Document instance to modify.
        source: The source directory context (e.g., "projects").
        source_instance: The specific project/language target (e.g., "hello-world").

    """
    instance_path = SOURCE_DIR / source / source_instance
    valid_path = instance_path / "valid-tests.md"
    invalid_path = instance_path / "invalid-tests.md"

    auto_gen_base = GENERATED_DIR
    auto_gen_path = auto_gen_base / source_instance / "testing.md"

    if auto_gen_path.exists():
        add_section(
            doc,
            source=auto_gen_base.name,
            source_instance=source_instance,
            section="Testing",
            level=2,
        )
    elif valid_path.exists() and invalid_path.exists():
        doc.add_heading("Testing", level=2)

        display_name = source_instance.replace("-", " ").title()

        doc.add_paragraph(
            "Every project in the Sample Programs repo should be tested. In this section, "
            f"we specify the set of tests specific to {display_name}. "
            "To keep things simple, we split up testing into two subsets: valid and invalid. "
            "Valid tests refer to tests that occur under correct input conditions. Invalid "
            "tests refer to tests that occur on bad input (e.g., letters instead of numbers).",
        )
        add_section(doc, source, source_instance, "Valid Tests", level=3)
        add_section(doc, source, source_instance, "Invalid Tests", level=3)
    else:
        add_section(doc, source, source_instance, "Testing", level=2)
