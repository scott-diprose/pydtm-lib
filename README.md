# pydtm-lib

Object model for standardising the structure of metadata applicable for mapping from one source data set to a target. Potentially being reshaped during the transfer.

This is a development release which does not enforce any structure on the metadata file.
Simply providing dot notation access to the loaded metadata fields. This is to provide
for rapid prototyping for https://github.com/scott-diprose/dtm-schema.

## User Guide

```shell
pip install pydtm-lib
```

```python
from pydtm import mapping

metadata = mapping.load_from_file('path_to_file')
print(metadata.name)
```

## Library Development

Current release requires Python 3.8 and pipenv installed.

```shell
pipenv sync --dev
```

Tasks are configured for the Visual Studio Code editor.
TODO: Look into moving to pyproject.toml

Ideas and constructive criticism welcome: https://github.com/scott-diprose/pydtm-lib/discussions
