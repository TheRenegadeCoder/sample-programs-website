import logging
import shutil
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

import subete
from constants import LANGUAGES_DIR, PROGRAMS_DIR, PROJECTS_DIR
from subete import imghdr
from utils.files import mkdir

log = logging.getLogger(__name__)

ASSETS_ROOT = Path("docs/assets/images")


@dataclass(frozen=True)
class CopySpec:
    src_dir: Path
    dest_dir: Path


def copy_article_images(repo: subete.Repo) -> None:
    """Copy all article images (languages, projects, programs)."""
    specs = _build_specs(repo)

    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(_copy_images, spec) for spec in specs]

        for f in as_completed(futures):
            try:
                f.result()
            except Exception:
                log.exception("Failed copying images")


def _build_specs(repo: subete.Repo) -> Iterable[CopySpec]:
    yield from _language_specs(repo)
    yield from _project_specs(repo)
    yield from _program_specs(repo)


def _language_specs(repo: subete.Repo) -> Iterable[CopySpec]:
    for lang in repo:
        name = lang.pathlike_name()
        yield CopySpec(
            LANGUAGES_DIR / name,
            ASSETS_ROOT / "languages" / name,
        )


def _project_specs(repo: subete.Repo) -> Iterable[CopySpec]:
    for project in repo.approved_projects():
        name = project.pathlike_name()
        yield CopySpec(
            PROJECTS_DIR / name,
            ASSETS_ROOT / "projects" / name,
        )


def _program_specs(repo: subete.Repo) -> Iterable[CopySpec]:
    for lang in repo:
        lang_name = lang.pathlike_name()

        for program in repo[str(lang)]:
            proj = program.project_pathlike_name()
            yield CopySpec(
                PROGRAMS_DIR / proj / lang_name,
                ASSETS_ROOT / "projects" / proj / lang_name,
            )


def _copy_images(spec: CopySpec) -> None:
    if not spec.src_dir.is_dir():
        return

    images = _list_images(spec.src_dir)
    if not images:
        return

    _ = mkdir(spec.dest_dir)

    for src in images:
        dest = spec.dest_dir / src.name
        log.info("Copying %s -> %s", src, dest)
        shutil.copy2(src, dest)


def _list_images(src_dir: Path) -> list[Path]:
    if not src_dir.is_dir():
        return []

    return [
        p
        for p in src_dir.iterdir()
        if p.is_file() and p.stem != "featured-image" and imghdr.what(p)
    ]
