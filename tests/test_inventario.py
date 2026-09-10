from src.inventario import (
    calcular_valor_stock,
    listar_itens_validos,
    relatorio_inventario,
)


def test_calcular_valor_stock_com_e_sem_imposto():
    itens = [
        {"nome": "livro", "quantidade": 2, "preco": 10, "categoria": "normal"},
        {"nome": "computador", "quantidade": 1, "preco": 100, "categoria": "taxado"},
        {"nome": "gratuito", "quantidade": 0, "preco": 0, "categoria": "normal"},
    ]
    assert calcular_valor_stock(itens, ["taxado"]) == 136.0


def test_listar_itens_validos_preserva_entradas():
    itens = [
        {"nome": "bom", "quantidade": 1, "preco": 2},
        None,
        {"quantidade": -1, "preco": 2},
    ]
    assert listar_itens_validos(itens) == itens


def test_relatorio_inventario_estado_vazio():
    assert relatorio_inventario([])["estado"] == "vazio"


def test_relatorio_inventario_estado_normal():
    itens = [{"nome": "caneta", "quantidade": 1, "preco": 2, "categoria": "papel"}]
    relatorio = relatorio_inventario(itens)
    assert relatorio["estado"] == "normal"
    assert relatorio["linhas"] == ["caneta - 2"]


def test_relatorio_inventario_estado_medio():
    itens = [{"nome": "monitor", "quantidade": 1, "preco": 900, "categoria": "taxado"}]
    assert relatorio_inventario(itens, ["taxado"])["estado"] == "medio"


def test_relatorio_inventario_estado_grande():
    itens = [
        {"nome": str(numero), "quantidade": 1, "preco": 101, "categoria": "normal"}
        for numero in range(11)
    ]
    assert relatorio_inventario(itens)["estado"] == "grande"


def test_relatorio_inventario_com_item_gratuito():
    itens = [{"nome": "amostra", "quantidade": 1, "preco": 0, "categoria": "normal"}]
    assert relatorio_inventario(itens)["linhas"] == ["amostra - 0"]