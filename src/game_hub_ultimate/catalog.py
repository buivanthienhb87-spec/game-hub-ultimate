from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class GameResource:
    title: str
    category: str
    platform: str
    summary: str
    source_url: str = ""
    tags: tuple[str, ...] = ()


def filter_resources(resources: Sequence[GameResource], *, category: str | None = None, platform: str | None = None) -> list[GameResource]:
    result: list[GameResource] = []
    for resource in resources:
        if category and resource.category.lower() != category.lower():
            continue
        if platform and resource.platform.lower() != platform.lower():
            continue
        result.append(resource)
    return result


def build_index(resources: Iterable[GameResource]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for resource in resources:
        index.setdefault(resource.category, []).append(resource.title)
    return {key: sorted(values) for key, values in sorted(index.items())}
