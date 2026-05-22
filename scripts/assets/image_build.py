import logging
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

import subete
from constants import (
    DEFAULT_LANGUAGE_IMAGE_NO_EXT,
    DEFAULT_PROGRAM_IMAGE_NO_EXT,
    DEFAULT_PROJECT_IMAGE_NO_EXT,
    LANGUAGES_DIR,
    PROGRAMS_DIR,
    PROJECTS_DIR,
    SOURCE_DIR,
)
from utils.files import mkdir

log = logging.getLogger(__name__)

ASSETS_DIR = Path("docs/assets/images")
LOGO_PATH = ASSETS_DIR / "icon-small.png"

FEATURED_GLOB = "featured-image.*"


@dataclass(frozen=True)
class ImageSpec:
    src_dir: Path
    dest_no_ext: str


def generate_images(repo: subete.Repo, workers: int = 8) -> int:
    """Generate all processed images using image-titler.

    Returns:
        0 if all succeeded, 1 if any failed.

    """
    specs = [
        *_language_specs(repo),
        *_project_specs(repo),
        *_program_specs(repo),
    ]

    failures = _run_parallel(specs, workers=workers)
    return 1 if failures else 0


def _run_parallel(specs: list[ImageSpec], workers: int) -> list[ImageSpec]:
    failures: list[ImageSpec] = []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        future_map = {pool.submit(_process_spec, spec): spec for spec in specs}

        for future in as_completed(future_map):
            spec = future_map[future]
            try:
                if not future.result():
                    failures.append(spec)
            except Exception:
                log.exception("Unexpected failure: %s", spec)
                failures.append(spec)

    for spec in failures:
        log.error("Failed image spec: %s", spec)

    return failures


def _process_spec(spec: ImageSpec) -> bool:
    src_image = _find_featured_image(spec.src_dir)
    if src_image is None:
        return True

    dest_path = ASSETS_DIR / f"{spec.dest_no_ext}{src_image.suffix}"
    _ = mkdir(dest_path.parent)

    log.info("Processing %s -> %s", src_image, dest_path)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        try:
            subprocess.run(
                [
                    "image-titler",
                    "--path",
                    str(src_image),
                    "--output",
                    str(tmp_dir),
                    "--logo",
                    str(LOGO_PATH),
                    "--no_title",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            produced = _pick_output(tmp_dir)
            if produced is None:
                log.error("No output produced for %s", src_image)
                return False

            _safe_move(produced, dest_path)
            return True

        except subprocess.CalledProcessError:
            log.exception("image-titler failed for %s", src_image)
            return False


def _pick_output(tmp_dir: Path) -> Path | None:
    """Pick deterministic output file."""
    files = sorted(p for p in tmp_dir.iterdir() if p.is_file())
    return files[0] if files else None


def _safe_move(src: Path, dest: Path) -> None:
    """Move file without crashing on existing destination."""
    if dest.exists():
        log.warning("Overwriting existing file: %s", dest)
        dest.unlink()

    shutil.move(str(src), str(dest))


def _find_featured_image(dir_path: Path) -> Path | None:
    if not dir_path.is_dir():
        return None
    return next(dir_path.glob(FEATURED_GLOB), None)


def _language_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [ImageSpec(LANGUAGES_DIR, DEFAULT_LANGUAGE_IMAGE_NO_EXT)]

    for lang in repo:
        name = lang.pathlike_name()
        specs.append(
            ImageSpec(LANGUAGES_DIR / name, f"the-{name}-programming-language"),
        )

    return specs


def _project_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [ImageSpec(PROJECTS_DIR, DEFAULT_PROJECT_IMAGE_NO_EXT)]

    for project in repo.approved_projects():
        name = project.pathlike_name()
        specs.append(
            ImageSpec(PROJECTS_DIR / name, f"{name}-in-every-language"),
        )

    return specs


def _program_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [ImageSpec(SOURCE_DIR, DEFAULT_PROGRAM_IMAGE_NO_EXT)]

    for lang in repo:
        lang_name = lang.pathlike_name()

        for program in repo[str(lang)]:
            proj = program.project_pathlike_name()
            specs.append(
                ImageSpec(
                    PROGRAMS_DIR / proj / lang_name,
                    f"{proj}-in-{lang_name}",
                ),
            )

    return specs
