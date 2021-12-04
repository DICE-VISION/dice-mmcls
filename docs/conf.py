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
import os
import subprocess
import sys

import pytorch_sphinx_theme
from m2r import MdInclude
from recommonmark.transform import AutoStructify
from sphinx.builders.html import StandaloneHTMLBuilder

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'MMClassification'
copyright = '2020, OpenMMLab'
author = 'MMClassification Authors'
version_file = '../mmcls/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


# The full version, including alpha/beta/rc tags
release = get_version()

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'myst_parser',
    'sphinx_copybutton',
]

autodoc_mock_imports = ['matplotlib', 'mmcls.version', 'mmcv.ops']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # 'logo_url': 'https://mmocr.readthedocs.io/en/latest/',
    'menu': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/open-mmlab/mmclassification'
        },
        {
            'name':
            'Colab Tutorials',
            'children': [
                {
                    'name':
                    'Train and inference with shell commands',
                    'url':
                    'https://colab.research.google.com/github/'
                    'open-mmlab/mmclassification/blob/master/docs/tutorials/'
                    'MMClassification_tools.ipynb',
                },
                {
                    'name':
                    'Train and inference with Python APIs',
                    'url':
                    'https://colab.research.google.com/github/'
                    'open-mmlab/mmclassification/blob/master/docs/tutorials/'
                    'MMClassification_python.ipynb',
                },
            ]
        },
        {
            'name':
            'Docs',
            'children': [
                {
                    'name': 'MMCV',
                    'url': 'https://mmcv.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MIM',
                    'url': 'https://openmim.readthedocs.io/en/latest/'
                },
                {
                    'name': 'MMAction2',
                    'url': 'https://mmaction2.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMClassification',
                    'url':
                    'https://mmclassification.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMDetection',
                    'url': 'https://mmdetection.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMDetection3D',
                    'url': 'https://mmdetection3d.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMEditing',
                    'url': 'https://mmediting.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMGeneration',
                    'url': 'https://mmgeneration.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMOCR',
                    'url': 'https://mmocr.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMPose',
                    'url': 'https://mmpose.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMSegmentation',
                    'url': 'https://mmsegmentation.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMTracking',
                    'url': 'https://mmtracking.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMFlow',
                    'url': 'https://mmflow.readthedocs.io/en/latest/',
                },
                {
                    'name': 'MMFewShot',
                    'url': 'https://github.com/open-mmlab/mmfewshot',
                },
            ]
        },
        {
            'name':
            'OpenMMLab',
            'children': [
                {
                    'name': 'Homepage',
                    'url': 'https://openmmlab.com/'
                },
                {
                    'name': 'GitHub',
                    'url': 'https://github.com/open-mmlab/'
                },
                {
                    'name': 'Twitter',
                    'url': 'https://twitter.com/OpenMMLab'
                },
                {
                    'name': 'Zhihu',
                    'url': 'https://zhihu.com/people/openmmlab'
                },
            ]
        },
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/readthedocs.css']
html_js_files = ['js/custom.js']

master_doc = 'index'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'mmclsdoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    'preamble':
    r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'mmcls.tex', 'MMClassification Documentation',
     'MMClassification Contributors', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'mmcls', 'MMClassification Documentation', [author],
              1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'mmcls', 'MMClassification Documentation', author, 'mmcls',
     'One line description of project.', 'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# set priority when building html
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml', 'image/gif', 'image/png', 'image/jpeg'
]

# -- Extension configuration -------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True


def builder_inited_handler(app):
    subprocess.run(['./stat.py'])


def setup(app):
    app.add_config_value('no_underscore_emphasis', False, 'env')
    app.add_config_value('m2r_parse_relative_links', False, 'env')
    app.add_config_value('m2r_anonymous_references', False, 'env')
    app.add_config_value('m2r_disable_inline_math', False, 'env')
    app.add_directive('mdinclude', MdInclude)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
    app.add_js_file('./_static/js/custom.js')
    app.connect('builder-inited', builder_inited_handler)
