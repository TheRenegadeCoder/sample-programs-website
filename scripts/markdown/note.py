import snakemd
from constants import AUTO_GEN_NOTE, CONTRIBUTING_NOTE


def generate_no_edit_note(
    doc: snakemd.Document,
    source: str,
    source_instance: str,
    filenames: list[str],
) -> None:
    """Generates an embedded raw HTML comment warning against manual edits.

    Args:
        doc: The snakemd Document instance to add the note to.
        source: The specific source folder category (e.g., "languages").
        source_instance: The specific folder sub-instance (e.g., "c-plus-plus").
        filenames: A list of structural markdown filenames to track.

    """
    note_filenames = "\n".join(
        f"- sources/{source}/{source_instance}/{filename}" for filename in filenames
    )

    note = (
        f"<!--\n"
        f"{AUTO_GEN_NOTE}\n\n"
        f"Instead, please edit the following:\n\n"
        f"{note_filenames}\n\n"
        f"{CONTRIBUTING_NOTE}\n"
        f"-->"
    )

    doc.add_raw(note)
