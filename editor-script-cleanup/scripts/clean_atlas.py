#!/usr/bin/env python3
from os.path import exists

_log_file = "python_log.txt"

if exists(_log_file):
    import sys
    import traceback

    def log_exception(a, b, tb):
        with open("python_log.txt", "a") as fp:
            traceback.print_tb(tb, file=fp)

    sys.stdout = open("python_log.txt", 'w')
    sys.excepthook = log_exception

from pathlib import Path

import deftree


def get_files(project_root, ending):
    """Generator to get files"""
    g = '**/*.{}'.format(ending)
    for f in project_root.glob(g):
        yield f


def missing_images_in_atlas(project_root, atlas_root):
    """get images in an atlas that does not exist on disk"""
    image_list = []
    for image in atlas_root.iter_attributes("image"):
        image_path = project_root / image.value[1:]
        if not image_path.exists():
            image_list.append(image)
    return image_list


def get_empty_animations(atlas_root):
    animation_list = []
    for animation in atlas_root.elements("animations"):
        if not animation.get_element("images"):
            animation_list.append(animation)
    return animation_list


def clean_up_atlas(project_root, atlas):
    """Remove all missing image in entries in the atlas"""
    tree = deftree.parse(atlas)
    root = tree.get_root()
    print("  Cleaning", atlas.relative_to(project_root))
    for missing in missing_images_in_atlas(project_root, root):
        image_element = missing.get_parent()
        image_element.get_parent().remove(image_element)
        print("    Removing", image_element.value)
    for animation in get_empty_animations(root):
        root.remove(animation)
    tree.write()


def verify(project_folder):
    """Print images that are missing on disk"""
    for atlas in get_files(project_folder, "atlas"):
        for missing in missing_images_in_atlas(project_folder, atlas):
            print("{}{}{}".format(atlas.replace(project_folder, ""),
                                  (50 - len(atlas.replace(project_folder, ""))) * " ",
                                  missing))


def clean_up_all_atlases(project_folder):
    """Remove all missing image in entries in the project"""
    for atlas in get_files(project_folder, "atlas"):
        clean_up_atlas(project_folder, atlas)


def main():
    path = Path().cwd()
    clean_up_all_atlases(path)


if __name__ == '__main__':
    print("Running Clean Atlas")
    main()

