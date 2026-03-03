# 1. La version de python
FROM python:3.12-slim

# 2. On récupère uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. On crée un dossier pour l'application
WORKDIR /app

# 4. On copie uniquement les fichiers de dépendances
COPY pyproject.toml uv.lock ./

# 5. On installe les paquets via l'interface pip de uv
# Note : On utilise '.' pour dire "installe les dépendances définies dans ce projet"
# --system permet d'installer sans venv
RUN uv pip install --system .

# 6. On copie le reste du code
COPY . .

# 7. On exécute le code (ajuste le chemin si main.py est dans le sous-dossier app/)
CMD ["python", "app/main.py"]