import pytest
import pandas as pd
from app.modules.math import add, multiply

# --- 1. PARAMÉTRISATION ---
# On teste 4 scénarios d'un coup (positifs, nuls, négatifs)
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 12),
    (20, 2, 22),
    (0, 2, 2),
    (-1, -1, -2),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """Teste l'addition sur plusieurs cas limites sans dupliquer le code."""
    assert add(a, b) == expected

# --- 2. FIXTURES PANDAS ---
@pytest.fixture
def mock_dataframe():
    """Génère un DataFrame en mémoire pour simuler un fichier CSV."""
    data = {
        "Nom": ["Alice", "Bob"],
        "Age": [25, 30],
        "Ville": ["Paris", "Lyon"]
    }
    return pd.DataFrame(data)

def test_process_data_logic(mock_dataframe):
    """
    Exemple de test utilisant la fixture.
    On imagine que ton module a une fonction qui compte les lignes.
    """
    # Ici, on teste la logique de traitement, pas la lecture du fichier
    assert len(mock_dataframe) == 2
    assert "Age" in mock_dataframe.columns

# --- 3. TESTS UNITAIRES CLASSIQUES ---
def test_multiply_success():
    """Vérifie que la multiplication simple fonctionne toujours."""
    assert multiply(3, 4) == 12