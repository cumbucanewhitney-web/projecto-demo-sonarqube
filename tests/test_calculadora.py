from src.calculadora import (
    analisar_compra,
    calcular_media_precos,
    somar_precos,
    somar_quantidades,
)


def test_somar_precos():
    assert somar_precos([10, 20, 30]) == 60


def test_somar_quantidades():
    assert somar_quantidades([1, 2, 3]) == 6


def test_calcular_media_precos():
    assert calcular_media_precos([10, 20, 30]) == 20


def test_analisar_compra_com_cliente_e_desconto():
    resultado = analisar_compra([20, 40], [2, 3], "Ana")
    assert resultado["cliente"] == "Compra de Ana"
    assert resultado["total"] == 73.8
    assert resultado["quantidades"] == 5


def test_analisar_compra_sem_dados():
    resultado = analisar_compra(None, None)
    assert resultado["cliente"] == "Compra sem cliente"
    assert resultado["media"] == 0


def test_analisar_compra_com_total_alto():
    resultado = analisar_compra([60, 60], [6, 6], "Empresa")
    assert resultado["total"] == 147.6


def test_analisar_compra_com_preco_negativo():
    resultado = analisar_compra([-10], [0])
    assert resultado["total"] == 0
    assert resultado["quantidades"] == 0
