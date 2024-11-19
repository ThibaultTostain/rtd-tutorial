# conf.py

# -- Project information -----------------------------------------------------

project = 'Nom de votre projet'
author = 'Votre nom ou organisation'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Extension pour générer la documentation à partir des docstrings
    'sphinx.ext.viewcode', # Ajoute des liens vers le code source
    'sphinx_copybutton',   # Ajoute les boutons "Copier" dans les blocs de code
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Vous pouvez remplacer par un autre thème comme "sphinx_rtd_theme"
html_static_path = ['_static']

# -- sphinx-copybutton configuration -----------------------------------------

# Ignorer certaines lignes spécifiques dans les blocs de code
copybutton_prompt_text = ">>> "  # Ignore les lignes commençant par ">>>"
copybutton_only_copy_prompt_lines = False  # Copie tout, pas uniquement les lignes commençant par le prompt

# Si besoin de styles CSS spécifiques pour le bouton (optionnel)
html_css_files = [
    'custom.css',  # Placez ce fichier dans le répertoire "_static" si nécessaire
]
