# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

import json
from typing import Any

import tomlkit
from ruamel.yaml import YAML


def nodify(subtree: Any, parent=None):
    """
    Recursively unpack a subtree as a sequence of node-parent pairs.
    """

    if type(subtree) is list:
        for node in subtree:
            for n, p in nodify(node, parent):
                yield n, p

    elif type(subtree) is dict:
        for key, value in subtree.items():
            for n1, p1 in nodify(key, parent):
                yield n1, p1
            for n2, p2 in nodify(value, key):
                yield n2, p2

    elif parent is not None:
        # if parent is None, we yield nothing
        yield subtree, parent


def merminate(subtree, with_heading=True):
    """
    Convert a subtree to a simple Mermaid flowchart.
    Includes document heading by default, disable to get links only.
    """

    if with_heading:
        yield "flowchart TD"

    for node, parent in nodify(subtree):
        yield f"  {parent} --> {node}"


def stringify(subtree, style: str):
    """
    Transform a subtree into a multiline string.
    Available styles are JSON, Mermaid flowchart, TOML and YAML.
    """

    if style == "json":
        return json.dumps(subtree, indent=2)
    elif style == "toml":
        return tomlkit.dumps(subtree)
    elif style == "yaml":
        yaml = YAML(typ=["safe", "string"], pure=True)
        return yaml.dump_to_string(subtree)  # noqa
        # typ="string" adds a `dump_to_string` method to the YAML object
        # see https://pypi.org/project/ruamel.yaml.string/
    elif style == "mermaid":
        return "\n".join(merminate(subtree)) + "\n"
    else:
        raise ValueError(f"Unknown style: {style}")


def _get_style_from_path(path):
    parts = path.split(".")
    if len(parts) == 1:
        raise ValueError(f"Filetype not recognised: {path}")

    style = parts[-1].lower()
    if style not in ["json", "mermaid", "toml", "yaml"]:
        raise ValueError(f"Filetype not recognised: {path}")

    return style


def load(path):
    """
    Load a file (JSON, TOML, YAML) as an iterable subtree.
    """

    style = _get_style_from_path(path)

    with open(path, "r") as f:
        if style == "json":
            return json.load(f)
        elif style == "toml":
            return tomlkit.load(f).unwrap()
        elif style == "yaml":
            yaml = YAML(typ="safe", pure=True)
            return yaml.load(f)
        else:
            raise ValueError(f"Cannot load {path}")


def write(subtree, path):
    """
    Write a subtree to a file (JSON, Mermaid flowchart, TOML, YAML).
    """

    style = _get_style_from_path(path)
    with open(path, "w") as f:
        multiline = stringify(subtree, style)
        if not multiline.endswith("\n"):
            multiline += "\n"
        f.write(multiline)
