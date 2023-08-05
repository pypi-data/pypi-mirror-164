# -*- coding: utf-8 -*-
#
# Problem Solving with Algorithms and Data Structures documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 27 08:17:45 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

#import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('../modules'))

from runestone import runestone_static_dirs, runestone_extensions
import petljadoc

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.mathjax'] + runestone_extensions() + petljadoc.runestone_ext.extensions()

#,'runestone.video','runestone.reveal','runestone.poll','runestone.tabbedStuff','runestone.disqus','runestone.codelens','runestone.activecode', 'runestone.assess', 'runestone.animation','runestone.meta', 'runestone.parsons', 'runestone.blockly', 'runestone.livecode','runestone.accessibility']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['{{templates_path}}']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = '{{project_title}}'
#pylint: disable=redefined-builtin
copyright = '{{now.year}} {{author}}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = '{{language}}'
locale_dirs = ['{{locale_dirs}}']
# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%%B %%d, %%Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# `keep_warnings <http://www.sphinx-doc.org/en/stable/config.html#confval-keep_warnings>`_:
# If true, keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True

# `rst_prolog <http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog>`_:
# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
rst_prolog = (
# For fill-in-the-blank questions, provide a convenient means to indicate a blank.
"""

.. |blank| replace:: :blank:`x`
"""
)

# -- Options for HTML output ---------------------------------------------------

html_context = {'course_id': '{{project_name}}',
                'login_required':'{{login_req}}',
                'appname': "{{master_app}}",
                'loglevel': int("{{log_level}}"),
                'course_url': "{{master_url}}",
                'use_services': '{{use_services}}',
                'python3': '{{python3}}',
                'dburl': os.environ['DBURL'] if 'DBURL' in os.environ else '{{dburl}}',
                'default_ac_lang': '{{default_ac_lang}}',
                'basecourse': '{{basecourse}}',
                'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                'proxy_uri_files': '/jobe/index.php/restapi/files/',
                'downloads_enabled': '{{downloads_enabled}}',
                'enable_chatcodes': '{{enable_chatcodes}}',
                'lang': '{{language_meta}}'
               }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = '{{html_theme}}'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {'nosidebar': 'true'}
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "{{project_title}}",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Chapters",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #
    # Note that this is served off CDN, so won't be available offline.
    #'bootswatch_theme': "slate",
}

#html_style = "style.css"

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["{{html_theme_path}}"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{{project_title}}'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title ='{{project_title}}'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.

# logo is included in layout file
#html_logo = "../source/_static/logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']  + runestone_static_dirs() + petljadoc.runestone_ext.static_dirs()

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%%b %%d, %%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = '{{project_name}}-doc'

# 'accessibility_style' config value is defined in the 'accessibility' extension. 
# By this config value you can select what accessibility stylesheet
# you want to add ('normal', 'light', 'darkest' or 'none')
#accessibility_style = 'normal'

# Config values for specific Runestone components
#
#activecode_div_class = 'runestone explainer ac_section alert alert-warning'
#activecode_hide_load_history = False
#mchoice_div_class = 'runestone alert alert-warning'
#clickable_div_class = 'runestone alert alert-warning'
#codelens_div_class = 'alert alert-warning cd_section'
#dragndrop_div_class = 'runestone'
#fitb_div_class = 'runestone'
#parsons_div_class = 'runestone'
#poll_div_class = 'alert alert-warning'
#shortanswer_div_class = 'journal alert alert-warning'
#shortanswer_optional_div_class = 'journal alert alert-success'
#showeval_div_class = 'runestone explainer alert alert-warning'
#tabbed_div_class = 'alert alert-warning'

petljadoc.runestone_ext.config_values_for_components(globals())
