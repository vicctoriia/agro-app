from http import HTTPStatus
from flask import Blueprint, jsonify, request
from .models import get_crop_data

bp = Blueprint('agro_app', __name__)

@bp.get('/')
def health_check():
    """Index teste."""
    return {'status': 'Ok'}, HTTPStatus.OK

@bp.route('/crop-data')
def fetch_crop_data():
    """Rota que aciona o BD."""
    filters = request.args.to_dict()
    data = get_crop_data(filters)

    return jsonify(data)
