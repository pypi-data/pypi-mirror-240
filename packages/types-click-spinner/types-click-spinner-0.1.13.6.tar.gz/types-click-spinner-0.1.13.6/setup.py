from setuptools import setup

name = "types-click-spinner"
description = "Typing stubs for click-spinner"
long_description = '''
## Typing stubs for click-spinner

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`click-spinner`](https://github.com/click-contrib/click-spinner) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`click-spinner`.

This version of `types-click-spinner` aims to provide accurate annotations
for `click-spinner==0.1.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/click-spinner. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `571cc6d77ad85c6b3c12f546f8b62c69f37da402` and was tested
with mypy 1.7.0, pyright 1.1.334, and
pytype 2023.10.17.
'''.lstrip()

setup(name=name,
      version="0.1.13.6",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/click-spinner.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['click_spinner-stubs'],
      package_data={'click_spinner-stubs': ['__init__.pyi', '_version.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.7",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
