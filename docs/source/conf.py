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
# sys.path.insert(0, os.path.abspath('.'))
import itertools
import os
import sys
import time
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'LogicLab编程工具用户指南'
author = '上海翌控科技有限公司'
copyright = '{}, {}'.format(time.strftime('%Y'), author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# Disable the Copyright footer for Read the docs at the bottom of the page
# by setting property html_show_copyright = False
html_show_copyright = True

# Disable showing Sphinx footer message:
# "Built with Sphinx using a theme provided by Read the Docs. "
html_show_sphinx = False

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'prev_next_buttons_location': None,
    #      'canonical_url': '',
    #      'analytics_id': 'UA-XXXXXXX-1',
    #      'logo_only': False,
    #      'display_version': True,
    #      'prev_next_buttons_location': 'bottom',
    #      'style_external_links': False,
    #      'vcs_pageview_mode': '',
    #      'style_nav_header_background': 'white',
    #      # Toc options
          'collapse_navigation': True,
          'sticky_navigation': True,
          'navigation_depth': -1,
    #      'includehidden': True,
    #      'titles_only': False
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the built-in "default.css".
# html_static_path = ['_static']

# Github options used with Sphinx
html_context = {
    "display_github": "True",
    "github_user": "nxtrol",
    "github_repo": "logiclab_userguide",
    "github_version": "master",
    "conf_py_path": "/docs/source/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']