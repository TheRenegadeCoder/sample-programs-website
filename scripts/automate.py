import logging
import pathlib
from datetime import date
from typing import List

import snakemd
import subete

log = logging.getLogger(__name__)


def _add_section(doc: snakemd.Document, source: str, source_instance: str, section: str, level: int = 2):
    """
    Adds a section to the document.

    :param snakemd.Document doc: the document to add the section to.
    :param str source: the specific source folder to pull from (e.g., languages).
    :param str source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param str section: the section to add to the document (e.g., Description).
    """
    doc.add_header(section, level=level)
    fp = pathlib.Path(
        f"sources/{source}/{source_instance}/{section.lower().replace(' ', '-')}.md")
    if fp.exists():
        log.info(f"Adding {section} section to document from source, {fp}")
        doc._contents.append(fp.read_text(encoding="utf-8"))
    else:
        log.warning(f"Failed to find {section} in {fp}")
        doc.add_paragraph(
            f"No '{section}' section available. Please consider contributing."
        ).insert_link("Please consider contributing", "https://github.com/TheRenegadeCoder/sample-programs-website")


def _add_testing_section(doc: snakemd.Document, source: str, source_instance: str):
    valid_path = pathlib.Path(f"sources/{source}/{source_instance}/valid-tests.md")
    invalid_path = pathlib.Path(f"sources/{source}/{source_instance}/invalid-tests.md")
    if valid_path.exists() and invalid_path.exists():
        doc.add_header("Testing", level=2)
        doc.add_paragraph(
            f"""
                Every project in the Sample Programs repo should be tested. In this section,
                we specify the set of tests specific to {" ".join(source_instance.split('-')).title()}.
                To keep things simple, we split up testing into two subsets: valid and invalid.
                Valid tests refer to tests that occur under correct input conditions. Invalid
                tests refer to tests that occur on bad input (e.g., letters instead of numbers).
                """
        )
        _add_section(doc, source, source_instance, "Valid Tests", level=3)
        _add_section(doc, source, source_instance, "Invalid Tests", level=3)
    else:
        _add_section(doc, source, source_instance, "Testing", level=2)


def _add_project_article_section(doc: snakemd.Document, repo: subete.Repo, project: subete.Project):
    """
    Generates a list of articles for each project page.

    :param snakemd.Document doc: the document to add the section to.
    :param subete.Repo repo: the repo to pull from.
    :param subete.Project project: the project to add to the document.
    """
    log.info(f"Generating article section of {project}")
    doc.add_header("Articles", level=2)
    articles = []
    for lang in repo:
        try:
            program: subete.Project = lang[project.name()]
        except KeyError:
            continue
        link = snakemd.InlineText(
            str(program),
            url=program.documentation_url()
        )
        articles.append(link)
    if len(articles) > 0:
        doc.add_element(snakemd.MDList(articles))
    else:
        log.warning(f"Failed to find any articles for {project}")
        doc.add_paragraph(
            f"No articles available. Please consider contributing."
        ).insert_link("Please consider contributing", "https://github.com/TheRenegadeCoder/sample-programs-website")


def _add_language_article_section(doc: snakemd.Document, repo: subete.Repo, language: str):
    """
    Generates a list of articles for each language page.

    :param snakemd.Document doc: the document to add the section to.
    :param subete.Repo repo: the repo to pull from.
    :param str language: the language to add to the document in its lookup form (e.g., Python).
    """
    doc.add_header("Articles", level=2)
    articles = []
    for program in repo[language]:
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

    :param snakemd.Document doc: the document to add the front matter to.
    :param pathlib.Path path: the path to the front matter file.
    :param str title: the title of the document
    """
    source_path = pathlib.Path("sources") / path
    doc.add_paragraph("---")
    if source_path.exists():
        doc._contents.append(source_path.read_text(encoding="utf-8").strip())
    else:
        doc._contents.append(
            f"title: {title}\nlayout: default\ndate: 2022-04-28\nlast-modified: {date.today().strftime('%Y-%m-%d')}"
        )
        log.warning(f"Failed to find {source_path}")
    doc.add_paragraph("---")


def _generate_sample_program_index(program: subete.SampleProgram, path: pathlib.Path):
    """
    Creates a sample program documentation file.

    :param subete.SampleProgram program: the sample program to create the documentation for.
    :param pathlib.Path path: the path to the documentation file.
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(
        f"programs/{program.project_pathlike_name()}/{program.language_pathlike_name()}"
    )
    _generate_front_matter(doc, root_path / "front_matter.yaml", str(program))
    doc.add_paragraph(
        f"Welcome to the {program} page! Here, you'll find the source code for this program "
        f"as well as a description of how the program works."
    ) \
        .insert_link(program.language_name(), program.language_collection().lang_docs_url()) \
        .insert_link(program.project_name(), program.project().requirements_url())
    doc.add_header("Current Solution", level=2)
    doc.add_paragraph("{% raw %}")
    doc.add_code(program.code().strip(), lang=program.language_name().lower())
    doc.add_paragraph("{% endraw %}")
    doc.add_paragraph(f"{program} was written by:") \
        .insert_link(program.language_name(), program.language_collection().lang_docs_url()) \
        .insert_link(program.project_name(), program.project().requirements_url())
    doc.add_element(snakemd.MDList(
        sorted(program.authors(), key=lambda x: x.casefold())))
    doc.add_paragraph("If you see anything you'd like to change or update, please consider contributing.") \
        .insert_link("please consider contributing", "https://github.com/TheRenegadeCoder/sample-programs")
    if program.modified() != program.created():
        doc.add_paragraph(
            "**Note**: The solution shown above is the current solution in the Sample "
            f"Programs repository as of {program.modified().strftime('%b %d %Y %H:%M:%S')}. "
            f"The solution was first committed on {program.created().strftime('%b %d %Y %H:%M:%S')}. "
            "As a result, documentation below may be outdated."
        )
    _add_section(
        doc,
        str(root_path / ".."),
        program.language_pathlike_name(),
        "How to Implement the Solution"
    )
    _add_section(
        doc,
        str(root_path / ".."),
        program.language_pathlike_name(),
        "How to Run the Solution"
    )
    try:
        doc.output_page(str(path))
    except Exception:
        log.exception(f"Failed to write {path}")


def _generate_project_index(project: subete.Project, previous: subete.Project, next: subete.Project):
    """
    Creates an index file for a single project. The path is assumed
    to be `projects/project/index.md`. 

    :param subete.Project project: the project to create the index file 
        for in the normalized form (e.g., hello-world).
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(f"projects/{project.pathlike_name()}")
    _generate_front_matter(
        doc,
        root_path / "front_matter.yaml",
        project.name()
    )
    doc.add_paragraph(
        f"Welcome to the {project.name()} page! Here, you'll find a description "
        f"of the project as well as a list of sample programs "
        f"written in various languages."
    )
    _add_section(doc, "projects", project.pathlike_name(), "Description")
    _add_section(doc, "projects", project.pathlike_name(), "Requirements")
    _add_testing_section(doc, "projects", project.pathlike_name())
    if not project.has_testing():
        doc.add_element(snakemd.Paragraph([
            snakemd.InlineText("Note:", bold=True),
            f" {project.name()} is not currently tested by Glotter. Consider contributing!"
        ]))
    _add_project_article_section(doc, repo, project)
    doc.add_horizontal_rule()
    doc.add_element(snakemd.MDList([
        snakemd.InlineText(f"Previous Project ({previous})", url=previous.requirements_url()),
        snakemd.InlineText(f"Next Project ({next})", url=next.requirements_url()),
    ]))
    doc.output_page(f"docs/projects/{project.pathlike_name()}")


def _generate_language_index(language: subete.LanguageCollection):
    """
    Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`. 
    """
    doc: snakemd.Document = snakemd.new_doc("index")
    root_path = pathlib.Path(f"languages/{language.pathlike_name()}")
    _generate_front_matter(
        doc,
        root_path / "front_matter.yaml",
        str(language)
    )
    doc.add_paragraph(
        f"Welcome to the {language} page! Here, you'll find a description "
        f"of the language as well as a list of sample programs "
        f"in that language."
    )
    _add_section(doc, "languages", language.pathlike_name(), "Description")
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
    projects = repo.approved_projects()
    for i, project in enumerate(projects):
        project: subete.Project
        path = pathlib.Path(f"docs/projects/{project.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_project_index(project, projects[i - 1], projects[(i + 1) % len(projects)])


def generate_sample_programs(repo: subete.Repo):
    """
    Creates the language folders in each project directory.
    """
    for language in repo:
        language: subete.LanguageCollection
        for program in language:
            program: subete.SampleProgram
            path = pathlib.Path(
                f"docs/projects/{program.project_pathlike_name()}/{language.pathlike_name()}"
            )
            path.mkdir(exist_ok=True, parents=True)
            _generate_sample_program_index(program, path)


def generate_language_paths(repo: subete.Repo):
    """
    Creates the language directory which contains all of the language folders
    and index.md files. 
    """
    for language in repo:
        language: subete.LanguageCollection
        path = pathlib.Path(f"docs/languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_language_index(language)


def generate_languages_index(repo: subete.Repo):
    """
    Creates the index.md files for the root directories.
    """
    language_index_path = pathlib.Path("docs/languages")
    language_index = snakemd.new_doc("index")
    _generate_front_matter(language_index, language_index_path /
                           "front_matter.yaml", "Programming Languages")
    language_index.add_paragraph(
        "Welcome to the Languages page! Here, you'll find a list of all of the languages represented in the collection. "
        f"At this time, there are {len(list(repo))} languages, of which {repo.total_tests()} are tested, "
        f"and {repo.total_programs()} code snippets."
    )
    language_index.add_header("Language Collections by Letter", level=2)
    language_index.add_paragraph(
        "To help you navigate the collection, the following languages are organized alphabetically and grouped by first letter."
    )
    for letter in repo.sorted_language_letters():
        language_index.add_header(letter.upper(), level=3)
        languages: list[subete.LanguageCollection] = repo.languages_by_letter(
            letter)
        snippets = sum(language.total_programs() for language in languages)
        tests = sum(1 if language.has_testinfo()
                    else 0 for language in languages)
        verb = "are" if tests != 1 else "is"
        singular = "language" if len(languages) == 1 else "languages"
        language_index.add_paragraph(
            f"The '{letter.upper()}' collection contains {len(languages)} {singular}, "
            f"of which {tests} {verb} tested, and {snippets} code snippets."
        )
        languages.sort(key=lambda x: x.name().casefold())
        languages = [
            snakemd.InlineText(x.name(), url=x.lang_docs_url())
            for x in languages
        ]
        language_index.add_element(snakemd.MDList(languages))
    language_index.output_page(str(language_index_path))


def generate_projects_index(repo: subete.Repo):
    projects_index_path = pathlib.Path("docs/projects")
    projects_index = snakemd.new_doc("index")
    _generate_front_matter(projects_index, projects_index_path /
                           "front_matter.yaml", "Programming Projects in Every Language")
    projects_index._contents[-2] = projects_index._contents[-2] + \
        "\nfeatured-image: programming-projects-in-every-language.jpg"
    project_tests = sum(1 if project.has_testing()
                        else 0 for project in repo.approved_projects())
    projects_index.add_paragraph(
        "Welcome to the Projects page! Here, you'll find a list of all of the projects represented in the collection. "
        f"At this time, the repo supports {repo.total_approved_projects()} projects, of which {project_tests} are tested."
    )
    projects_index.add_header("Projects List", level=2)
    projects_index.add_paragraph(
        "To help you navigate the collection, the following projects are organized alphabetically."
    )
    repo.approved_projects().sort(key=lambda x: x.name().casefold())
    projects = [
        snakemd.InlineText(
            project.name(),
            url=project.requirements_url()
        )
        for project in repo.approved_projects()
    ]
    projects_index.add_element(snakemd.MDList(projects))
    projects_index.output_page(str(projects_index_path))


def clean(folder: str):
    """
    Deletes the contents of the docs directory.
    """
    path = pathlib.Path(folder)
    if path.exists():
        for child in path.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                clean(child)
        path.rmdir()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    clean("docs/projects")
    clean("docs/languages")
    repo = subete.load()
    generate_language_paths(repo)
    generate_project_paths(repo)
    generate_sample_programs(repo)
    generate_languages_index(repo)
    generate_projects_index(repo)
