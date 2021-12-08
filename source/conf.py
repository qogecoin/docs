"""Sphinx config file."""

# -- Project information -----------------------------------------------------

project = 'docs'
copyright = '2021, The Qogecoin Authors'
author = 'The Qogecoin Authors'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'

# The githubpages extension will autogenerate CNAME file when base_url is set.
html_baseurl = 'https://www.qogecoin.org'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'Qogecoin Docs'

html_theme_options = {
    'extra_navbar': '',
    'use_download_button': False,
    'use_fullscreen_button': False,

    'repository_url': 'https://github.com/qogecoin/qogecoin',
    'use_repository_button': True,
}
