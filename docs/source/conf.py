import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'sphinx'
copyright = '2026, cogiverse'
author = 'cogiverse'

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc', # Pour extraire la doc du code
    'sphinx.ext.napoleon', # Pour supporter les docstrings style
    'sphinx.ext.mathjax', # Pour latex
    'sphinx.ext.viewcode', # Pour afficher code source
    'myst_parser', # Pour le markdown
    'sphinx_copybutton', # Pour ajouter un bouton de copie
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

html_theme = "sphinx_rtd_theme"
html_logo = "_static/img/logo.png"
html_title = "Documentation - Sphinx - UV"
html_static_path = ['_static']

# Empêche MyST de valider les liens vers des fichiers externes/générés
myst_all_links_external = False

# Supprimer l'avertissement spécifique pour le dossier coverage
suppress_warnings = ["myst.xref_missing"]