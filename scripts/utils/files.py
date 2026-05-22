import shutil
from pathlib import Path


def mkdir(path: str | Path, *, exist_ok: bool = True) -> Path:
    """Create a directory (including parents if needed).

    Args:
        path: Directory to create.
        exist_ok: If True, ignores existing directories.

    Returns:
        Path object of the created directory.

    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=exist_ok)
    return p


def clean(folder: str | Path) -> None:
    """Remove all contents of a folder recursively.

    Args:
        folder: Directory to clear.

    Raises:
        FileNotFoundError: If the folder does not exist.
        PermissionError: If files cannot be removed.

    """
    path = Path(folder)

    if path.exists():
        shutil.rmtree(path)

    mkdir(path)
