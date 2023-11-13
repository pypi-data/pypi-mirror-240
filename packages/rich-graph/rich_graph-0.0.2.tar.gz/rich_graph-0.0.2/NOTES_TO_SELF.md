To build:
in parent directory ("/rich_graph"), run:

```bash
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```

Old contents of pyproject.toml:
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "rich_graph"
version = "0.0.1"
authors = [
{ name = "Anthony Sifontes", email = "anthony.sifontes@gmail.com" },
]
maintainers = [
{ name = "Anthony Sifontes", email = "anthony.sifontes@gmail.com" },
]
description = "Utility structures and functions for working with graphs while maintaining your sanity."
readme = "README.md"
requires-python = ">=3.6"
classifiers = [
"Development Status :: 3 - Alpha",
"Intended Audience :: Developers",
"License :: OSI Approved :: MIT License",
"Programming Language :: Python :: 3",
]

[project.urls]
"Homepage" = "https://github.com/amsifontes/rich_graph"
"Bug Tracker" = "https://github.com/amsifontes/rich_graph/issues"

to build:
python3 setup.py bdist_wheel

to install locally (for rapid testing):

```bash
$> pip3 install -e .
$> python3
$> >>> import rich_graph
```

to package source:

```bash
$> python setup.py sdist
```

build both wheel and source dist: `python3 setup.py bdist_wheel sdist`
