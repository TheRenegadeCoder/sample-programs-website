import pathlib
import logging

import subete
import snakemd

log = logging.getLogger(__name__)


def _add_project_section(doc: snakemd.Document, source: str, source_instance: str, section: str):
    """
    Adds a section to the document.

    :param doc: the document to add the section to.
    :param source: the specific source folder to pull from (e.g., languages).
    :param source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param section: the section to add to the document (e.g., Description).
    """
    doc.add_header(section, level=2)
    fp = pathlib.Path(f"sources/{source}/{source_instance}/{section.lower()}.md")
    if fp.exists():
        log.info(f"Adding {section} section to document from source, {fp}")
        doc._contents.append(fp.read_text())
    else:
        log.warning(f"Failed to find {section} in {fp}")
        doc.add_paragraph(
            f"No {section.lower()} available. Please consider contributing.")


def _add_article_section(doc: snakemd.Document, repo: subete.Repo, project: str):
    """
    Generates a list of articles.
    """
    doc.add_header("Articles", level=2)
    articles = []
    for lang in repo.language_collections().values():
        for key, program in lang.sample_programs().items():
            if key.replace(" ", "-").lower() == project:
                link = snakemd.InlineText(
                    str(program),
                    url=program._sample_program_doc_url
                )
                articles.append(link)
    doc.add_element(snakemd.MDList(articles))


def generate_project_index(project: str):
    """
    Creates an index file for a single project. The path is assumed
    to be `projects/project/index.md`. 
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    title = ' '.join([
        word.capitalize() if len(project) > 3 else word.upper()
        for word in project.split('-')
    ])
    doc.add_header(f"{title} in Every Language")
    _add_project_section(doc, "projects", project, "Description")
    _add_project_section(doc, "projects", project, "Requirements")
    _add_project_section(doc, "projects", project, "Testing")
    _add_article_section(doc, repo, project)
    doc.output_page(f"docs/projects/{project}")


def generate_project_paths(repo: subete.Repo):
    """
    Creates the project directory which contains all of the project folders
    and index.md files.
    """
    projects = repo._projects
    for project in projects:
        path = pathlib.Path(f"docs/projects/{project}")
        path.mkdir(exist_ok=True, parents=True)
        generate_project_index(project)


def generate_language_index(language: subete.LanguageCollection):
    """
    Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`. 
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    doc.add_header(f"The {str(language)} Programming Language")
    _add_project_section(doc, "languages", language, "Description")
    doc.add_header("Articles", level=2)
    # TODO: Add a list of articles for this language
    doc.add_header("Further Reading", level=2)
    # TODO: Add a list of resources
    doc.output_page(f"docs/languages/{language.pathlike_name()}")


def generate_language_paths(repo: subete.Repo):
    """
    Creates the language directory which contains all of the language folders
    and index.md files. 
    """
    languages: dict = repo.language_collections()
    for _, language in languages.items():
        path = pathlib.Path(f"docs/languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        generate_language_index(language)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    repo = subete.load()
    generate_language_paths(repo)
    generate_project_paths(repo)
