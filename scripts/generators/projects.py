import datetime
import logging
from pathlib import Path

import snakemd
import subete
from assets.images import get_default_project_image, get_project_image
from constants import PROJECT_MD_FILENAMES
from markdown.articles import add_project_article_section
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section, add_testing_section
from repo.queries import get_program_datetimes

log = logging.getLogger(__name__)


def generate_project_paths(repo: subete.Repo) -> None:
    """Creates the project directory which contains all of the project folders
    and index.md files.

    :param subete.Repo repo: the repo to pull from.
    """
    projects = repo.approved_projects()
    projects.sort(key=lambda x: x.name().casefold())
    for i, project in enumerate(projects):
        project: subete.Project
        log.info("Generating project paths for %s", str(project))
        path = Path(f"docs/projects/{project.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        generate_project_index(repo, project, projects[i - 1], projects[(i + 1) % len(projects)])


def generate_project_index(
    repo: subete.Repo,
    project: subete.Project,
    previous: subete.Project,
    next: subete.Project,
) -> None:
    """Creates an index file for a single project. The path is assumed
    to be `projects/project/index.md`.

    :param subete.Repo repo: the repo to pull from.
    :param subete.Project project: the project to create the index file
        for in the normalized form (e.g., hello-world).
    :param subete.Project previous: the previous project alphabetically.
    :param subete.Project next: the next project alphabetically.
    """
    doc: snakemd.Document = snakemd.new_doc()
    project_name: str = project.name()
    times: list[datetime.datetime | None] = [project.doc_created(), project.doc_modified()]
    for language in repo:
        for program in language:
            if program.project_name() == project_name:
                times += get_program_datetimes(program)

    generate_front_matter(
        doc,
        project.name(),
        image=get_project_image(project),
        times=times,
        tags=[project.pathlike_name()],
    )
    generate_no_edit_note(doc, "projects", project.pathlike_name(), PROJECT_MD_FILENAMES)
    doc.add_paragraph(
        f"Welcome to the {project.name()} page! Here, you'll find a description "
        f"of the project as well as a list of sample programs "
        f"written in various languages.",
    )
    doc_authors: set[str] = project.doc_authors()
    if doc_authors:
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    add_section(doc, "projects", project.pathlike_name(), "Description")
    add_section(doc, "projects", project.pathlike_name(), "Requirements")
    add_testing_section(doc, "projects", project.pathlike_name())
    if not project.has_testing():
        doc.add_block(
            snakemd.Paragraph(
                [
                    snakemd.Inline("Note:", bold=True),
                    f" {project.name()} is not currently tested by Glotter2. Consider contributing!",
                ],
            ),
        )

    add_project_article_section(doc, repo, project)
    doc.add_horizontal_rule()
    doc.add_paragraph('<nav class="project-nav">')
    doc.add_paragraph('<div id="prev" markdown="1">')
    doc.add_block(
        snakemd.Paragraph(
            [
                snakemd.Inline(
                    f"<-- Previous Project ({previous})",
                    link=previous.requirements_url(),
                ),
            ],
        ),
    )
    doc.add_paragraph("</div>")
    doc.add_paragraph('<div id="next" markdown="1">')
    doc.add_block(
        snakemd.Paragraph(
            [snakemd.Inline(f"Next Project ({next}) -->", link=next.requirements_url())],
        ),
    )
    doc.add_paragraph("</div>")
    doc.add_paragraph("</nav>")
    doc.dump("index", directory=f"docs/projects/{project.pathlike_name()}")


def generate_projects_index(repo: subete.Repo) -> None:
    """Generate index.md for file for Projects page

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating projects index")
    projects_index_path = Path("docs/projects")
    projects_index: snakemd.Document = snakemd.new_doc()
    times: list[datetime.datetime | None] = []
    for language in repo:
        language: subete.LanguageCollection
        for program in language:
            program: subete.SampleProgram
            times += get_program_datetimes(program)

    generate_front_matter(
        projects_index,
        "Programming Projects in Every Language",
        times=times,
        image=get_default_project_image(),
    )
    project_tests = sum(1 if project.has_testing() else 0 for project in repo.approved_projects())
    projects_index.add_paragraph(
        "Welcome to the Projects page! Here, you'll find a list of all of the projects represented in the collection. "
        f"At this time, the repo supports {repo.total_approved_projects()} projects, of which {project_tests} are tested.",
    )
    projects_index.add_heading("Projects List", level=2)
    projects_index.add_paragraph(
        "To help you navigate the collection, the following projects are organized alphabetically.",
    )
    repo.approved_projects().sort(key=lambda x: x.name().casefold())
    projects = [
        snakemd.Inline(
            project.name(),
            link=project.requirements_url(),
        )
        for project in repo.approved_projects()
    ]
    projects_index.add_block(snakemd.MDList(projects))
    projects_index.dump("index", directory=str(projects_index_path))
