# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'delegated-qc'
copyright = '2025, Matthew Prest'
author = 'Matthew Prest'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_autodoc_typehints',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# sphinx.ext.intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'qiskit': ('https://qiskit.org/documentation/', None),
}

# sphinx.ext.autodoc
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# sphinx.ext.autosummary
autosummary_generate = True

# sphinx.ext.todo
todo_include_todos = True

# myst_parser
myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'deflist',
    'html_admonition',
    'html_image',
    'colon_fence',
    'smartquotes',
    'replacements',
    'linkify',
    'substitution',
]