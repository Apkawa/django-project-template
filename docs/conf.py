# -*- coding: utf-8 -*-
import sys, os
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.coverage']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'uslugi24'
copyright = u'2013, apkawa'
version = '0.1a1'
release = '0.1a1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'uslugi24doc'

_title = u'{} Documentation'.format(project)


latex_elements = {
    'inputenc': '',
    'utf8extra': '',
    'preamble': '''

\usepackage{fontspec}
\setsansfont{Liberation Sans}
\setromanfont{Liberation Sans}
\setmonofont{DejaVu Sans Mono}
''',
}

latex_documents = [
  ('index', 'uslugi24.tex', _title,
   u'apkawa', 'manual'),
]

man_pages = [
    ('index', project, _title,
     [u'apkawa'], 1)
]

texinfo_documents = [
  ('index', project, _title,
   u'apkawa', project, 'One line description of project.',
   'Miscellaneous'),
]
