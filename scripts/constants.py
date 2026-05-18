from pathlib import Path

SOURCE_DIR = Path("sources")
DOCS_DIR = Path("docs")

ASSETS_DIR = DOCS_DIR / "assets" / "images"

GENERATED_DIR = SOURCE_DIR / "generated"
LANGUAGES_DIR = SOURCE_DIR / "languages"
PROGRAMS_DIR = SOURCE_DIR / "programs"
PROJECTS_DIR = SOURCE_DIR / "projects"

DOCS_LANGUAGES_DIR = DOCS_DIR / "languages"
DOCS_PROGRAMS_DIR = DOCS_DIR / "projects"
DOCS_PROJECTS_DIR = DOCS_DIR / "projects"

DEFAULT_IMAGES = {
    "program": "sample-programs-in-every-language",
    "project": "programming-projects-in-every-language",
    "language": "programming-languages",
}

DEFAULT_PROGRAM_IMAGE_NO_EXT = DEFAULT_IMAGES["program"]
DEFAULT_PROJECT_IMAGE_NO_EXT = DEFAULT_IMAGES["project"]
DEFAULT_LANGUAGE_IMAGE_NO_EXT = DEFAULT_IMAGES["language"]

AUTO_GENERATED_NOTICE = "AUTO-GENERATED -- DO NOT EDIT"
CONTRIBUTING_NOTICE = "See .github/CONTRIBUTING.md for contribution guidelines."

PROGRAM_MD_FILES = (
    "how-to-implement-the-solution.md",
    "how-to-run-the-solution.md",
)

PROJECT_MD_FILES = (
    "description.md",
    "requirements.md",
)

LANGUAGE_MD_FILES = ("description.md",)
