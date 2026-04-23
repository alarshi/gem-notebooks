import os
import sys

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'CIG Education GEM Notebooks'
author = 'CIG Education Team'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    "nbsphinx",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_title = 'CIG Education GEM Notebooks'
html_logo  = './assets/education-gem-notebooks_icon.png'
html_static_path = ['_static']

# -- Read the Docs specific configuration ------------------------------------
sys.path.insert(0, os.path.abspath('elasticity-flexture-L0/'))