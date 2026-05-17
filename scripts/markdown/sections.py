import logging
from pathlib import Path

import snakemd
from constants import *

log = logging.getLogger(__name__)


def add_section(
    doc: snakemd.Document,
    source: str,
    source_instance: str,
    section: str,
    level: int = 2,
) -> None:
    """Adds a section to the document.

    :param snakemd.Document doc: the document to add the section to.
    :param str source: the specific source folder to pull from (e.g., languages).
    :param str source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param str section: the section to add to the document (e.g., Description).
    """
    doc.add_heading(section, level=level)
    fp = Path(f"sources/{source}/{source_instance}/{section.lower().replace(' ', '-')}.md")
    if fp.exists():
        log.info(f"Adding {section} section to document from source, {fp}")
        doc.add_raw(fp.read_text(encoding="utf-8"))
    else:
        log.warning(f"Failed to find {section} in {fp}")
        doc.add_paragraph(
            f"No '{section}' section available. Please consider contributing.",
        ).insert_link(
            "Please consider contributing",
            "https://github.com/TheRenegadeCoder/sample-programs-website",
        )


def add_testing_section(doc: snakemd.Document, source: str, source_instance: str) -> None:
    valid_path = Path(f"sources/{source}/{source_instance}/valid-tests.md")
    invalid_path = Path(f"sources/{source}/{source_instance}/invalid-tests.md")
    auto_gen_path = Path(f"{AUTO_GEN_TEST_DOC_DIR}/{source_instance}/testing.md")
    if auto_gen_path.exists():
        add_section(
            doc,
            Path(AUTO_GEN_TEST_DOC_DIR).name,
            source_instance,
            "Testing",
            level=2,
        )
    elif valid_path.exists() and invalid_path.exists():
        doc.add_heading("Testing", level=2)
        doc.add_paragraph(
            f"""
                Every project in the Sample Programs repo should be tested. In this section,
                we specify the set of tests specific to {" ".join(source_instance.split("-")).title()}.
                To keep things simple, we split up testing into two subsets: valid and invalid.
                Valid tests refer to tests that occur under correct input conditions. Invalid
                tests refer to tests that occur on bad input (e.g., letters instead of numbers).
                """,
        )
        add_section(doc, source, source_instance, "Valid Tests", level=3)
        add_section(doc, source, source_instance, "Invalid Tests", level=3)
    else:
        add_section(doc, source, source_instance, "Testing", level=2)
