
from flask import Blueprint, jsonify, request
from model.aluno import Aluno, adicionar_aluno, listar_alunos, aluno_por_id, atualizar_aluno, excluir_aluno

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET'])
def listar_alunos_route():
    try:
        alunos = listar_alunos()
        return jsonify(alunos), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@aluno_bp.route('/', methods=['POST'])
def adicionar_aluno_route():
    try:
        novos_dados = request.get_json()
        response, status_code = adicionar_aluno(novos_dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@aluno_bp.route('/<int:id>', methods=['GET'])
def buscar_aluno_route(id):
    try:
        aluno = aluno_por_id(id)
        return jsonify(aluno), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno_route(id):
    try:
        novos_dados = request.get_json()
        atualizar_aluno(id, novos_dados)
        return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@aluno_bp.route('/<int:id>', methods=['DELETE'])
def excluir_aluno_route(id):
    try:
        excluir_aluno(id)
        return jsonify({'message': 'Aluno excluído com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404
