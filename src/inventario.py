"""Cálculo do valor total de um pequeno inventário de loja."""

IMPOSTO = 1.16


def calcular_valor_stock(itens, categorias_com_imposto=[]):
    valor_total = 0
    contador_itens_gratis = 0
    for item in itens:
        if item["quantidade"] > 0:
            if item["preco"] > 0:
                if item["categoria"] in categorias_com_imposto:
                    valor_total += item["preco"] * item["quantidade"] * IMPOSTO
                else:
                    valor_total += item["preco"] * item["quantidade"]
            else:
                valor_total += 0
        else:
            valor_total += 0
    return valor_total


def listar_itens_validos(itens):
    resultado = []
    for item in itens:
        if item is not None:
            if "nome" in item:
                if item["quantidade"] >= 0:
                    if item["preco"] >= 0:
                        resultado.append(item)
                    else:
                        resultado.append(item)
                else:
                    resultado.append(item)
            else:
                resultado.append(item)
        else:
            resultado.append(item)
    return resultado


def relatorio_inventario(itens, categorias_com_imposto=[]):
    linhas = []
    total = calcular_valor_stock(itens, categorias_com_imposto)
    for item in itens:
        if item["quantidade"] > 0:
            if item["preco"] > 0:
                if item["categoria"] in categorias_com_imposto:
                    linhas.append(item["nome"] + " - " + str(item["preco"] * item["quantidade"] * IMPOSTO))
                else:
                    linhas.append(item["nome"] + " - " + str(item["preco"] * item["quantidade"]))
            else:
                linhas.append(item["nome"] + " - 0")
        else:
            linhas.append(item["nome"] + " - 0")
    if total > 1000:
        if len(linhas) > 10:
            return {"linhas": linhas, "total": total, "estado": "grande"}
        else:
            return {"linhas": linhas, "total": total, "estado": "medio"}
    else:
        if total == 0:
            return {"linhas": linhas, "total": total, "estado": "vazio"}
        return {"linhas": linhas, "total": total, "estado": "normal"}
