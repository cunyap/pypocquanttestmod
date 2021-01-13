import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from pathlib import Path
# sys.path.insert(0, os.path.abspath('..\src\main\python\pyPOCQuantUI\pypocquant'))
# sys.path.insert(0, os.path.abspath('../src/main/python/pyPOCQuantUI'))
# sys.path.append('..\..\pypocquantui\src\main\python\pyPOCQuantUI')
# print(os.path.abspath('../src/main/python/pyPOCQuantUI/pypocquant'))

pypocquant_path = Path(__file__).resolve().parent.parent / 'src' / 'main' / 'python' / 'pyPOCQuantUI' 
print('Adding pypocquant on path', pypocquant_path)
sys.path.insert(0, str(pypocquant_path))


# -- Project information -----------------------------------------------------

project = 'pyPOCQuantsamplemod'
copyright = '2020, Andreas P. Cuny and Aaron Ponti'
author = 'Andreas P. Cuny and Aaron Ponti'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx_rtd_theme",
    'm2r2',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'autoapi.extension',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx_markdown_tables',
    'nbsphinx_link',
]

autosummary_generate = False
m2r_parse_relative_links = True
m2r_anonymous_references = True

autoapi_type = 'python'
print('autoapi path:', str(Path(pypocquant_path / 'pypocquant')))
autoapi_dirs = [str(Path(pypocquant_path))] # ['../src/main/python/pyPOCQuantUI/pypocquant']
autoapi_ignore = ['index.rst', 'ui', 'main.py', 'example_nb']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '_templates', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# source_suffix = '.rst'
source_suffix = ['.rst', '.md']
