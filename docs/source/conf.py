# -*- coding: utf-8 -*-
import sys
import os

# Adding directory with BookingCore package to the sys path.
sys.path.insert(0, os.path.abspath('../..'))
import easyemail


# -- General configuration ----------------------------------------------------

# Defining Sphinx extension modules.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx']

autodoc_default_flags = ['members', 'undoc-members', 'private-members',
                         'show-inheritance']
autodoc_member_order = 'bysource'
intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
}

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'EasyEmail'
copyright = u'2013, Marek Szwalkiewicz'

# The version info for the project, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
#
# The short X.Y version.
version = easyemail.__version__
# The full version, including alpha/beta/rc tags.
release = easyemail.__version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Don't display module names before objects titles, it's more readable.
add_module_names = False


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.
try:
    import sphinx_readable_theme
except:
    html_theme = "default"
else:
    html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
    html_theme = 'readable'

# Output file base name for HTML help builder.
htmlhelp_basename = 'easyemaildoc'


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'EasyEmail', u'EasyEmail Documentation', [u'Marek Szwalkiewicz'], 1)
]
