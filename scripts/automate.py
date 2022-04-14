import pathlib

import subete
import snakemd


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


def generate_language_index(language: subete.LanguageCollection):
    """
    Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`. 
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    doc.add_header(str(language))
    doc.output_page(f"languages/{language.pathlike_name()}")


def generate_language_paths(repo: subete.Repo):
    """
    Creates the language directory which contains all of the language folders
    and index.md files. 
    """
    languages: dict = repo.language_collections()
    for _, language in languages.items():
        path = pathlib.Path(f"languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        generate_language_index(language)

if __name__ == "__main__":
    repo = subete.load()
    generate_language_paths(repo)
