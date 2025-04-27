
from flask import Blueprint, jsonify, request
from model.professor import Professor, adicionar_professor, listar_professores, professor_por_id, atualizar_professor, excluir_professor

professor_bp = Blueprint('professor', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def listar_professores_route():
    try:
        professores = listar_professores()
        return jsonify(professores), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@professor_bp.route('/', methods=['POST'])
def adicionar_professor_route():
    try:
        novos_dados = request.get_json()
        response, status_code = adicionar_professor(novos_dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@professor_bp.route('/<int:id>', methods=['GET'])
def buscar_professor_route(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor_route(id):
    try:
        novos_dados = request.get_json()
        response = atualizar_professor(id, novos_dados)
        return jsonify({'message': 'Professor atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@professor_bp.route('/<int:id>', methods=['DELETE'])
def excluir_professor_route(id):
    try:
        excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 404
