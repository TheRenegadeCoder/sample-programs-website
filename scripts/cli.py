import argparse
import logging
import sys

import subete
from assets.image_build import generate_images
from assets.image_copy import copy_article_images
from constants import AUTO_GEN_TEST_DOC_DIR
from generators.languages import generate_language_paths, generate_languages_index
from generators.main_page import generate_main_page
from generators.projects import generate_project_paths, generate_projects_index
from generators.sample_programs import generate_sample_programs
from generators.tests import generate_auto_gen_test_docs
from logging_setup import setup_logging
from utils.files import clean

log = logging.getLogger("automate")


def main() -> None:
    setup_logging()
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", "-l", action="store_true", help="Use local contents of website")
    parsed_args = parser.parse_args()

    clean("docs/projects")
    clean("docs/languages")
    clean(AUTO_GEN_TEST_DOC_DIR)

    log.info("Loading repos (this may take several minutes)")
    website_repo_dir = "." if parsed_args.local else None
    repo = subete.load(sample_programs_website_repo_dir=website_repo_dir)
    repo.set_additional_language_colors("additional-language-colors.yml")

    generate_main_page(repo)
    generate_language_paths(repo)
    generate_auto_gen_test_docs(repo)
    generate_project_paths(repo)
    generate_sample_programs(repo)
    generate_languages_index(repo)
    generate_projects_index(repo)
    copy_article_images(repo)
    status_code = generate_images(repo)
    sys.exit(status_code)
