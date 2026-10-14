from flask import abort, redirect, request, url_for
from flask_login import current_user


PERMISSOES_ROTAS = {
    'area_plus': ['PLUS'],
}


def autorizar(lista_permissoes):
    """Verifica se o usuário possui uma das permissões informadas."""
    if current_user.role not in lista_permissoes:
        abort(403)

    return None


def verificar_autorizacao():
    """Executa a verificação antes das rotas que possuem permissões."""
    lista_permissoes = PERMISSOES_ROTAS.get(request.endpoint)

    if lista_permissoes is None:
        return None

    return autorizar(lista_permissoes)
