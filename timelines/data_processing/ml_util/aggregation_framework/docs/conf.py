# -*- coding: utf-8 -*-
#
# docbird documentation build configuration file
# Note that not all possible configuration values are present in this
# autogenerated file.
#

from os.path import abspath, dirname, isfile, join


extensions = [
  "sphinx.ext.autodoc",
  "sphinx.ext.intersphinx",
  "sphinx.ext.ifconfig",
  "sphinx.ext.graphviz",
  "twitter.docbird.ext.thriftlexer",
  "twitter.docbird.ext.toctree_default_caption",
  "sphinxcontrib.httpdomain",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"""Aggregation Framework"""
description = u""""""

# The short X.Y version.
version = u"""1.0"""
# The full version, including alpha/beta/rc tags.
release = u"""1.0"""

exclude_patterns = ["_build"]

pygments_style = "sphinx"

html_theme = "default"

html_static_path = ["_static"]

html_logo = u""""""

# Automagically add project logo, if it exists
# (checks on any build, not just init)
# Scan for some common defaults (png or svg format,
# called "logo" or project name, in docs folder)
if not html_logo:
  location = dirname(abspath(__file__))
  for logo_file in ["logo.png", "logo.svg", ("%s.png" % project), ("%s.svg" % project)]:
    html_logo = logo_file if isfile(join(location, logo_file)) else html_logo

graphviz_output_format = "svg"
