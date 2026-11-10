from flask import Blueprint, render_template


erros_bp = Blueprint("erros", __name__)

@erros_bp.app_errorhandler(403)
def nao_autorizado(e):
    return render_template('erros/403.html'), 403