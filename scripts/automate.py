from typing import Optional
import datetime
import logging
import os
import pathlib
import shutil
import subprocess
import tempfile
import sys
import functools

import snakemd
import subete
import glotter
import yaml

log = logging.getLogger("automate")
AUTO_GEN_TEST_DOC_DIR = "sources/generated"

DEFAULT_PROGRAM_IMAGE_NO_EXT = "sample-programs-in-every-language"
DEFAULT_PROJECT_IMAGE_NO_EXT = "programming-projects-in-every-language"
DEFAULT_LANGUAGE_IMAGE_NO_EXT = "programming-languages"


def _add_section(doc: snakemd.Document, source: str, source_instance: str, section: str, level: int = 2):
    """
    Adds a section to the document.

    :param snakemd.Document doc: the document to add the section to.
    :param str source: the specific source folder to pull from (e.g., languages).
    :param str source_instance: the specific source instance to pull from (e.g., c-plus-plus).
    :param str section: the section to add to the document (e.g., Description).
    """
    doc.add_heading(section, level=level)
    fp = pathlib.Path(
        f"sources/{source}/{source_instance}/{section.lower().replace(' ', '-')}.md")
    if fp.exists():
        log.info(f"Adding {section} section to document from source, {fp}")
        doc.add_raw(fp.read_text(encoding="utf-8"))
    else:
        log.warning(f"Failed to find {section} in {fp}")
        doc.add_paragraph(
            f"No '{section}' section available. Please consider contributing."
        ).insert_link("Please consider contributing", "https://github.com/TheRenegadeCoder/sample-programs-website")


def _add_testing_section(doc: snakemd.Document, source: str, source_instance: str):
    valid_path = pathlib.Path(f"sources/{source}/{source_instance}/valid-tests.md")
    invalid_path = pathlib.Path(f"sources/{source}/{source_instance}/invalid-tests.md")
    auto_gen_path = pathlib.Path(f"{AUTO_GEN_TEST_DOC_DIR}/{source_instance}/testing.md")
    if auto_gen_path.exists():
        _add_section(
            doc, pathlib.Path(AUTO_GEN_TEST_DOC_DIR).name, source_instance, "Testing", level=2
        )
    elif valid_path.exists() and invalid_path.exists():
        doc.add_heading("Testing", level=2)
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
    doc.add_heading("Articles", level=2)
    articles = []
    for lang in repo:
        try:
            program: subete.SampleProgram = lang[project.name()]
        except KeyError:
            continue
        link = snakemd.Inline(
            str(program),
            link=program.documentation_url()
        )
        articles.append(link)
    if len(articles) > 0:
        doc.add_block(snakemd.MDList(articles))
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
    doc.add_heading("Articles", level=2)
    articles = []
    for program in repo[language]:
        link = snakemd.Inline(
            str(program),
            link=program._sample_program_doc_url
        )
        articles.append(link)
    doc.add_block(snakemd.MDList(articles))


def _generate_front_matter(
        doc: snakemd.Document, 
        path: pathlib.Path, 
        title: str, 
        created_at: Optional[datetime.datetime] = None, 
        last_modified: Optional[datetime.datetime] = None, 
        image: Optional[str] = None
    ):
    """
    Takes the existing front matter and adds it to the document.
    If no front matter exists, a default one is created.

    :param snakemd.Document doc: the document to add the front matter to.
    :param pathlib.Path path: the path to the front matter file.
    :param str title: the title of the document.
    :param datetime.datetime created_at: optional date/time when item is created.
    :param datatime.datetime last_modified: optional date/time when item was last modified.
    :param str image: optional filename of the image.
    """
    source_path = pathlib.Path("sources") / path
    if source_path.exists():
        front_matter = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    else:
        front_matter = {"title": title}
        if created_at:
            front_matter["date"] = created_at.strftime("%Y-%m-%d")

        if not last_modified:
            last_modified = created_at

        if last_modified:
            front_matter["last-modified"] = last_modified.strftime("%Y-%m-%d")

        log.warning(f"Failed to find %s", str(source_path))

    front_matter["layout"] = "default"
    if image:
        front_matter["featured-image"] = image

    if front_matter.get("date") and not front_matter.get("last-modified"):
        front_matter["last-modified"] = front_matter["date"]

    raw = "---\n" + yaml.safe_dump(front_matter) + "---"
    doc.add_raw(raw)


def _generate_sample_program_index(program: subete.SampleProgram, path: pathlib.Path):
    """
    Creates a sample program documentation file.

    :param subete.SampleProgram program: the sample program to create the documentation for.
    :param pathlib.Path path: the path to the documentation file.
    """
    doc: snakemd.Document = snakemd.new_doc()
    root_path = pathlib.Path(
        f"programs/{program.project_pathlike_name()}/{program.language_pathlike_name()}"
    )
    _generate_front_matter(
        doc, 
        root_path / "front_matter.yaml", 
        str(program), 
        created_at=program.created(),
        image=_get_program_image(program)
    )
    doc.add_paragraph(
        f"Welcome to the {program} page! Here, you'll find the source code for this program "
        f"as well as a description of how the program works."
    ) \
        .insert_link(program.language_name(), program.language_collection().lang_docs_url()) \
        .insert_link(program.project_name(), program.project().requirements_url())
    doc.add_heading("Current Solution", level=2)

    if program.image_type():
        image_dest = path / pathlib.Path(program.project_path()).name
        shutil.copy(program.project_path(), image_dest)
        doc.add_block(
            snakemd.Paragraph(
                [
                    snakemd.Inline(
                        f"{program.project_name()} in {program.language_name()}",
                        image="/" + "/".join(image_dest.parts[1:])
                    )
                ]
            )
        )
    else:
        doc.add_paragraph("{% raw %}")
        doc.add_code(program.code().rstrip().expandtabs(4), lang=program.language_name().lower().replace(" ", "_"))
        doc.add_paragraph("{% endraw %}")

    doc.add_paragraph(f"{program} was written by:") \
        .insert_link(program.language_name(), program.language_collection().lang_docs_url()) \
        .insert_link(program.project_name(), program.project().requirements_url())
    doc.add_block(snakemd.MDList(sorted(program.authors(), key=lambda x: x.casefold())))
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
        doc.dump("index", dir=str(path))
    except Exception:
        log.exception(f"Failed to write {path}")


def _get_program_image(program: subete.SampleProgram) -> Optional[str]:
    """
    Gets the filename of the image for a sample program

    :param subete.SampleProgram program: the sample program to get the image for.
    :return: Filename of image if found, None otherwise.
    """
    project_path = program.project_pathlike_name()
    language_path = program.language_pathlike_name()
    image_path = pathlib.Path(f"sources/programs/{project_path}/{language_path}")
    return _get_image(
        image_path,
        f"{project_path}-in-{language_path}",
        _get_project_image(program.project())
    )


@functools.lru_cache()
def _get_project_image(project: subete.Project) -> Optional[str]:
    """
    Gets the filename of the image for a project

    :param subete.Project project: the project to create the index file 
        for in the normalized form (e.g., hello-world).
    :return: Filename of image if found, None otherwise.
    """

    project_path = project.pathlike_name()
    image_path = pathlib.Path(f"sources/projects/{project_path}")
    return _get_image(
        image_path,
        f"{project_path}-in-every-language",
        _get_default_project_image()
    )


@functools.lru_cache()
def _get_default_project_image() -> Optional[str]:
    """
    Gets the filename of the default project image

    :return: Filename of image if found, None otherwise
    """

    _get_image(pathlib.Path("sources"), DEFAULT_PROJECT_IMAGE_NO_EXT)


@functools.lru_cache()
def _get_image(
    image_path: pathlib.Path, filename_prefix_no_ext: str, default_filename: Optional[str] = None
) -> str:
    if image_path.is_dir():
        path = next(image_path.glob("featured-image.*"), None)
        if path:
            return f"{filename_prefix_no_ext}{path.suffix}"
        
    return default_filename


def _generate_project_index(project: subete.Project, previous: subete.Project, next: subete.Project):
    """
    Creates an index file for a single project. The path is assumed
    to be `projects/project/index.md`. 

    :param subete.Project project: the project to create the index file 
        for in the normalized form (e.g., hello-world).
    """
    doc: snakemd.Document = snakemd.new_doc()
    root_path = pathlib.Path(f"projects/{project.pathlike_name()}")
    _generate_front_matter(
        doc,
        root_path / "front_matter.yaml",
        project.name(),
        image=_get_project_image(project)
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
        doc.add_block(snakemd.Paragraph([
            snakemd.Inline("Note:", bold=True),
            f" {project.name()} is not currently tested by Glotter2. Consider contributing!"
        ]))
    _add_project_article_section(doc, repo, project)
    doc.add_horizontal_rule()
    doc.add_paragraph("<nav class=\"project-nav\">")
    doc.add_paragraph("<div id=\"prev\" markdown=\"1\">")
    doc.add_block(snakemd.Paragraph([snakemd.Inline(f"<-- Previous Project ({previous})", link=previous.requirements_url())]))
    doc.add_paragraph("</div>")
    doc.add_paragraph("<div id=\"next\" markdown=\"1\">")
    doc.add_block(snakemd.Paragraph([snakemd.Inline(f"Next Project ({next}) -->", link=next.requirements_url())]))
    doc.add_paragraph("</div>")
    doc.add_paragraph("</nav>")
    doc.dump("index", dir=f"docs/projects/{project.pathlike_name()}")  


def _generate_language_index(language: subete.LanguageCollection):
    """
    Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`.

    :param subete.LanguageCollection language: the collection sample programs for a language.
    """
    doc: snakemd.Document = snakemd.new_doc()
    root_path = pathlib.Path(f"languages/{language.pathlike_name()}")
    oldest_program: subete.SampleProgram = min(language, key=lambda x: x.created())
    _generate_front_matter(
        doc,
        root_path / "front_matter.yaml",
        f"The {language} Programming Language",
        created_at=oldest_program.created(),
        image=_get_language_image(language)
    )
    doc.add_paragraph(
        f"Welcome to the {language} page! Here, you'll find a description "
        f"of the language as well as a list of sample programs "
        f"in that language."
    )
    _add_section(doc, "languages", language.pathlike_name(), "Description")
    _add_language_article_section(doc, repo, str(language))
    try:
        doc.dump("index", dir=f"docs/languages/{language.pathlike_name()}")
    except Exception:
        log.exception(f"Failed to write {language.pathlike_name()}")


def _get_language_image(language: subete.LanguageCollection) -> Optional[str]:
    """
    Get image filename for a language

    :param subete.LanguageCollection language: the collection sample programs for a language.
    :return: Filename of image if found, None otherwise.
    """
    language_path = language.pathlike_name()
    image_path = pathlib.Path(f"sources/languages/{language_path}")
    return _get_image(
        image_path,
        f"the-{language_path}-programming-language",
        _get_default_language_image()
    )


@functools.lru_cache()
def _get_default_language_image() -> Optional[str]:
    """
    Get default language image filename

    :return: Filename of image if found, None otherwise.
    """

    return _get_image(pathlib.Path("sources/languages"), DEFAULT_LANGUAGE_IMAGE_NO_EXT)


def generate_project_paths(repo: subete.Repo):
    """
    Creates the project directory which contains all of the project folders
    and index.md files.

    :param subete.Repo repo: the repo to pull from.
    """
    projects = repo.approved_projects()
    projects.sort(key=lambda x: x.name().casefold())
    for i, project in enumerate(projects):
        project: subete.Project
        log.info("Generating project paths for %s", str(project))
        path = pathlib.Path(f"docs/projects/{project.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_project_index(project, projects[i - 1], projects[(i + 1) % len(projects)])


def generate_sample_programs(repo: subete.Repo):
    """
    Creates the language folders in each project directory.

    :param subete.Repo repo: the repo to pull from.
    """
    for language in repo:
        language: subete.LanguageCollection
        for program in language:
            log.info("Generate sample programs for %s in %s", str(program), str(language))
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

    :param subete.Repo repo: the repo to pull from.
    """
    for language in repo:
        log.info("Generating language paths for %s", str(language))
        language: subete.LanguageCollection
        path = pathlib.Path(f"docs/languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        _generate_language_index(language)


def generate_auto_gen_test_docs(repo: subete.Repo):
    """
    Generate auto-generated test documentation

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating test documentation")
    curr_dir = os.getcwd()
    doc_dir = pathlib.Path(AUTO_GEN_TEST_DOC_DIR).absolute()
    os.chdir(repo.sample_programs_repo_dir())
    glotter.generate_test_docs(
        doc_dir=doc_dir,
        repo_name="Sample Programs",
        repo_url="https://github.com/TheRenegadeCoder/sample-programs"
    )
    os.chdir(curr_dir)


def generate_languages_index(repo: subete.Repo):
    """
    Creates the index.md files for the root directories.

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating language index")
    language_index_path = pathlib.Path("docs/languages")
    language_index = snakemd.new_doc()
    oldest_lang: subete.LanguageCollection = min(repo, key=lambda lang: min(lang, key=lambda x: x.created()).created())
    oldest_program: subete.SampleProgram = min(oldest_lang, key=lambda x: x.created())
    newest_lang: subete.LanguageCollection = max(repo, key=lambda lang: max(lang, key=lambda x: x.created()).created())
    newest_program: subete.SampleProgram = max(newest_lang, key=lambda x: x.created())
    _generate_front_matter(
        language_index, 
        language_index_path / "front_matter.yaml", 
        "Programming Languages",
        created_at=oldest_program.created(),
        last_modified=newest_program.created(),
        image=_get_default_language_image()
    )
    language_index.add_paragraph(
        "Welcome to the Languages page! Here, you'll find a list of all of the languages represented in the collection. "
        f"At this time, there are {len(list(repo))} languages, of which {repo.total_tests()} are tested, "
        f"and {repo.total_programs()} code snippets."
    )
    language_index.add_heading("Language Collections by Letter", level=2)
    language_index.add_paragraph(
        "To help you navigate the collection, the following languages are organized alphabetically and grouped by first letter."
    )
    for letter in repo.sorted_language_letters():
        language_index.add_heading(letter.upper(), level=3)
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
            snakemd.Inline(x.name(), link=x.lang_docs_url())
            for x in languages
        ]
        language_index.add_block(snakemd.MDList(languages))
    language_index.dump("index", dir=str(language_index_path))


def generate_projects_index(repo: subete.Repo):
    """
    Generate index.md for file for Projects page

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating projects index")
    projects_index_path = pathlib.Path("docs/projects")
    projects_index: snakemd.Document = snakemd.new_doc()
    oldest_lang: subete.LanguageCollection = min(repo, key=lambda lang: min(lang, key=lambda x: x.created()).created())
    oldest_program: subete.SampleProgram = min(oldest_lang, key=lambda x: x.created())
    newest_lang: subete.LanguageCollection = max(repo, key=lambda lang: max(lang, key=lambda x: x.created()).created())
    newest_program: subete.SampleProgram = max(newest_lang, key=lambda x: x.created())
    _generate_front_matter(
        projects_index, 
        projects_index_path / "front_matter.yaml", 
        "Programming Projects in Every Language",
        created_at=oldest_program.created(),
        last_modified=newest_program.created(),
        image=_get_default_project_image()
    )
    project_tests = sum(
        1 if project.has_testing() else 0 
        for project in repo.approved_projects()
    )
    projects_index.add_paragraph(
        "Welcome to the Projects page! Here, you'll find a list of all of the projects represented in the collection. "
        f"At this time, the repo supports {repo.total_approved_projects()} projects, of which {project_tests} are tested."
    )
    projects_index.add_heading("Projects List", level=2)
    projects_index.add_paragraph(
        "To help you navigate the collection, the following projects are organized alphabetically."
    )
    repo.approved_projects().sort(key=lambda x: x.name().casefold())
    projects = [
        snakemd.Inline(
            project.name(),
            link=project.requirements_url()
        )
        for project in repo.approved_projects()
    ]
    projects_index.add_block(snakemd.MDList(projects))
    projects_index.dump("index", dir=str(projects_index_path))


def generate_images(repo: subete.Repo) -> int:
    """
    Use image-titler to resize and crop images and add logo

    :param subete.Repo repo: the repo to pull from.
    :return: 0 if no error, non-zero otherwise
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        status_code = 0
        status_code = _generate_language_images(repo, temp_dir, status_code)
        status_code = _generate_project_images(repo, temp_dir, status_code)
        status_code = _generate_program_images(repo, temp_dir, status_code)
    return status_code


def _generate_language_images(repo: subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = _generate_image(
        temp_dir, "sources/languages", DEFAULT_LANGUAGE_IMAGE_NO_EXT, status_code
    )
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        status_code = _generate_image(
            temp_dir, f"sources/{language_path}", language_path, status_code
        )

    return status_code


def _generate_project_images(repo: subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = _generate_image(
        temp_dir, "sources/projects", DEFAULT_PROJECT_IMAGE_NO_EXT, status_code
    )
    for project in repo.approved_projects():
        project_path = project.pathlike_name()
        status_code = _generate_image(
            temp_dir,
            f"sources/projects/{project_path}",
            f"{project_path}-in-every-language",
            status_code
        )


def _generate_program_images(repo:subete.Repo, temp_dir: str, status_code: int) -> int:
    status_code = _generate_image(
        temp_dir, "sources", DEFAULT_PROGRAM_IMAGE_NO_EXT, status_code
    )
    language: subete.LanguageCollection
    for language in repo:
        language_path = language.pathlike_name()
        program: subete.SampleProgram
        for program in repo[str(language)]:
            program_path = program.project_pathlike_name()
            status_code = _generate_image(
                temp_dir,
                f"sources/programs/{program_path}/{language_path}",
                f"{program_path}-in-{language_path}",
                status_code
            )

    return status_code


def _generate_image(temp_dir: str, src: str, dest_filename_no_ext: str, status_code: int) -> int:
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
                "--path", str(src_image_path),
                "--output", temp_dir,
                "--logo", logo,
                "--no_title"
            ],
            check=True
        )
        temp_image_path = next(pathlib.Path(temp_dir).iterdir())
        shutil.move(temp_image_path, dest_image_path)
    except subprocess.CalledProcessError as exc:
        log.error("image-titler exited with %d status", exc.returncode)
        status_code = 1

    return status_code


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
    logging.basicConfig(format="%(name)-12s | %(levelname)-8s | %(message)s", level=logging.INFO)
    clean("docs/projects")
    clean("docs/languages")
    clean(AUTO_GEN_TEST_DOC_DIR)

    subete.repo.logger.setLevel(logging.WARNING)  # Reduce the noise of subete
    log.info("Loading repos (this may take several minutes)")
    repo = subete.load()

    generate_language_paths(repo)
    generate_auto_gen_test_docs(repo)
    generate_project_paths(repo)
    generate_sample_programs(repo)
    generate_languages_index(repo)
    generate_projects_index(repo)
    status_code = generate_images(repo)
    sys.exit(status_code)
