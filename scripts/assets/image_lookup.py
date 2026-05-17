import functools
from pathlib import Path

import subete
from constants import DEFAULT_LANGUAGE_IMAGE_NO_EXT, DEFAULT_PROJECT_IMAGE_NO_EXT


def find_program_image(program: subete.SampleProgram) -> str | None:
    """Gets the filename of the image for a sample program

    :param subete.SampleProgram program: the sample program to get the image for.
    :return: Filename of image if found, None otherwise.
    """
    project_path = program.project_pathlike_name()
    language_path = program.language_pathlike_name()
    image_path = Path(f"sources/programs/{project_path}/{language_path}")
    return find_image(
        image_path,
        f"{project_path}-in-{language_path}",
        find_project_image(program.project()),
    )


@functools.lru_cache
def find_project_image(project: subete.Project) -> str | None:
    """Gets the filename of the image for a project

    :param subete.Project project: the project to create the index file
        for in the normalized form (e.g., hello-world).
    :return: Filename of image if found, None otherwise.
    """
    project_path = project.pathlike_name()
    image_path = Path(f"sources/projects/{project_path}")
    return find_image(
        image_path,
        f"{project_path}-in-every-language",
        find_default_project_image(),
    )


@functools.lru_cache
def find_default_project_image() -> str | None:
    """Gets the filename of the default project image

    :return: Filename of image if found, None otherwise
    """
    return find_image(Path("sources/projects"), DEFAULT_PROJECT_IMAGE_NO_EXT)


@functools.lru_cache
def find_image(
    image_path: Path,
    filename_prefix_no_ext: str,
    default_filename: str | None = None,
) -> str | None:
    if image_path.is_dir():
        path = next(image_path.glob("featured-image.*"), None)
        if path:
            return f"{filename_prefix_no_ext}{path.suffix}"

    return default_filename


def find_language_image(language: subete.LanguageCollection) -> str | None:
    """Get image filename for a language

    :param subete.LanguageCollection language: the collection sample programs for a language.
    :return: Filename of image if found, None otherwise.
    """
    language_path = language.pathlike_name()
    image_path = Path(f"sources/languages/{language_path}")
    return find_image(
        image_path,
        f"the-{language_path}-programming-language",
        find_default_language_image(),
    )


@functools.lru_cache
def find_default_language_image() -> str | None:
    """Get default language image filename

    :return: Filename of image if found, None otherwise.
    """
    return find_image(Path("sources/languages"), DEFAULT_LANGUAGE_IMAGE_NO_EXT)
