import pathlib

import subete
import snakemd

repo = subete.load()


def generate_project_paths(repo: subete.Repo):
    """
    Creates the project directory which contains all of the project folders
    and index.md files.
    """
    projects = repo._projects
    for project in projects:
        path = pathlib.Path(f"projects/{project}")
        path.mkdir(exist_ok=True, parents=True)
        project = path / "index.md"
        project.touch(exist_ok=True)


def generate_language_paths(repo: subete.Repo):
    """
    Creates the language directory which contains all of the language folders
    and index.md files. 
    """
    languages: dict = repo.language_collections()
    for _, language in languages.items():
        path = pathlib.Path(f"languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        lang = path / "index.md"
        lang.touch(exist_ok=True)
