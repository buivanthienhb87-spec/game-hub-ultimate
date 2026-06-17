from __future__ import annotations
import json
from pathlib import Path
from .catalog import GameResource, build_index

def export_index(resources: list[GameResource], output_path: str) -> None:
    index = build_index(resources)
    Path(output_path).write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")

def load_resources(path: str) -> list[GameResource]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [GameResource(**item) for item in data]
