[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jeertmans/bibetal/main.svg)](https://results.pre-commit.ci/latest/github/jeertmans/bibetal/main)
[![Latest Release][pypi-version-badge]][pypi-version-url]
[![Python version][pypi-python-version-badge]][pypi-version-url]
![PyPI - Downloads](https://img.shields.io/pypi/dm/bibetal)
# bib et al. - The "One author et al." tool

bibetal is a pure Python script that rewrites bib files to only contain one author / editor per entry. Other authors / editors are automatically replaced by *and others*, which in turn is parsed as *et al.* in most bibliographies.

### Installation
bibetal can be installed using `pip`:
```
pip install bibetal
```

### Usage

Currently, bibetal only processes one file at a time and edits it in-place:

```
bibetal <FILE>
```

### Contributing

Feel free to contribute or propose ideas using the [Issues](https://github.com/jeertmans/bibetal/issues) and [Pull requests](https://github.com/jeertmans/bibetal/pulls) tabs.


[pypi-version-badge]: https://img.shields.io/pypi/v/bibetal?label=SelSearch
[pypi-version-url]: https://pypi.org/project/bibetal/
[pypi-python-version-badge]: https://img.shields.io/pypi/pyversions/bibetal
