import logging
from collections import defaultdict
from pathlib import Path

import snakemd
import subete
from assets.image_lookup import find_project_image, get_default_project_image
from constants import PROJECT_MD_FILENAMES
from markdown.articles import add_project_article_section
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section, add_testing_section
from repo.queries import get_program_datetimes
from utils.files import mkdir
from utils.plural import is_are, pluralize

log = logging.getLogger(__name__)

DOCS_PROJECTS_DIR = Path("docs/projects")


def generate_project_paths(repo: subete.Repo) -> None:
    """Creates the project directories and triggers individual index generation.

    Args:
        repo: The subete Repository instance to pull data from.

    """
    projects = sorted(repo.approved_projects(), key=lambda x: x.name().casefold())
    project_datetime_map = _map_program_datetimes_by_project(repo)
    num_projects = len(projects)

    for i, project in enumerate(projects):
        log.info("Generating project paths for %s", project)

        target_dir = DOCS_PROJECTS_DIR / project.pathlike_name()
        mkdir(target_dir)

        prev_project = projects[i - 1]
        next_project = projects[(i + 1) % num_projects]

        generate_project_index(
            repo=repo,
            project=project,
            prev_project=prev_project,
            next_project=next_project,
            target_dir=target_dir,
            program_times=project_datetime_map.get(project.name(), []),
        )


def generate_project_index(
    repo: subete.Repo,
    project: subete.Project,
    prev_project: subete.Project,
    next_project: subete.Project,
    target_dir: Path,
    program_times: list,
) -> None:
    """Creates a markdown index file for a single project.

    Args:
        repo: The subete Repository instance.
        project: The target subete Project instance to document.
        prev_project: The alphabetically previous project instance.
        next_project: The alphabetically next project instance.
        target_dir: The resolve Path destination directory for the index.
        program_times: Pre-collected program datetimes matching this project.

    """
    path_name = project.pathlike_name()
    doc = snakemd.new_doc()

    times = [project.doc_created(), project.doc_modified()] + program_times

    generate_front_matter(
        doc,
        project.name(),
        image=find_project_image(project),
        times=times,
        tags=[path_name],
    )
    generate_no_edit_note(doc, "projects", path_name, PROJECT_MD_FILENAMES)

    doc.add_paragraph(
        f"Welcome to the {project.name()} page! Here, you'll find a description "
        f"of the project as well as a list of sample programs written in various languages.",
    )

    if doc_authors := project.doc_authors():
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    add_section(doc, "projects", path_name, "Description")
    add_section(doc, "projects", path_name, "Requirements")
    add_testing_section(doc, "projects", path_name)

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

    _add_navigation_footer(doc, prev_project, next_project)

    doc.dump("index", directory=str(target_dir))


def generate_projects_index(repo: subete.Repo) -> None:
    """Generates the comprehensive master index.md for the main Projects page.

    Args:
        repo: The subete Repository instance to pull data from.

    """
    log.info("Generating projects index")
    projects_index = snakemd.new_doc()

    times = [
        dt for language in repo for program in language for dt in get_program_datetimes(program)
    ]

    generate_front_matter(
        projects_index,
        "Programming Projects in Every Language",
        times=times,
        image=get_default_project_image(),
    )

    sorted_projects = sorted(repo.approved_projects(), key=lambda x: x.name().casefold())
    num_projects = len(sorted_projects)
    project_tests = sum(1 for project in sorted_projects if project.has_testing())

    projects_index.add_paragraph(
        "Welcome to the Projects page! Here, you'll find a list of all of the projects represented in the collection. "
        f"At this time, the repo supports {pluralize(num_projects, 'project')}, of which "
        f"{project_tests} {is_are(project_tests)} tested.",
    )
    projects_index.add_heading("Projects List", level=2)
    projects_index.add_paragraph(
        "To help you navigate the collection, the following projects are organized alphabetically.",
    )

    project_links = [
        snakemd.Inline(project.name(), link=project.requirements_url())
        for project in sorted_projects
    ]
    projects_index.add_block(snakemd.MDList(project_links))
    projects_index.dump("index", directory=str(DOCS_PROJECTS_DIR))


def _map_program_datetimes_by_project(repo: subete.Repo) -> dict[str, list]:
    """Helper to group program datetimes by project name in a single pass."""
    mapping = defaultdict(list)
    for language in repo:
        for program in language:
            mapping[program.project_name()].extend(get_program_datetimes(program))
    return mapping


def _add_navigation_footer(
    doc: snakemd.Document,
    prev_proj: subete.Project,
    next_proj: subete.Project,
) -> None:
    """Appends the custom HTML/Markdown pagination elements to the bottom of the document."""
    doc.add_paragraph('<nav class="project-nav">')
    doc.add_paragraph('<div id="prev" markdown="1">')
    doc.add_block(
        snakemd.Paragraph(
            [
                snakemd.Inline(
                    f"<-- Previous Project ({prev_proj})",
                    link=prev_proj.requirements_url(),
                ),
            ],
        ),
    )
    doc.add_paragraph("</div>")
    doc.add_paragraph('<div id="next" markdown="1">')
    doc.add_block(
        snakemd.Paragraph(
            [snakemd.Inline(f"Next Project ({next_proj}) -->", link=next_proj.requirements_url())],
        ),
    )
    doc.add_paragraph("</div>")
    doc.add_paragraph("</nav>")
