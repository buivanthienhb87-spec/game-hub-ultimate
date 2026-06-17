from game_hub_ultimate.catalog import GameResource, build_index

resources = [
    GameResource("Beginner Guide", "guide", "pc", "Introductory player guide"),
    GameResource("Patch Archive", "patch-notes", "cross-platform", "Update index"),
]
print(build_index(resources))
