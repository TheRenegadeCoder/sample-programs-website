from functools import cache
from pathlib import Path

import subete
from constants import DEFAULT_LANGUAGE_IMAGE_NO_EXT, DEFAULT_PROJECT_IMAGE_NO_EXT

BASE_DIR = Path("sources")
PROJECTS_DIR = BASE_DIR / "projects"
LANGUAGES_DIR = BASE_DIR / "languages"
PROGRAMS_DIR = BASE_DIR / "programs"


@cache
def _resolve_image(
    directory: Path,
    target_name: str,
    fallback: str | None = None,
) -> str | None:
    """Locates a 'featured-image' and formats its output name.

    Args:
        directory: The Path directory to search within.
        target_name: The base filename string to return if an image is found.
        fallback: The filename to return if no image is found in the directory.

    Returns:
        The target name combined with the original file extension if found,
        otherwise the fallback value.

    """
    if directory.is_dir():
        if img_file := next(directory.glob("featured-image.*"), None):
            return f"{target_name}{img_file.suffix}"

    return fallback


@cache
def get_default_project_image() -> str | None:
    """Retrieves the default project image filename.

    Returns:
        The filename of the default project image if found, otherwise None.

    """
    return _resolve_image(PROJECTS_DIR, DEFAULT_PROJECT_IMAGE_NO_EXT)


@cache
def get_default_language_image() -> str | None:
    """Retrieves the default language image filename.

    Returns:
        The filename of the default language image if found, otherwise None.

    """
    return _resolve_image(LANGUAGES_DIR, DEFAULT_LANGUAGE_IMAGE_NO_EXT)


@cache
def find_project_image(project: subete.Project) -> str | None:
    """Gets the image filename for a specific project.

    Args:
        project: The subete Project instance to look up.

    Returns:
        The formatted project image filename, or the default project image
        if a specific one isn't found.

    """
    name = project.pathlike_name()
    return _resolve_image(
        directory=PROJECTS_DIR / name,
        target_name=f"{name}-in-every-language",
        fallback=get_default_project_image(),
    )


def find_language_image(language: subete.LanguageCollection) -> str | None:
    """Gets the image filename for a specific language.

    Args:
        language: The subete LanguageCollection instance to look up.

    Returns:
        The formatted language image filename, or the default language image
        if a specific one isn't found.

    """
    name = language.pathlike_name()
    return _resolve_image(
        directory=LANGUAGES_DIR / name,
        target_name=f"the-{name}-programming-language",
        fallback=get_default_language_image(),
    )


def find_program_image(program: subete.SampleProgram) -> str | None:
    """Gets the image filename for a specific sample program.

    Args:
        program: The subete SampleProgram instance to look up.

    Returns:
        The formatted sample program image filename, falling back to its
        associated project image if not found locally.

    """
    proj_name = program.project_pathlike_name()
    lang_name = program.language_pathlike_name()

    return _resolve_image(
        directory=PROGRAMS_DIR / proj_name / lang_name,
        target_name=f"{proj_name}-in-{lang_name}",
        fallback=find_project_image(program.project()),
    )
