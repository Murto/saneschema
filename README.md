[![Build Status](https://travis-ci.org/Murto/saneschema.svg?branch=master)](https://travis-ci.org/Murto/saneschema)

# saneschema

saneschema is a JSON schema package for people who want an easier-to-parse schema than that provided by `jsonschema`.
saneschema checks that a JSON file conforms to a given structure, or schema, which can be a very useful tool for data validation.

## Installation

The following sections assume that python 3 is your default version of python.

### PyPi & Pip

Installation with PyPi and Pip is the easier option and will ensure you have the most up to date, stable version

```bash
pip install saneschema
```

### Git & Pip

Installation with Git and Pip is a bit more work but will ensure you have the most up to date version.

```bash
git clone https://github.com/Murto/saneschema.git
cd saneschema
python setup.py
pip dist/*.whl
```
