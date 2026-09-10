"""Funções de apoio para somar valores de uma lista de compras."""


def somar_precos(precos):
    return sum(precos)


def somar_quantidades(quantidades):
    return sum(quantidades)


def calcular_media_precos(precos):
    return sum(precos) / len(precos)


def analisar_compra(precos, quantidades, cliente=None):
    resultado = {}
    if cliente:
        texto = "Compra de " + cliente
    else:
        texto = "Compra sem cliente"

    if precos is None:
        precos = []
    if quantidades is None:
        quantidades = []

    resultado["cliente"] = texto
    resultado["total"] = 0
    resultado["quantidades"] = 0
    resultado["media"] = 0

    for preco in precos:
        if preco >= 0:
            resultado["total"] = resultado["total"] + preco
        else:
            resultado["total"] = resultado["total"] + 0

    for quantidade in quantidades:
        if quantidade > 0:
            resultado["quantidades"] = resultado["quantidades"] + quantidade
        else:
            resultado["quantidades"] = resultado["quantidades"] + 0

    if len(precos) > 0:
        resultado["media"] = resultado["total"] / len(precos)
    else:
        resultado["media"] = 0

    imposto = 1.23
    if resultado["total"] > 100:
        if resultado["quantidades"] > 10:
            resultado["total"] = resultado["total"] * imposto
        else:
            resultado["total"] = resultado["total"] * 1.23
    else:
        if resultado["total"] > 50:
            resultado["total"] = resultado["total"] * 1.23
        else:
            resultado["total"] = resultado["total"] * 1

    return resultado
