# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath('..'))  # Autodoc

# -- Project information -----------------------------------------------------

project = 'Mars Insight'
copyright = '2020, Albert Wigmore'
author = 'Albert Wigmore'
release = '0.0.1'

# # -- General configuration ---------------------------------------------------

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
]

templates_path = [
]

exclude_patterns = [
]


# # -- Options for HTML output -------------------------------------------------

html_theme = 'press'

# Theme options
html_theme_options = {
    "external_links": [
        ("Github", "https://github.com/albertwigmore/mars-insight"),
    ]
}
