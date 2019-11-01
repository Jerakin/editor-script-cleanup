#!/usr/bin/env python3
from pathlib import Path
import deftree


def clean_gui(project_path, gui_file):
    tree = deftree.parse(gui_file)

    output = []
    output.extend(clean_textures(tree))
    output.extend(clean_layers(tree))
    output.extend(clean_fonts(tree))
    output.extend(clean_spine_scenes(tree))
    if output:
        output.insert(0, gui_file.relative_to(project_path))
    else:
        output.append("No obsolete resources found")

    for line in output:
        print(line)


def resource_used_in_scene(root, resource_name):
    used_resource = list()
    for x in root.iter_elements("nodes"):
        if not x:
            continue
        resource = x.get_attribute(resource_name)
        if resource:
            atlas = resource.value.split("/")[0]
            if atlas and atlas not in used_resource:
                used_resource.append(atlas)
    return used_resource


def clean_textures(tree):
    out = []
    root = tree.get_root()
    gui_file = tree.get_document_path()
    # CLEAN UP TEXTURES
    for x in root.iter_elements("textures"):
        if not x:
            continue

        name_attr = x.get_attribute("name")

        if name_attr:
            name = name_attr.value
            if name not in resource_used_in_scene(root, "texture"):
                root.remove(x)
                out.append("  Atlas {}".format(name))
                tree.write(gui_file)
    return out


def clean_layers(tree):
    out = []
    root = tree.get_root()
    gui_file = tree.get_document_path()

    # CLEAN UP LAYERS
    for x in root.iter_elements("layers"):
        if not x:
            continue

        name_attr = x.get_attribute("name")
        if name_attr:
            name = name_attr.value
            if name not in resource_used_in_scene(root, "layer"):
                root.remove(x)
                out.append("  Layer {}".format(name))
                tree.write(gui_file)
    return out


def clean_fonts(tree):
    out = []
    root = tree.get_root()
    gui_file = tree.get_document_path()

    # CLEAN UP FONTS
    for x in root.iter_elements("fonts"):
        if not x:
            continue

        name_attr = x.get_attribute("name")
        if name_attr and name_attr not in ["puzzle_ja", "puzzle_zh", "zh", "ja", "ko", "zh_CN"]:
            name = name_attr.value
            if name not in resource_used_in_scene(root, "font"):
                root.remove(x)
                out.append("  Font {}".format(name))
                tree.write(gui_file)
    return out


def clean_spine_scenes(tree):
    out = []
    root = tree.get_root()
    gui_file = tree.get_document_path()

    # CLEAN UP SPINE
    for x in root.iter_elements("spine_scenes"):
        if not x:
            continue

        name_attr = x.get_attribute("name")
        if name_attr:
            name = name_attr.value
            if name not in resource_used_in_scene(root, "spine_scene"):
                root.remove(x)
                out.append("  Spine Scene {}".format(name))
                tree.write(gui_file)
    return out


def main():
    project_path = Path().cwd()
    g = '**/*.gui'
    for gui in project_path.glob(g):
        clean_gui(project_path, gui)


if __name__ == '__main__':
    print("Running Clean GUI")
    main()
