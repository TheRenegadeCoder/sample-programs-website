import snakemd
from constants import AUTO_GEN_NOTE, CONTRIBUTING_NOTE


def generate_no_edit_note(
    doc: snakemd.Document,
    source: str,
    source_instance: str,
    filenames: list[str],
) -> None:
    """Generates "DO NOT EDIT" note

    :param snakemd.Document doc: the document to add the note to.
    :param str source: the specific source folder to pull from (e.g., languages).
    :param str source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param list[str] filenames: the markdown filenames
    """
    note_filenames = "\n".join(
        f"- sources/{source}/{source_instance}/{filename}" for filename in filenames
    )
    note = f"""\
<!--
{AUTO_GEN_NOTE}

Instead, please edit the following:

{note_filenames}

{CONTRIBUTING_NOTE}
-->"""
    doc.add_raw(note)
