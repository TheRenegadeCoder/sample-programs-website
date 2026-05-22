import logging
import os
from pathlib import Path

import glotter
import subete
from constants import GENERATED_DIR

log = logging.getLogger(__name__)

from contextlib import AbstractContextManager


class chdir(AbstractContextManager):
    """Non-thread-safe context manager to change the current working directory."""

    def __init__(self, path) -> None:
        self.path = path
        self._old_cwd = []

    def __enter__(self) -> None:
        self._old_cwd.append(os.getcwd())
        os.chdir(self.path)

    def __exit__(self, *excinfo) -> None:
        os.chdir(self._old_cwd.pop())


def generate_auto_gen_test_docs(repo: subete.Repo) -> None:
    """Generates automated test documentation using Glotter.

    Args:
        repo: The subete Repository instance to pull information from.

    """
    log.info("Generating test documentation")

    doc_dir = GENERATED_DIR.resolve()
    repo_dir = Path(repo.sample_programs_repo_dir())

    with chdir(repo_dir):
        glotter.generate_test_docs(
            doc_dir=doc_dir,
            repo_name="Sample Programs",
            repo_url="https://github.com/TheRenegadeCoder/sample-programs",
        )
