# defe

> A Tech feed Aggregator for Developers


![PyPI](https://img.shields.io/pypi/v/defe)
![GitHubLicense](https://img.shields.io/github/license/bhupesh-v/defe)
![PyPI - Status](https://img.shields.io/pypi/status/defe)


## 🔮 Installation

Install **defe** using `pip` from PyPI

```bash
pip install defe
```

## Usage

- As CLI
Just run the `defe` command

- As a Package

```python

from defe import defe
import pprint

f = defe.feed()

pprint.pprint(f.news(3))
pprint.pprint(f.feeders("newsletters"))

```

## Documentation

> [defe Documentation](https://defe.readthedocs.io/en/latest/)


## Development

1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git https://github.com/codeclassroom/CodeRunner.git
```
3. Install Dependencies.
```bash
pip install -r requirements.txt
```
4. Run tests.
```bash
python tests.py
```
5. Lint the project with
```bash
black --check --diff .
```

## 📝 Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for details.
