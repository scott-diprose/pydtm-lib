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

Current release has been tested on Python 3.10.4

```powershell
./setup.dev.ps1
```

Tasks are configured for the Visual Studio Code editor.

Ideas and constructive criticism welcome: https://github.com/scott-diprose/pydtm-lib/discussions

---

Get Data. Process driven by metadata:

- SQL column defs
- API & JSON Path

>> extract data lineage & document downstream datasets
>> surface as web app, and integrate with subject area documentation
>> integrate with reporting tooltips, etc

---

DLM (Data Linage Metadata)
A standard metadata library.

WASM & PYPi pkg

1. generation and extract utils
2. object serialisation (load/unload)
3. schemas and validation
4. protocol matching (identify the intended schema of a loaded json document)
