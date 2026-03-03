"""Tests unitaires pour le module mathématique."""

from app.modules.mon_module import add, multiply


def test_add_success():
    """Vérifie que l'addition de deux entiers fonctionne."""
    a, b = 10, 5
    result = add(a, b)
    assert result == 15

def test_multiply_success():
    """Vérifie que la multiplication fonctionne."""
    assert multiply(3, 4) == 12

def test_add_negative_numbers():
    """Vérifie l'addition avec des nombres négatifs."""
    assert add(-1, -1) == -2
