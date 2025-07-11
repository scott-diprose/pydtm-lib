# M4DM (Metadata for Data Meaning)

> pym4dm-lib

A metadata library which captures the meaning of individual data elements. Where an
element originated from or how it was transformed/derived from originating data.
Maintaing data linage accross all maintained data stores delivers the most potential
to provide understanding and meaning to data.

If data linage is also maintained in a computer readable format. This then provides
the potential for code generation.

WASM & PyPI pkg

1. schemas and validation
2. protocol matching - identify the intended schema of a loaded json document
3. object serialisation - load/unload specific schema instances

Also provide through plugins (e.g. implemention of templating for code generation):

- web components for viewing and editing (served from a HTTP service, or obtained locally from WASM)
- metadata generation
- data extract and load
- data transform
- data profiling
- data testing

---

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
