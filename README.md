# 🚀 Sphinx Project

![CI Status](https://img.shields.io/badge/CI-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-success)
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
