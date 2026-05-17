import logging
import os
from pathlib import Path

import glotter
import subete
from constants import AUTO_GEN_TEST_DOC_DIR

log = logging.getLogger(__name__)


def generate_auto_gen_test_docs(repo: subete.Repo) -> None:
    """Generate auto-generated test documentation

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating test documentation")
    curr_dir = os.getcwd()
    doc_dir = Path(AUTO_GEN_TEST_DOC_DIR).absolute()
    os.chdir(repo.sample_programs_repo_dir())
    glotter.generate_test_docs(
        doc_dir=doc_dir,
        repo_name="Sample Programs",
        repo_url="https://github.com/TheRenegadeCoder/sample-programs",
    )
    os.chdir(curr_dir)
