# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

import os

import click

from nodule import nod


@click.command("nodule")
@click.argument("format")
@click.argument("path")
def nodule(format, path):
    """
    Convert file at PATH to FORMAT. Supported formats are: JSON, TOML, YAML.
    MERMAID is also supported as an output format.

    `import nodule.nod` to iterate over these data structures.
    """

    # Basic input validation

    _format = format.lower()
    if _format not in ["json", "mermaid", "toml", "yaml"]:
        exit(f"Target format {_format} not recognised.")

    if not os.path.isfile(path):
        exit(f"Path {path} is invalid.")

    valid_source = (
        path.endswith(".json") or path.endswith(".toml") or path.endswith(".yaml")
    )
    if not valid_source:
        exit("Source type not recognised.")

    target_path = path[:-4] + _format

    # Attempt translation

    try:
        subtree = nod.load(path)
        nod.write(subtree, target_path)
    except Exception as e:
        exit(f"An error occurred: {e}")
