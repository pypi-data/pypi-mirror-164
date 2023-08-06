# python-packaging
Sample Integrations for PyPI and GitHub Actions

## Pre-requisites

- [Python](https://www.python.org/downloads/) >= 3.9 for application development

## Quickstart CLI

### OS X / Linux
```shell
# clone the repo
git clone https://github.com/LinuxForHealth/python-packaging.git
cd python-packaging

# create virtual environment and create an "editable" install
python3 -m venv venv --clear && \
        source venv/bin/activate && \
        python3 -m pip install --upgrade pip setuptools wheel build

python3 -m pip install -e .[dev]

# run tests
python3 -m pytest        
```


