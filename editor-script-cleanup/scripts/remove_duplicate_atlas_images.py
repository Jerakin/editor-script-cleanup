#!/usr/bin/env python3
from pathlib import Path

import deftree


def get_files(project_root, ending):
    """Generator to get files"""
    g = '**/*.{}'.format(ending)
    for f in project_root.glob(g):
        yield f


def list_duplicates(root: deftree.Element):
    # adds all elements it haven't seen to set(seen) and all other to seen_twice
    seen = list()
    seen_twice = list()
    for image_element in root.elements("images"):
        image = image_element.get_attribute("image")
        if image.value in seen:
            seen_twice.append(image)
        else:
            seen.append(image.value)

    return seen_twice


def remove_duplicates(atlas):
    """Remove all duplicated image entries in the atlas"""
    tree = deftree.DefTree()
    root = tree.parse(atlas)

    duplicated_images = []
    duplicated_images.extend(list_duplicates(root))

    for animation in root.elements("animations"):
        duplicated_images.extend(list_duplicates(animation))

    for duplicate in duplicated_images:
        print("    Removed {}".format(duplicate.value))
        image_element = duplicate.get_parent()
        image_element.get_parent().remove(image_element)

    tree.write(atlas)


def clean_up_all_atlases(project_folder):
    """Remove all missing image in entries in the project"""
    for atlas in get_files(project_folder, "atlas"):
        print("  Cleaning", atlas.relative_to(project_folder))
        remove_duplicates(atlas)


def main():
    path = Path().cwd()
    clean_up_all_atlases(path)


if __name__ == '__main__':
    print("Running Remove Duplicate Images")
    main()

