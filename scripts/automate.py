import pathlib
import logging
from string import ascii_lowercase

import subete
import snakemd

log = logging.getLogger(__name__)


def _add_section(doc: snakemd.Document, source: str, source_instance: str, section: str):
    """
    Adds a section to the document.

    :param doc: the document to add the section to.
    :param source: the specific source folder to pull from (e.g., languages).
    :param source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param section: the section to add to the document (e.g., Description).
    """
    doc.add_header(section, level=2)
    fp = pathlib.Path(f"sources/{source}/{source_instance}/{section.lower().replace(' ', '-')}.md")
    if fp.exists():
        log.info(f"Adding {section} section to document from source, {fp}")
        doc._contents.append(fp.read_text(encoding="utf-8"))
    else:
        log.warning(f"Failed to find {section} in {fp}")
        doc.add_paragraph(
            f"No {section.lower()} available. Please consider contributing."
        )


def _add_project_article_section(doc: snakemd.Document, repo: subete.Repo, project: str):
    """
    Generates a list of articles for each project page.

    :param doc: the document to add the section to.
    :param repo: the repo to pull from.
    :param project: the project to add to the document in the normalized form (e.g., hello-world).
    """
    log.info(f"Generating article section of {project}")
    doc.add_header("Articles", level=2)
    articles = []
    for lang in repo.language_collections().values():
        if program := lang.sample_programs().get(project.replace('-', ' ').title()):
            link = snakemd.InlineText(
                str(program),
                url=program._sample_program_doc_url
            )
            articles.append(link)
    doc.add_element(snakemd.MDList(articles))


def _add_language_article_section(doc: snakemd.Document, repo: subete.Repo, language: str):
    """
    Generates a list of articles for each language page.

    :param doc: the document to add the section to.
    :param repo: the repo to pull from.
    :param language: the language to add to the document in its lookup form (e.g., Python).
    """
    doc.add_header("Articles", level=2)
    articles = []
    for program in repo[language].sample_programs().values():
        link = snakemd.InlineText(
            str(program),
            url=program._sample_program_doc_url
        )
        articles.append(link)
    doc.add_element(snakemd.MDList(articles))


def _generate_front_matter(doc: snakemd.Document, path: pathlib.Path, title: str):
    """
    Takes the existing front matter and adds it to the document.
    If no front matter exists, a default one is created.
    """
    source_path = pathlib.Path("sources") / path
    doc.add_paragraph("---")
    if source_path.exists():
        doc._contents.append(source_path.read_text(encoding="utf-8").strip())
    else:
        doc.add_paragraph(f"title: {title}")
        log.warning(f"Failed to find {path}")
    doc.add_paragraph("---")


def _generate_sample_program_index(program: subete.SampleProgram, path: pathlib.Path, language: str):
    """
    Creates a sample program documentation file.
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(f"programs/{program._normalize_program_name()}/{language}")
    _generate_front_matter(doc, root_path / "front_matter.yaml", str(program))
    doc.add_paragraph(
        f"Welcome to the {program} page! Here, you'll find the source code for this program "
        f"as well as a description of how the program works."
    )
    doc.add_header("Current Solution", level=2)
    doc.add_paragraph("Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.")
    doc.add_paragraph("{% raw %}")
    doc.add_code(program.code(), lang=program.language())
    doc.add_paragraph("{% endraw %}")
    _add_section(doc, str(root_path / ".."), language, "How to Implement the Solution")
    _add_section(doc, str(root_path / ".."), language, "How to Run the Solution")
    try:
        doc.output_page(str(path))
    except Exception:
        log.exception(f"Failed to write {path}")


def _generate_project_index(project: str):
    """
    Creates an index file for a single project. The path is assumed
    to be `projects/project/index.md`. 

    :param project: the project to create the index file for in the normalized form (e.g., hello-world).
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(f"sources/projects/{project}")
    title = ' '.join([
        word.capitalize() if len(project) > 3 else word.upper()
        for word in project.split('-')
    ])
    _generate_front_matter(doc, root_path / "front_matter.yaml", title)
    doc.add_paragraph(
        f"Welcome to the {title} page! Here, you'll find a description "
        f"of the project as well as a list of sample programs "
        f"written in various languages."
    )
    _add_section(doc, "projects", project, "Description")
    _add_section(doc, "projects", project, "Requirements")
    _add_section(doc, "projects", project, "Testing")
    _add_project_article_section(doc, repo, project)
    doc.output_page(f"docs/projects/{project}")


def _generate_language_index(language: subete.LanguageCollection):
    """
    Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`. 
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(f"languages/{language.pathlike_name()}")
    _generate_front_matter(doc, root_path / "front_matter.yaml", str(language))
    doc.add_paragraph(
        f"Welcome to the {language} page! Here, you'll find a description " 
        f"of the language as well as a list of sample programs "
        f"in that language."
    )
    _add_section(doc, "languages", language, "Description")
    _add_language_article_section(doc, repo, str(language))
    try:
        doc.output_page(f"docs/languages/{language.pathlike_name()}")
    except Exception:
        log.exception(f"Failed to write {language.pathlike_name()}")


def generate_project_paths(repo: subete.Repo):
    """
    Creates the project directory which contains all of the project folders
    and index.md files.
    """
    projects = repo._projects
    for project in projects:
        path = pathlib.Path(f"docs/projects/{project}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_project_index(project)


def generate_sample_programs(repo: subete.Repo):
    """
    Creates the language folders in each project directory.
    """
    for language in repo.language_collections().values():
        for program in language.sample_programs().values():
            path = pathlib.Path(f"docs/projects/{program._normalize_program_name()}/{language.pathlike_name()}")
            path.mkdir(exist_ok=True, parents=True)
            _generate_sample_program_index(program, path, language.pathlike_name())


def generate_language_paths(repo: subete.Repo):
    """
    Creates the language directory which contains all of the language folders
    and index.md files. 
    """
    languages: dict = repo.language_collections()
    for _, language in languages.items():
        path = pathlib.Path(f"docs/languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_language_index(language)


def generate_languages_index(repo: subete.Repo):
    """
    Creates the index.md files for the root directories.
    """
    language_index_path = pathlib.Path("docs/languages")
    language_index = snakemd.new_doc("index")
    _generate_front_matter(language_index, language_index_path / "front_matter.yaml", "Programming Languages")
    language_index.add_paragraph(
        "Welcome to the Languages page! Here, you'll find a list of all of the languages represented in the collection."
    )
    language_index.add_header("Language Collections by Letter", level=2)
    language_index.add_paragraph(
        "To help you navigate the collection, the following languages are organized alphabetically and grouped by first letter."
    )
    for letter in ascii_lowercase:
        language_index.add_header(letter, level=3)
        languages: list[subete.LanguageCollection] = repo.languages_by_letter(letter)
        languages = [snakemd.InlineText(str(x).upper(), url=x.lang_docs_url()) for x in languages]
        language_index.add_element(snakemd.MDList(languages))
    language_index.output_page(str(language_index_path))


def generate_projects_index(repo: subete.Repo):
    projects_index_path = pathlib.Path("docs/projects")
    projects_index = snakemd.new_doc("index")
    _generate_front_matter(projects_index, projects_index_path / "front_matter.yaml", "Projects")
    projects_index.add_paragraph(
        "Welcome to the Projects page! Here, you'll find a list of all of the projects represented in the collection."
    )
    projects_index.add_header("Projects List", level=2)
    projects_index.add_paragraph(
        "To help you navigate the collection, the following projects are organized alphabetically."
    )
    projects = [
        snakemd.InlineText(
            project.replace("-", " ").title() 
            if len(project) > 3 
            else project.upper(),
            url=f"https://sampleprograms.io/projects/{project}"
        ) 
        for project in repo._projects
    ]
    projects_index.add_element(snakemd.MDList(projects))
    projects_index.output_page(str(projects_index_path))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    repo = subete.load()
    generate_language_paths(repo)
    generate_project_paths(repo)
    generate_sample_programs(repo)
    generate_languages_index(repo)
    generate_projects_index(repo)
