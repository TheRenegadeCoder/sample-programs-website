import contextlib
import logging
from pathlib import Path

import glotter
import subete
from constants import GENERATED_DIR

log = logging.getLogger(__name__)


def generate_auto_gen_test_docs(repo: subete.Repo) -> None:
    """Generates automated test documentation using Glotter.

    Args:
        repo: The subete Repository instance to pull information from.

    """
    log.info("Generating test documentation")

    doc_dir = GENERATED_DIR.resolve()
    repo_dir = Path(repo.sample_programs_repo_dir())

    # Safely switch directories. The context manager guarantees the original
    # working directory is restored even if an exception occurs inside the block.
    with contextlib.chdir(repo_dir):
        glotter.generate_test_docs(
            doc_dir=doc_dir,
            repo_name="Sample Programs",
            repo_url="https://github.com/TheRenegadeCoder/sample-programs",
        )
