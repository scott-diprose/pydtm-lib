py -3.12 -m venv --clear --upgrade-deps .venv
if ($? -ne $true) {
    Exit $LastExitCode
}

& $PSScriptRoot\.venv\Scripts\Activate.ps1
if ($? -ne $true) {
    Exit $LastExitCode
}

# pip list --outdated

# python -m pip install --upgrade --require-virtualenv --editable .[dev]
# python -m pip freeze --exclude-editable > requirements.lock.txt && echo "-e ." >> requirements.lock.txt
# python -m pip install -r requirements.lock.txt --require-virtualenv

python -m pip install -r requirements.dev.txt --require-virtualenv
Exit $LastExitCode
