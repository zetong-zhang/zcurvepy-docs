# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ZCurvePy'
copyright = '2025, TUBIC'
author = 'TUBIC'

release = '1.5'
version = '1.5.9'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "html_image",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst',
}

master_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
