# 🤝 Guide de contribution

Merci de vouloir aider à améliorer **Sphinx Markdown Project** ! 

## 🛠️ Configuration du poste de travail
Le projet utilise `uv`.
1. `git clone <url>`
2. `uv sync`

## 🧪 Cycle de validation
Avant de soumettre une Pull Request :
- **Linting :** `uv run ruff check .`
- **Tests & Couverture :** `uv run pytest --cov=app "--cov-report=html:docs/source/_static/coverage" tests/`
- **Documentation :** `uv run sphinx-build -b html docs/source docs/build/html`

## 🚀 Soumission
Créez une branche `feature/nom` et ouvrez une Pull Request vers `main`.