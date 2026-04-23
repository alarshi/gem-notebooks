# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'GEM Notebooks'
author = 'CIG Education Team'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_nb',
]

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst',
    '.ipynb': 'myst-nb',
}

exclude_patterns = ['_build', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_title = 'CIG Education GEM Notebooks'
html_logo  = './assets/education-gem-notebooks_icon.png'
html_static_path = ['_static']
