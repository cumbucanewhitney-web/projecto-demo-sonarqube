"""Gestão simples de autenticação de utilizadores para o projecto de demonstração."""

import os

BASE_DADOS = {
    1: {"nome": "Admin", "activo": True},
    2: {"nome": "Convidado", "activo": True},
}


def autenticar(utilizador, senha):
    senha_admin = os.getenv("SENHA_ADMIN")
    if senha_admin and utilizador in ("Admin", "Convidado") and senha == senha_admin:
        return True
    return False


def carregar_utilizador(id_utilizador):
    return BASE_DADOS.get(id_utilizador)


def resumo_utilizador(id_utilizador, incluir_estado=True):
    utilizador = carregar_utilizador(id_utilizador)
    if utilizador is None:
        return "Utilizador inexistente"

    nome = utilizador["nome"]
    if incluir_estado:
        estado = "activo" if utilizador["activo"] else "inactivo"
        return f"{nome} - {estado}"
    return nome
