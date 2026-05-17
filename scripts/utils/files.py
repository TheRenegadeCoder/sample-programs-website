from pathlib import Path


def clean(folder: str | Path) -> None:
    """Deletes the contents of the docs directory."""
    path = Path(folder)
    if path.exists():
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                clean(child)
        path.rmdir()
