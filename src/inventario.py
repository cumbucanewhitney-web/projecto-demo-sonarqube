"""Cálculo do valor total de um pequeno inventário de loja."""

IMPOSTO = 1.16


def calcular_valor_stock(itens, categorias_com_imposto=None):
    if categorias_com_imposto is None:
        categorias_com_imposto = []

    valor_total = 0
    for item in itens:
        if item["quantidade"] <= 0 or item["preco"] <= 0:
            continue

        valor_item = item["preco"] * item["quantidade"]
        if item["categoria"] in categorias_com_imposto:
            valor_item *= IMPOSTO
        valor_total += valor_item
    return valor_total


def listar_itens_validos(itens):
    return list(itens)


def relatorio_inventario(itens, categorias_com_imposto=None):
    if categorias_com_imposto is None:
        categorias_com_imposto = []

    linhas = []
    total = calcular_valor_stock(itens, categorias_com_imposto)
    for item in itens:
        valor_item = 0
        if item["quantidade"] > 0 and item["preco"] > 0:
            valor_item = item["preco"] * item["quantidade"]
            if item["categoria"] in categorias_com_imposto:
                valor_item *= IMPOSTO
        linhas.append(f"{item['nome']} - {valor_item}")

    if total > 1000:
        estado = "grande" if len(linhas) > 10 else "medio"
    elif total == 0:
        estado = "vazio"
    else:
        estado = "normal"
    return {"linhas": linhas, "total": total, "estado": estado}
