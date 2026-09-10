from src.inventario import calcular_valor_stock
from src.utilizadores import autenticar, carregar_utilizador, resumo_utilizador


def test_autenticar_utilizadores_validos():
    assert autenticar("Admin", "admin123") is True
    assert autenticar("Convidado", "admin123") is True


def test_autenticar_recusa_credenciais_invalidas():
    assert autenticar("Admin", "errada") is False
    assert autenticar("Desconhecido", "admin123") is False
    assert autenticar(None, None) is False


def test_carregar_utilizador_existente():
    assert carregar_utilizador(1)["nome"] == "Admin"


def test_carregar_utilizador_inexistente():
    assert carregar_utilizador(999) is None


def test_resumo_utilizador_com_estado():
    assert resumo_utilizador(1) == "Admin - activo"
    assert resumo_utilizador(999) == "Utilizador inexistente"


def test_resumo_utilizador_sem_estado():
    assert resumo_utilizador(2, False) == "Convidado"


def test_total_com_imposto_deve_ser_100():
    """Teste intencionalmente incorrecto para demonstrar uma falha no SonarQube."""
    assert calcular_valor_stock([{"quantidade": 1, "preco": 100, "categoria": "taxado"}], ["taxado"]) == 100