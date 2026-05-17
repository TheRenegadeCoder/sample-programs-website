import logging
import os
import shutil
from pathlib import Path

import subete
from subete import imghdr

log = logging.getLogger(__name__)


def copy_article_images(repo: subete.Repo) -> None:
    """Copy article images to the appropriate directory

    :param subete.Repo repo: the repo to pull from.
    """
    copy_language_images(repo)
    copy_project_images(repo)
    copy_program_images(repo)


def copy_language_images(repo: subete.Repo) -> None:
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        copy_image(
            f"sources/languages/{language_path}",
            f"docs/assets/images/languages/{language_path}",
        )


def copy_project_images(repo: subete.Repo) -> None:
    project: subete.Project
    for project in repo.approved_projects():
        project_path = project.pathlike_name()
        copy_image(
            f"sources/projects/{project_path}",
            f"docs/assets/images/projects/{project_path}",
        )


def copy_program_images(repo: subete.Repo) -> None:
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        program: subete.SampleProgram
        for program in repo[str(language)]:
            project_path = program.project_pathlike_name()
            copy_image(
                f"sources/programs/{project_path}/{language_path}",
                f"docs/assets/images/projects/{project_path}/{language_path}",
            )


def copy_image(src_dir: str, dest_dir: str) -> None:
    src_dir_path = Path(src_dir)
    dest_dir_path = Path(dest_dir)
    if not src_dir_path.exists():
        return

    src_image_paths = [
        path
        for path in src_dir_path.iterdir()
        if path.is_file() and path.stem != "featured-image" and imghdr.what(path)
    ]
    if src_image_paths:
        os.makedirs(dest_dir, exist_ok=True)
        for src_image_path in src_image_paths:
            dest_image_path = dest_dir_path / src_image_path.name
            log.info("Copying image %s -> %s", str(src_image_path), str(dest_image_path))
            shutil.copy(src_image_path, dest_image_path)
