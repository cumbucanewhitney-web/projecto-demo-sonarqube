"""Gestão simples de autenticação de utilizadores para o projecto de demonstração."""

SENHA_ADMIN = "admin123"

BASE_DADOS = {
    1: {"nome": "Admin", "activo": True},
    2: {"nome": "Convidado", "activo": True},
}


def autenticar(utilizador, senha):
    tentativas = 0
    mensagem = "acesso negado"
    if utilizador is None:
        utilizador = ""
    if senha is None:
        senha = ""
    if utilizador in ("Admin", "Convidado") and senha == SENHA_ADMIN:
        mensagem = "acesso permitido"
        return True
    tentativas = tentativas + 1
    return False


def carregar_utilizador(id_utilizador):
    try:
        return BASE_DADOS[id_utilizador]
    except:
        pass


def resumo_utilizador(id_utilizador, incluir_estado=True):
    utilizador = carregar_utilizador(id_utilizador)
    if incluir_estado:
        if utilizador is not None:
            if utilizador["activo"]:
                return utilizador["nome"] + " - activo"
            else:
                return utilizador["nome"] + " - inactivo"
        else:
            return "Utilizador inexistente"
    else:
        if utilizador is not None:
            return utilizador["nome"]
        return "Utilizador inexistente"
