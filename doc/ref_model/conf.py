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

linkcheck_ignore = [
    "https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md",
    "https://github.com/opencontainers/runtime-spec/blob/master/config.md",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en",
    "https://ntia.gov/page/software-bill-materials",
    "https://www.cisecurity.org/controls/cis-controls-list",
    'https://github.com/cnti-testcatalog/testsuite/blob/main/RATIONALE.md#',
    "https://infocentre2.gsma.com/",
    "https://www.gsma.com/membership/member-gateway/",
    "https://www.gsma.com/",
    "https://www.gsma.com/security/resources/fs-31-gsma-baseline-security-controls/",
    "https://us.aicpa.org/content/aicpa/interestareas/frc/assuranceadvisoryservices/sorhome.html",
    "https://www.rfc-editor.org/info/rfc5907 ",
    "https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf",
    "https://ntia.gov/SBOM",
    "https://ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf", 
    "https://www.fcc.gov/", 
    "https://gdpr-info.eu/", 
    "https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism", 
    "https://sourceforge.net/p/linux-ima/wiki/Home", 
    "https://sourceforge.net/projects/tboot/"
]

linkcheck_timeout = 10
linkcheck_retries = 2

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
