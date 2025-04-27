
from flask import Blueprint, jsonify, request
from model.turma import Turma, adicionar_turma, listar_turmas, turma_por_id, atualizar_turma, excluir_turma

turma_bp = Blueprint('turma', __name__, url_prefix='/turmas')

@turma_bp.route('/', methods=['GET'])
def listar_turmas_route():
    try:
        turmas = listar_turmas()
        return jsonify(turmas), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@turma_bp.route('/', methods=['POST'])
def adicionar_turma_route():
    try:
        novos_dados = request.get_json()
        response, status_code = adicionar_turma(novos_dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@turma_bp.route('/<int:id>', methods=['GET'])
def buscar_turma_route(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma_route(id):
    try:
        novos_dados = request.get_json()
        atualizar_turma(id, novos_dados)
        return jsonify({'message': 'Turma atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@turma_bp.route('/<int:id>', methods=['DELETE'])
def excluir_turma_route(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404
