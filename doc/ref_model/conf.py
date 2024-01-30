project = 'Anuket Reference Model (RM)'
copyright = '2022, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex'
]
html_theme = "piccolo_theme"
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

html_static_path = ['_static']
templates_path = ['_templates']

html_css_files = [
    'custom.css',
]

html_show_sourcelink = False
html_theme_options = {
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Inverse png
html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
