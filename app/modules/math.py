"""Module regroupant les fonctions mathématiques de base.

Ce module fournit des outils simples pour démontrer l'utilisation
de Ruff, Pytest et Sphinx.
"""


def add(a: int, b: int) -> int:
    """Additionne deux nombres entiers.

    Args:
        a: Le premier nombre entier.
        b: Le deuxième nombre entier.

    Returns:
        La somme de a et b.

    Example:
        >>> add(2, 3)
        5

    """
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiplie deux nombres entiers.

    Args:
        a: Le premier facteur.
        b: Le deuxième facteur.

    Returns:
        Le produit de a et b.

    """
    return a * b
