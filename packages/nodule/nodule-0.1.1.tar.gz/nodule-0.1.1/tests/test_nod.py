# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

from nodule import nod


def test_style_from_path():
    style = nod._get_style_from_path("example.json")
    assert "json" == style
