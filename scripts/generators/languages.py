import datetime
import logging
from pathlib import Path

import snakemd
import subete
from assets.image_lookup import find_default_language_image, find_language_image
from constants import LANGUAGE_MD_FILENAMES
from markdown.articles import add_language_article_section
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section
from repo.queries import get_program_datetimes
from utils.plural import is_are, pluralize
from utils.text import markdown_escape

log = logging.getLogger(__name__)


def generate_language_index(repo: subete.Repo, language: subete.LanguageCollection) -> None:
    """Creates a language file for a single language. The path is assumed
    to be `languages/language/index.md`.

    :param subete.LanguageCollection language: the collection sample programs for a language.
    """
    doc: snakemd.Document = snakemd.new_doc()
    times: list[datetime.datetime | None] = []
    for program in language:
        program: subete.SampleProgram
        times += get_program_datetimes(program)

    times += [language.doc_created(), language.doc_modified()]

    doc_authors: set[str] = language.doc_authors()
    language_escaped = markdown_escape(language.name())
    generate_front_matter(
        doc,
        f"The {language} Programming Language",
        times=times,
        image=find_language_image(language),
        authors=doc_authors,
        tags=[language.pathlike_name()],
    )
    generate_no_edit_note(doc, "languages", language.pathlike_name(), LANGUAGE_MD_FILENAMES)
    doc.add_paragraph(
        f"Welcome to the {language_escaped} page! Here, you'll find a description "
        f"of the language as well as a list of sample programs "
        f"in that language.",
    )
    if doc_authors:
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    add_section(doc, "languages", language.pathlike_name(), "Description")
    add_language_article_section(doc, repo, str(language))
    try:
        doc.dump("index", directory=f"docs/languages/{language.pathlike_name()}")
    except Exception:
        log.exception(f"Failed to write {language.pathlike_name()}")


def generate_language_paths(repo: subete.Repo) -> None:
    """Creates the language directory which contains all of the language folders
    and index.md files.

    :param subete.Repo repo: the repo to pull from.
    """
    for language in repo:
        log.info("Generating language paths for %s", str(language))
        language: subete.LanguageCollection
        path = Path(f"docs/languages/{language.pathlike_name()}")
        path.mkdir(exist_ok=True, parents=True)
        generate_language_index(repo, language)


def get_language_letter_links(repo: subete.Repo) -> str:
    # Have to use raw HTML for this since there is no way to add a class attribute
    # in Markdown
    language_letter_links = (
        [
            '<ul class="letter-link">',
        ]
        + [
            f'    <li><a href="#{letter.lower()}">{letter.upper()}</a></li>'
            for letter in repo.sorted_language_letters()
        ]
        + [
            "</ul>",
        ]
    )
    return "\n".join(language_letter_links)


def generate_languages_index(repo: subete.Repo) -> None:
    """Creates the index.md files for the root directories.

    :param subete.Repo repo: the repo to pull from.
    """
    log.info("Generating language index")
    language_index_path = Path("docs/languages")
    times: list[datetime.datetime | None] = []
    for language in repo:
        language: subete.LanguageCollection
        for program in language:
            program: subete.SampleProgram
            times += get_program_datetimes(program)

    language_index = snakemd.new_doc()
    generate_front_matter(
        language_index,
        "Programming Languages",
        times=times,
        image=find_default_language_image(),
    )
    num_languages = len(list(repo))
    verb = is_are(num_languages)
    singular = pluralize(num_languages, "language")
    welcome_text = (
        "Welcome to the Languages page! Here, you'll find a list of all of the languages represented in the collection. "
        f"At this time, there {verb} {num_languages} {singular}, of which {repo.total_tests()} are tested"
    )
    untestables = repo.total_untestables()
    if untestables:
        verb_untestables = is_are(untestables)
        welcome_text += f", {untestables} {verb_untestables} untestable"

    num_programs = repo.total_programs()
    singular = pluralize(num_programs, "snippet")
    welcome_text += f", and {num_programs} code {singular}."
    language_index.add_paragraph(welcome_text)

    language_index.add_heading("Language Breakdown", level=2)
    generate_language_breakdown_percentage(repo, language_index)

    language_index.add_heading("Language Collections by Letter", level=2)
    language_index.add_paragraph(
        "To help you navigate the collection, the following languages are organized alphabetically and grouped by first letter. "
        "To go to a particular letter, just click one of the links below.",
    )
    language_index.add_raw(get_language_letter_links(repo))

    return_to_top = [
        "&laquo; ",
        snakemd.Inline("Return to Top", link="#language-collections-by-letter"),
        " &raquo;",
    ]
    language_index.add_block(
        snakemd.Paragraph(["To return here, just click the "] + return_to_top + [" link."]),
    )

    for letter in repo.sorted_language_letters():
        language_index.add_heading(letter.upper(), level=3)
        languages: list[subete.LanguageCollection] = repo.languages_by_letter(letter)
        snippets = sum(language.total_programs() for language in languages)
        tests = sum(1 if language.has_testinfo() else 0 for language in languages)
        untestables = sum(1 if language.has_untestable_info() else 0 for language in languages)
        verb = is_are(tests)
        num_languages = len(languages)
        singular = pluralize(tests, "language")
        verb_untestables = is_are(untestables)
        language_statement = (
            f"The '{letter.upper()}' collection contains {num_languages} {singular}, "
            f"of which {tests} {verb} tested"
        )
        if untestables:
            language_statement += f", {untestables} {verb_untestables} untestable"

        language_index.add_paragraph(f"{language_statement}, and {snippets} code snippets.")
        languages.sort(key=lambda x: x.name().casefold())
        languages_list = [get_language_link_and_testability(x) for x in languages]
        language_index.add_block(snakemd.MDList(languages_list))
        language_index.add_block(snakemd.Paragraph(return_to_top))

    language_index.dump("index", directory=str(language_index_path))


def get_language_link_and_testability(
    language: subete.LanguageCollection,
) -> snakemd.Paragraph:
    language_escaped = markdown_escape(language.name())
    language_link = snakemd.Inline(language_escaped, link=language.lang_docs_url())
    num_programs = language.total_programs()
    singular = pluralize(num_programs, "code snippet")
    phrase = f"{num_programs} {singular}"
    if language.has_testinfo():
        return snakemd.Paragraph([language_link, f" ({phrase})"])

    if language.has_untestable_info():
        testability = [
            f" ({phrase}, ",
            snakemd.Inline("untestabled", link=language.untestable_info_url()),
            ")",
        ]
    else:
        testability = [snakemd.Inline(f" {phrase}, (untested)")]

    return snakemd.Paragraph([language_link] + testability)


def generate_language_breakdown_percentage(repo: subete.Repo, doc: snakemd.Document):
    language_info = sorted(
        ((language.name(), language.percentage(), language.color()) for language in repo),
        key=lambda x: (-x[1], x[0]),
    )
    max_language_percentage = language_info[0][1]

    doc.add_paragraph("Here are the percentages for each language in the collection:")
    doc.add_raw(
        """\
<details>
<summary>Click here to expand or collapse...</summary>
<table class="bar-graph">""",
    )

    for language_name, percentage, color in language_info:
        bar_graph_width = 100.0 * percentage / max_language_percentage
        bar_graph_style = f"width: {bar_graph_width:.2f}%; background-color: {color};"
        doc.add_raw(
            f"""\
    <tr>
        <td class="right nowrap">{language_name}</td>
        <td class="right">{percentage:.2f}%</td>
        <td class="bar-graph"><div style="{bar_graph_style}"></div></td> 
    </tr>""",
        )

    doc.add_raw(
        """\
</table>
</details>""",
    )
