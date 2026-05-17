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
)

log = logging.getLogger(__name__)

ASSETS_DIR = Path("docs/assets/images")
LOGO_PATH = ASSETS_DIR / "icon-small.png"


@dataclass(frozen=True)
class ImageSpec:
    src_dir: Path
    dest_no_ext: str


def generate_images(repo: subete.Repo) -> int:
    """Generate all processed images using image-titler.

    Returns:
        0 if all succeeded, 1 if any failed.

    """
    specs = [
        *_language_specs(repo),
        *_project_specs(repo),
        *_program_specs(repo),
    ]

    return 1 if _run_parallel(specs) else 0


def _run_parallel(specs: list[ImageSpec], workers: int = 8) -> list[ImageSpec]:
    failures: list[ImageSpec] = []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_process_spec, spec): spec for spec in specs}

        for future in as_completed(futures):
            spec = futures[future]
            try:
                if not future.result():
                    failures.append(spec)
            except Exception:
                log.exception("Unexpected failure: %s", spec)
                failures.append(spec)

    for spec in failures:
        log.error("Failed image: %s", spec)

    return failures


def _process_spec(spec: ImageSpec) -> bool:
    src_image = _find_featured_image(spec.src_dir)
    if src_image is None:
        return True  # treat missing as OK

    dest_path = ASSETS_DIR / f"{spec.dest_no_ext}{src_image.suffix}"

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
            )

            produced_files = list(tmp_dir.iterdir())
            if not produced_files:
                log.error("No output generated for %s", src_image)
                return False

            shutil.move(produced_files[0], dest_path)
            return True

        except subprocess.CalledProcessError:
            log.exception("image-titler failed for %s", src_image)
            return False


def _find_featured_image(dir_path: Path) -> Path | None:
    if not dir_path.exists():
        return None
    return next(dir_path.glob("featured-image.*"), None)


def _language_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [
        ImageSpec(Path("sources/languages"), DEFAULT_LANGUAGE_IMAGE_NO_EXT),
    ]

    for lang in repo:
        name = lang.pathlike_name()
        specs.append(
            ImageSpec(
                Path("sources/languages") / name,
                f"the-{name}-programming-language",
            ),
        )

    return specs


def _project_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [
        ImageSpec(Path("sources/projects"), DEFAULT_PROJECT_IMAGE_NO_EXT),
    ]

    for project in repo.approved_projects():
        name = project.pathlike_name()
        specs.append(
            ImageSpec(
                Path("sources/projects") / name,
                f"{name}-in-every-language",
            ),
        )

    return specs


def _program_specs(repo: subete.Repo) -> list[ImageSpec]:
    specs = [
        ImageSpec(Path("sources"), DEFAULT_PROGRAM_IMAGE_NO_EXT),
    ]

    for lang in repo:
        lang_name = lang.pathlike_name()

        for program in repo[str(lang)]:
            proj = program.project_pathlike_name()

            specs.append(
                ImageSpec(
                    Path("sources/programs") / proj / lang_name,
                    f"{proj}-in-{lang_name}",
                ),
            )

    return specs
