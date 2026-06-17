from game_hub_ultimate.catalog import GameResource, build_index, filter_resources


def test_filter_resources_by_category():
    resources = [
        GameResource("Beginner Guide", "guide", "pc", "Start here"),
        GameResource("Patch Archive", "patch-notes", "pc", "Updates"),
    ]
    assert [item.title for item in filter_resources(resources, category="guide")] == ["Beginner Guide"]


def test_build_index_groups_titles():
    resources = [GameResource("A", "guide", "pc", ""), GameResource("B", "guide", "mobile", "")]
    assert build_index(resources) == {"guide": ["A", "B"]}
