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
# import os
# import sys
# import celery
# import sphinx_rtd_dark_mode
# sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------

project = "backpack"
copyright = "2021, 4lul"
author = "4lul"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# import docutils.core
#
# docutils.core.publish_file(
#    source_path ="intro.rst",
#    destination_path ="intro.html",
#    writer_name ="html")

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ["celery"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# extensions = ['sphinx_rtd_dark_mode']
# html_theme = 'sphinx_rtd_dark_mode'
# html_theme = 'sphinx_celery'
html_theme = "furo"
#'sphinx-rtd-theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom1.css"]

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        #    "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        #    "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

html_theme_options = {
    "light_css_variables": {
        "font-stack": "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif,'Apple Color Emoji','Segoe UI Emoji'",
        "font-stack--monospace": "ui-monospace,SFMono-Regular,SF Mono,Menlo,Consolas,Liberation Mono,monospace",
        "color-code-background": "#EEE",
        "highlight-background-color": "#EEE",
    },
    "dark_css_variables": {
        "font-stack": "Georgia, serif",
        "font-stack--monospace": "monospace,Mono",
    },
}
#
# html_sidebars = {
#        '**': ['localtoc.html',
#               'relations.html',
#               'sourcelink.html',
#               'searchbox.html'
#            ]
#
#        }
# html_style = 'css/custom.css'
