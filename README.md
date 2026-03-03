# 🚀 Sphinx Project

[![CI Status](https://github.com/ElvexDom/sphinx-init/actions/workflows/ci.yml/badge.svg)](https://github.com/ElvexDom/sphinx-init/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ElvexDom/sphinx-init/python-coverage-comment-action-data/endpoint.json)](https://github.com/ElvexDom/sphinx-init/tree/python-coverage-comment-action-data)
![License](https://img.shields.io/badge/license-MIT-blue)

Bienvenue dans le projet. Cette boîte à outils Python est conçue avec une exigence d'excellence technique.

## 🛠 Installation

Le projet utilise `uv` pour une gestion rapide et robuste des dépendances.

# Installation automatique (recommandée)
```bash
# Cloner le dépôt
git clone <url-du-repo>
cd sphinx-init
```

```bash
# Installer l'environnement
uv sync
```

# Installation manuelle
```bash
# Installation de la dépendance principale
uv add pandas
# Installation des outils de test, linting et documentation
uv add --dev pytest pytest-cov ruff sphinx sphinx-rtd-theme myst-parser sphinx-copybutton
```

[!TIP]
L'utilisation de --dev place ces bibliothèques dans le groupe de dépendances de développement, les séparant ainsi des dépendances logicielles de base.

# Créer le répertoire de documentation et lancer l'assistant
```bash
mkdir docs
uv run sphinx-quickstart docs
```

#  Qualité & Maintenance
Linting :
```bash
uv run ruff check .
```

Tests :
```bash
uv run pytest --cov=app --cov-report=html:docs/source/_static/coverage tests/
```

Génération Doc :
```bash
uv run sphinx-build -b html docs/source docs/build
```
