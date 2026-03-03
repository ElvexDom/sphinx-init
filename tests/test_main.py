from app.main import main


def test_main_output(capsys):
    """Vérifie que la fonction main affiche le bon message de bienvenue."""
    main()

    # On capture la sortie de la console
    captured = capsys.readouterr()

    # On vérifie que le message attendu est bien présent
    assert "Hello from sphinx-markdown!" in captured.out

