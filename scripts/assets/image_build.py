import logging
import shutil
import subprocess
import tempfile
from pathlib import Path

import subete
from constants import (
    DEFAULT_LANGUAGE_IMAGE_NO_EXT,
    DEFAULT_PROGRAM_IMAGE_NO_EXT,
    DEFAULT_PROJECT_IMAGE_NO_EXT,
)

log = logging.getLogger(__name__)


def generate_images(repo: subete.Repo) -> int:
    """Use image-titler to resize and crop images and add logo

    :param subete.Repo repo: the repo to pull from.
    :return: 0 if no error, non-zero otherwise
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        status_code = 0
        status_code = generate_language_images(repo, temp_dir, status_code)
        status_code = generate_project_images(repo, temp_dir, status_code)
        status_code = generate_program_images(repo, temp_dir, status_code)
    return status_code


def generate_language_images(repo: subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = generate_image(
        temp_dir,
        "sources/languages",
        DEFAULT_LANGUAGE_IMAGE_NO_EXT,
        status_code,
    )
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        status_code = generate_image(
            temp_dir,
            f"sources/languages/{language_path}",
            f"the-{language_path}-programming-language",
            status_code,
        )

    return status_code


def generate_project_images(repo: subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = generate_image(
        temp_dir,
        "sources/projects",
        DEFAULT_PROJECT_IMAGE_NO_EXT,
        status_code,
    )
    for project in repo.approved_projects():
        project_path = project.pathlike_name()
        status_code = generate_image(
            temp_dir,
            f"sources/projects/{project_path}",
            f"{project_path}-in-every-language",
            status_code,
        )

    return status_code


def generate_program_images(repo: subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = generate_image(
        temp_dir,
        "sources",
        DEFAULT_PROGRAM_IMAGE_NO_EXT,
        status_code,
    )
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        program: subete.SampleProgram
        for program in repo[str(language)]:
            program_path = program.project_pathlike_name()
            status_code = generate_image(
                temp_dir,
                f"sources/programs/{program_path}/{language_path}",
                f"{program_path}-in-{language_path}",
                status_code,
            )

    return status_code


def generate_image(temp_dir: str, src: str, dest_filename_no_ext: str, status_code: int) -> int:
    src_image_path = next(Path(src).glob("featured-image.*"), None)
    if not src_image_path:
        return status_code

    dest = Path("docs/assets/images")
    logo = str(dest / "icon-small.png")

    dest_image_path = dest / f"{dest_filename_no_ext}{src_image_path.suffix}"
    log.info("Processing %s -> %s", str(src_image_path), str(dest_image_path))
    try:
        subprocess.run(
            [
                "image-titler",
                "--path",
                str(src_image_path),
                "--output",
                temp_dir,
                "--logo",
                logo,
                "--no_title",
            ],
            check=True,
        )
        temp_image_path = next(Path(temp_dir).iterdir())
        shutil.move(temp_image_path, dest_image_path)
    except subprocess.CalledProcessError as exc:
        log.error("image-titler exited with %d status", exc.returncode)
        status_code = 1

    return status_code
