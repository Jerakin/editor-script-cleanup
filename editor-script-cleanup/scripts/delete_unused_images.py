#!/usr/bin/env python3
from pathlib import Path
import configparser

import deftree


def all_files(project_root, ending):
    # Generator to get files
    g = '**/*.{}'.format(ending)
    for f in project_root.glob(g):
        yield f


def image_in_file(atlas):
    # Returns all images in an atlas
    tree = deftree.parse(atlas)
    root = tree.get_root()
    images = []
    for x in root.iter_attributes("image"):
        images.append(x)
    return images


def image_in_cubemap(cubemap):
    # Returns all images in a cubemap
    tree = deftree.parse(cubemap)
    root = tree.get_root()
    images = []
    for child in root.attributes():
        if child.value.endswith(".png"):
            images.append(child)
    return images


def unused_png_remover(project_root, project_file):
    files_with_images = {}

    config = configparser.ConfigParser()
    config.read(project_file)
    config_images = []
    for key in config:
        for value in config[key]:
            if config[key][value].endswith(".png"):
                config_images.append(config[key][value])
    files_with_images["game.project"] = config_images

    for x in all_files(project_root, "tilesource"):
        files_with_images[x.name] = image_in_file(x)

    for x in all_files(project_root, "atlas"):
        files_with_images[x.name] = image_in_file(x)

    for x in all_files(project_root, "cubemap"):
        files_with_images[x.name] = image_in_cubemap(x)

    for x in all_files(project_root, "png"):
        count = 0
        relative_image = "/{}".format(x.relative_to(project_root).as_posix())
        for file in files_with_images:
            if relative_image in files_with_images[file]:
                count += 1
        if count == 0:
            path = project_root / relative_image[1:]
            print("  Removed", path)
            path.remove()


def main():
    project_root = Path().cwd()
    project_file = project_root / "game.project"
    if project_file.exists():
        unused_png_remover(project_root, project_file)


if __name__ == '__main__':
    print("Running Delete Unused Images")
    main()

