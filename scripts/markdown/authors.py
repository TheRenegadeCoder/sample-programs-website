import snakemd


def add_authors_to_doc(doc: snakemd.Document, authors: set[str]) -> None:
    """Add a sorted list of authors to a document.

    :param snakemd.Document doc: the document to add the list of authors to.
    :param authors: List of authors
    """
    doc.add_block(snakemd.MDList(sorted(authors, key=str.casefold)))
