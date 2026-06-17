from game_hub_ultimate.catalog import GameResource
from game_hub_ultimate.export import export_index, load_resources
import json, tempfile, os

def test_export_and_load_roundtrip():
    resources = [GameResource("Guide A", "guide", "pc", "Summary")]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        export_index(resources, f.name)
        path = f.name
    loaded = load_resources(path)
    os.unlink(path)
    assert loaded[0].title == "Guide A"
