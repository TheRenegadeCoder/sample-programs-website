import functools
import logging
import os
import pathlib
import shutil
import subprocess
import tempfile

import subete
from constants import (
    DEFAULT_LANGUAGE_IMAGE_NO_EXT,
    DEFAULT_PROGRAM_IMAGE_NO_EXT,
    DEFAULT_PROJECT_IMAGE_NO_EXT,
)
from subete import imghdr

log = logging.getLogger(__name__)


def get_program_image(program: subete.SampleProgram) -> str | None:
    """Gets the filename of the image for a sample program

    :param subete.SampleProgram program: the sample program to get the image for.
    :return: Filename of image if found, None otherwise.
    """
    project_path = program.project_pathlike_name()
    language_path = program.language_pathlike_name()
    image_path = pathlib.Path(f"sources/programs/{project_path}/{language_path}")
    return get_image(
        image_path,
        f"{project_path}-in-{language_path}",
        get_project_image(program.project()),
    )


@functools.lru_cache
def get_project_image(project: subete.Project) -> str | None:
    """Gets the filename of the image for a project

    :param subete.Project project: the project to create the index file
        for in the normalized form (e.g., hello-world).
    :return: Filename of image if found, None otherwise.
    """
    project_path = project.pathlike_name()
    image_path = pathlib.Path(f"sources/projects/{project_path}")
    return get_image(
        image_path,
        f"{project_path}-in-every-language",
        get_default_project_image(),
    )


@functools.lru_cache
def get_default_project_image() -> str | None:
    """Gets the filename of the default project image

    :return: Filename of image if found, None otherwise
    """
    return get_image(pathlib.Path("sources/projects"), DEFAULT_PROJECT_IMAGE_NO_EXT)


@functools.lru_cache
def get_image(
    image_path: pathlib.Path,
    filename_prefix_no_ext: str,
    default_filename: str | None = None,
) -> str | None:
    if image_path.is_dir():
        path = next(image_path.glob("featured-image.*"), None)
        if path:
            return f"{filename_prefix_no_ext}{path.suffix}"

    return default_filename


def get_language_image(language: subete.LanguageCollection) -> str | None:
    """Get image filename for a language

    :param subete.LanguageCollection language: the collection sample programs for a language.
    :return: Filename of image if found, None otherwise.
    """
    language_path = language.pathlike_name()
    image_path = pathlib.Path(f"sources/languages/{language_path}")
    return get_image(
        image_path,
        f"the-{language_path}-programming-language",
        get_default_language_image(),
    )


@functools.lru_cache
def get_default_language_image() -> str | None:
    """Get default language image filename

    :return: Filename of image if found, None otherwise.
    """
    return get_image(pathlib.Path("sources/languages"), DEFAULT_LANGUAGE_IMAGE_NO_EXT)


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
    src_dir_path = pathlib.Path(src_dir)
    dest_dir_path = pathlib.Path(dest_dir)
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
    src_image_path = next(pathlib.Path(src).glob("featured-image.*"), None)
    if not src_image_path:
        return status_code

    dest = pathlib.Path("docs/assets/images")
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
        temp_image_path = next(pathlib.Path(temp_dir).iterdir())
        shutil.move(temp_image_path, dest_image_path)
    except subprocess.CalledProcessError as exc:
        log.error("image-titler exited with %d status", exc.returncode)
        status_code = 1

    return status_code
