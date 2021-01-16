#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#
# PlasmaPy documentation build configuration file, created by
# sphinx-quickstart on Wed May 31 18:16:46 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys

from datetime import datetime
from pkg_resources import parse_version
from sphinx.application import Sphinx

sys.path.insert(0, os.path.abspath(".."))

from plasmapy import __version__ as release

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx_gallery.load_style",
    "IPython.sphinxext.ipython_console_highlighting",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "astropy": ("http://docs.astropy.org/en/stable/", None),
}

autoclass_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "PlasmaPy"
author = "PlasmaPy Community"
copyright = f"2015-{datetime.utcnow().year}, {author}"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
#  Note: If plasmapy.__version__ can not be defined then it is set to 'unknown'.
#        However, release needs to be a semantic style version number, so set
#        the 'unknown' case to ''.
release = "" if release == "unknown" else release
if release == "unknown":
    release = version = revision = ""
else:
    pv = parse_version(release)
    release = pv.public
    version = ".".join(release.split(".")[:2])  # short X.Y version
    if pv.local is not None:
        revision = pv.local[1:]  # revision number w/o the leading g
    else:
        revision = ""


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "notebooks/langmuir_samples",
    "**.ipynb_checkpoints",
]


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

default_role = "obj"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'traditional'
# html_theme = 'agogo'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_logo = "./_static/with-text-light-190px.png"
html_theme_options = {
    "logo_only": True,
    #
    # TOC options
    #   https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options
    "includehidden": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# A list of prefixes that are ignored for sorting the Python module
# index (e.g., if this is set to ['foo.'], then foo.bar is shown under
# B, not F).
modindex_common_prefix = ["plasmapy."]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "PlasmaPydoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    #
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    #
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    #
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "PlasmaPy.tex",
        "PlasmaPy Documentation",
        "PlasmaPy Community",
        "manual",
    )
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "plasmapy", "PlasmaPy Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "PlasmaPy",
        "PlasmaPy Documentation",
        author,
        "PlasmaPy",
        "Python package for plasma physics",
        "Miscellaneous",
    )
]

html_favicon = "./_static/icon.ico"


# -- NBSphinx options

nbsphinx_thumbnails = {
    "notebooks/*": "_images/graphic-circular.png",
    "notebooks/langmuir_analysis": "_static/notebook_images/langmuir_analysis.png",
    "notebooks/plasma/grids_cartesian": "_static/notebook_images/uniform_grid_thumbnail.png",
    "notebooks/plasma/grids_nonuniform": "_static/notebook_images/nonuniform_grid_thumbnail.png",
}

# adapted from https://github.com/spatialaudio/nbsphinx/blob/58b8034dd9d7349c1b4ac3e7a7d6baa87ab2a6a9/doc/conf.py

# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = 'docs/' + env.doc2path(env.docname, base=None) %}
{% set nb_base = 'tree' if env.config.revision else 'blob' %}
{% set nb_where = env.config.revision if env.config.revision else 'master' %}

.. raw:: html

    <div class="admonition note">
      <p style="margin-bottom:0px">
        This page was generated by
        <a href="https://nbsphinx.readthedocs.io/">nbsphinx</a> from
        <a class="reference external" href="https://github.com/PlasmaPy/PlasmaPy/{{ nb_base|e }}/{{ nb_where|e }}/{{ docname|e }}">{{ docname|e }}</a>.
        <br>
        Interactive online version:
        <a href="https://mybinder.org/v2/gh/PlasmaPy/PlasmaPy/{{ nb_where|e }}/?filepath={{ docname|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>.
      </p>
    </div>

.. raw:: latex

    \nbsphinxstartnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{The following section was generated from
    \sphinxcode{\sphinxupquote{\strut {{ docname | escape_latex }}}} \dotfill}}
"""


def setup(app: Sphinx) -> None:
    app.add_config_value("revision", "", True)
    app.add_stylesheet("rtd_theme_overrides.css")
