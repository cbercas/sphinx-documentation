# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import sphinx_rtd_theme

# Configurar la ruta al directorio raíz del proyecto
sys.path.insert(0, os.path.abspath('../../source'))
print("sys.path:", sys.path)
sys.path.insert(0, os.path.abspath('../src'))
print("sys.path:", sys.path)

project = 'Proyecto Equipo 05 | Tema 05 '
copyright = '2024, Equipo 05'
author = 'Cristina Bermúdez Castro, Pedro Blanco Vargas, Noah Montaño Muñoz'
release = '1'
language = 'es'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Genera documentacion automaticamente desde docstrings
    'sphinx.ext.napoleon', # Interpreta docstring en formatos google y nunpy
    'sphinx.ext.viewcode', # Agrega enlaces al código fuente desde la documentación
    'sphinx_rtd_theme', # Tema visual basado en read the docs
    'sphinx.ext.doctest',
    'myst_parser', # Habilita soporte para archivos Markdown
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []
html_css_files = [
    'custom.css',  # Nombre del archivo CSS
]

# Tema de resaltado de Pygments
pygments_style = 'sphinx' 

html_theme = 'sphinx_rtd_theme'

# Configuración para soportar múltiples tipos de archivos fuente
source_suffix = {
    '.rst': 'restructuredtext',  # Archivos en formato reStructuredText
    '.md': 'markdown',  # Archivos en formato Markdown
}

latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

latex_documents = [
    ('index', 'documento.tex', 'Título del Documento',
     'Autor del Documento', 'manual'),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output