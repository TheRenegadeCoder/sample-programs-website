import logging
from pathlib import Path

import snakemd
import subete
from assets.image_lookup import find_language_image, get_default_language_image
from constants import LANGUAGE_MD_FILENAMES
from markdown.articles import add_language_article_section
from markdown.authors import add_authors_to_doc
from markdown.front_matter import generate_front_matter
from markdown.note import generate_no_edit_note
from markdown.sections import add_section
from repo.queries import get_program_datetimes
from utils.files import mkdir
from utils.plural import is_are, pluralize
from utils.text import markdown_escape

log = logging.getLogger(__name__)

DOCS_LANGUAGES_DIR = Path("docs/languages")


def generate_language_paths(repo: subete.Repo) -> None:
    """Creates the individual language directories and indexes.

    Args:
        repo: The subete Repository instance to pull data from.

    """
    for language in repo:
        log.info("Generating language paths for %s", language)
        target_dir = DOCS_LANGUAGES_DIR / language.pathlike_name()
        _ = mkdir(target_dir)
        generate_language_index(repo, language, target_dir)


def generate_language_index(
    repo: subete.Repo,
    language: subete.LanguageCollection,
    target_dir: Path,
) -> None:
    """Creates a markdown language documentation index file for a single language.

    Args:
        repo: The subete Repository instance.
        language: The targeted subete LanguageCollection.
        target_dir: The target Path directory to dump files into.

    """
    doc = snakemd.new_doc()

    times = [dt for program in language for dt in get_program_datetimes(program)]
    times.extend([language.doc_created(), language.doc_modified()])

    doc_authors = language.doc_authors()
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
        f"of the language as well as a list of sample programs in that language.",
    )

    if doc_authors:
        doc.add_paragraph("This article was written by:")
        add_authors_to_doc(doc, doc_authors)

    add_section(doc, "languages", language.pathlike_name(), "Description")
    add_language_article_section(doc, repo, str(language))

    try:
        doc.dump("index", directory=str(target_dir))
    except Exception:
        log.exception("Failed to write %s", language.pathlike_name())


def generate_languages_index(repo: subete.Repo) -> None:
    """Creates the central main index.md landing page for all Programming Languages.

    Args:
        repo: The subete Repository instance.

    """
    log.info("Generating language index")

    times = [
        dt for language in repo for program in language for dt in get_program_datetimes(program)
    ]

    language_index = snakemd.new_doc()
    generate_front_matter(
        language_index,
        "Programming Languages",
        times=times,
        image=get_default_language_image(),
    )

    total_languages = len(list(repo))
    welcome_text = (
        "Welcome to the Languages page! Here, you'll find a list of all of the languages represented in the collection. "
        f"At this time, there {is_are(total_languages)} {pluralize(total_languages, 'language')}, "
        f"of which {repo.total_tests()} are tested"
    )

    if untestables := repo.total_untestables():
        welcome_text += f", {untestables} {is_are(untestables)} untestable"

    total_programs = repo.total_programs()
    welcome_text += f", and {pluralize(total_programs, 'code snippet')}."
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
        languages = repo.languages_by_letter(letter)

        snippets = sum(lang.total_programs() for lang in languages)
        tests = sum(1 for lang in languages if lang.has_testinfo())
        letter_untestables = sum(1 for lang in languages if lang.has_untestable_info())

        num_languages = len(languages)
        language_statement = (
            f"The '{letter.upper()}' collection contains {pluralize(num_languages, 'language')}, "
            f"of which {tests} {is_are(tests)} tested"
        )
        if letter_untestables:
            language_statement += f", {letter_untestables} {is_are(letter_untestables)} untestable"

        language_index.add_paragraph(
            f"{language_statement}, and {pluralize(snippets, 'code snippet')}.",
        )

        languages.sort(key=lambda x: x.name().casefold())
        languages_list = [get_language_link_and_testability(x) for x in languages]
        language_index.add_block(snakemd.MDList(languages_list))
        language_index.add_block(snakemd.Paragraph(return_to_top))

    language_index.dump("index", directory=str(DOCS_LANGUAGES_DIR))


def get_language_letter_links(repo: subete.Repo) -> str:
    """Generates the sticky HTML fast-navigation link grid categorized by letter."""
    links = [
        f'    <li><a href="#{l.lower()}">{l.upper()}</a></li>'
        for l in repo.sorted_language_letters()
    ]
    return "\n".join(['<ul class="letter-link">'] + links + ["</ul>"])


def get_language_link_and_testability(language: subete.LanguageCollection) -> snakemd.Paragraph:
    """Generates a dynamic markdown paragraph item containing metadata markers for a language link."""
    language_escaped = markdown_escape(language.name())
    language_link = snakemd.Inline(language_escaped, link=language.lang_docs_url())

    phrase = pluralize(language.total_programs(), "code snippet")

    if language.has_testinfo():
        return snakemd.Paragraph([language_link, f" ({phrase})"])

    if language.has_untestable_info():
        testability = [
            f" ({phrase}, ",
            snakemd.Inline("untestabled", link=language.untestable_info_url()),
            ")",
        ]
    else:
        testability = [snakemd.Inline(f" ({phrase}, untested)")]

    return snakemd.Paragraph([language_link] + testability)


def generate_language_breakdown_percentage(repo: subete.Repo, doc: snakemd.Document) -> None:
    """Renders the stylized, expanded HTML table displaying language layout distributions."""
    language_info = sorted(
        ((lang.name(), lang.percentage(), lang.color()) for lang in repo),
        key=lambda x: (-x[1], x[0]),
    )
    max_percentage = language_info[0][1] if language_info else 1.0

    doc.add_paragraph("Here are the percentages for each language in the collection:")
    doc.add_raw(
        '<details>\n<summary>Click here to expand or collapse...</summary>\n<table class="bar-graph">',
    )

    for name, percentage, color in language_info:
        bar_width = 100.0 * percentage / max_percentage
        doc.add_raw(
            f"    <tr>\n"
            f'        <td class="right nowrap">{name}</td>\n'
            f'        <td class="right">{percentage:.2f}%</td>\n'
            f'        <td class="bar-graph"><div style="width: {bar_width:.2f}%; background-color: {color};"></div></td>\n'
            f"    </tr>",
        )

    doc.add_raw("</table>\n</details>")
