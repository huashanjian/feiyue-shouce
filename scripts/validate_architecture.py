from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONFIG = ROOT / "mkdocs.yml"

REQUIRED_TOP_LEVEL = {
    "start-here",
    "admissions",
    "majors",
    "universities",
    "campus-life",
    "pathways",
    "cases",
    "commons",
}

NON_CONTENT_TOP_LEVEL = {
    "assets",
    "javascripts",
    "overrides",
    "stylesheets",
}

LEGACY_PATH_PARTS = {
    "zhuanye",
    "yuanxiao",
    "zhiyuan",
    "zaixiao",
    "shenzao",
    "qiuzhi",
    "fulu",
}

KEBAB_PART = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOWER_FILE = re.compile(r"^[a-z0-9][a-z0-9.-]*$")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def iter_nav_paths(node: Any) -> list[str]:
    paths: list[str] = []
    if isinstance(node, str):
        paths.append(node)
    elif isinstance(node, list):
        for item in node:
            paths.extend(iter_nav_paths(item))
    elif isinstance(node, dict):
        for value in node.values():
            paths.extend(iter_nav_paths(value))
    return paths


def validate_path_names(errors: list[str]) -> None:
    allowed_top = REQUIRED_TOP_LEVEL | NON_CONTENT_TOP_LEVEL
    for child in DOCS.iterdir():
        if child.is_dir() and child.name not in allowed_top:
            fail(f"unexpected top-level docs directory: {child.relative_to(ROOT)}", errors)

    for path in DOCS.rglob("*"):
        rel = path.relative_to(DOCS)
        lower_parts = {part.lower() for part in rel.parts}
        legacy_hits = lower_parts & LEGACY_PATH_PARTS
        if legacy_hits:
            fail(f"legacy pinyin path part in {path.relative_to(ROOT)}: {sorted(legacy_hits)}", errors)

        if path.is_dir():
            if not KEBAB_PART.fullmatch(path.name):
                fail(f"directory name must be lowercase kebab-case: {path.relative_to(ROOT)}", errors)
            continue

        if path.name in {"CNAME"}:
            continue
        if not LOWER_FILE.fullmatch(path.name):
            fail(f"file name must be lowercase: {path.relative_to(ROOT)}", errors)


def validate_required_indexes(errors: list[str]) -> None:
    for name in sorted(REQUIRED_TOP_LEVEL):
        index = DOCS / name / "index.md"
        if not index.exists():
            fail(f"missing first-level index: {index.relative_to(ROOT)}", errors)


def validate_c_class_containers(errors: list[str]) -> None:
    for directory in DOCS.rglob("perspectives"):
        guide = directory / "how-to-contribute.md"
        if not guide.exists():
            fail(f"missing perspectives contribution guide: {guide.relative_to(ROOT)}", errors)

    for required in [
        DOCS / "cases" / "how-to-contribute.md",
        DOCS / "commons" / "stories" / "how-to-contribute.md",
    ]:
        if not required.exists():
            fail(f"missing contribution guide: {required.relative_to(ROOT)}", errors)


def validate_nav(errors: list[str]) -> None:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    nav_paths = iter_nav_paths(config.get("nav", []))
    for raw_path in nav_paths:
        if "://" in raw_path:
            continue
        path = raw_path.split("#", 1)[0]
        if not path:
            continue
        target = DOCS / path
        if not target.exists():
            fail(f"nav target does not exist: {path}", errors)
        lowered = {part.lower() for part in Path(path).parts}
        legacy_hits = lowered & LEGACY_PATH_PARTS
        if legacy_hits:
            fail(f"nav uses legacy pinyin path part in {path}: {sorted(legacy_hits)}", errors)


def validate_public_boundary(errors: list[str]) -> None:
    required_phrase = "未来可能被莞言瓜语转载"
    files = [
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github" / "pull_request_template.md",
        DOCS / "cases" / "templates" / "case-template.md",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        if required_phrase not in text:
            fail(f"missing public repost notice phrase: {path.relative_to(ROOT)}", errors)


def main() -> int:
    errors: list[str] = []
    validate_path_names(errors)
    validate_required_indexes(errors)
    validate_c_class_containers(errors)
    validate_nav(errors)
    validate_public_boundary(errors)

    if errors:
        print("Architecture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Architecture validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
