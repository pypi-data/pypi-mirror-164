from setuptools import setup

name = "types-Flask-SQLAlchemy"
description = "Typing stubs for Flask-SQLAlchemy"
long_description = '''
## Typing stubs for Flask-SQLAlchemy

This is a PEP 561 type stub package for the `Flask-SQLAlchemy` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Flask-SQLAlchemy`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/Flask-SQLAlchemy. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `cb154816333671ae0b438001b04d298ff3d4559d`.
'''.lstrip()

setup(name=name,
      version="2.5.9",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/Flask-SQLAlchemy.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-SQLAlchemy'],
      packages=['flask_sqlalchemy-stubs'],
      package_data={'flask_sqlalchemy-stubs': ['__init__.pyi', 'model.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
