# nodule

Convert, visualize and iterate over heterogeneous trees.

## Usage

```
Usage: nodule [OPTIONS] FORMAT PATH

  Convert file at PATH to FORMAT. Supported formats are: JSON, TOML, YAML.
  MERMAID is also supported as an output format.

  `import nodule.nod` to iterate over these data structures.

Options:
  --help  Show this message and exit.
```

<!-- start @generated footer -->

# Development environment

## Install prerequisites

- Python 3.10
- pdm
- make
- pipx (optional, required for `make install-source`)

## Instructions

- Fork the upstream repository.
- `git clone [fork-url]`
- `cd [project-folder]`
- Run `make develop` to initialise your development environment.

You can use any text editor or IDE that supports virtualenv / pdm. See the
Makefile for toolchain details.

Please `make test` and `make lint` before submitting changes.

## Make targets

```
USAGE: make [target]

help    : Show this message.
develop : Set up Python development environment.
run     : Run from source.
clean   : Remove all build artefacts.
test    : Run tests and generate coverage report.
lint    : Fix or warn about linting errors.
build   : Clean, test, lint, then generate new build artefacts.
publish : Upload build artefacts to PyPI.
install-source : Install source as a local Python application.
```

# Sharing and contributions

```
nodule
https://lofidevops.neocities.org
Copyright 2023 David Seaward and contributors
SPDX-License-Identifier: Apache-2.0
```

Shared under Apache-2.0. We adhere to the Contributor Covenant 2.1, and certify
origin per DCO 1.1 with a signed-off-by line. Contributions under the same
terms are welcome.

Submit security and conduct issues as private tickets. Sign commits with
`git commit --signoff`. For a software bill of materials run `reuse spdx`. For
more details see CONDUCT, COPYING and CONTRIBUTING.
