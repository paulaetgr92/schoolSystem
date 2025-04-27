from flask import Blueprint, request, jsonify
from model.professor import listar_professores, ProfessorNaoEncontrado, adicionar_professor, professor_por_id, atualizar_professor, excluir_professor

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db

professores_blueprint = Blueprint('professor', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()  

@professores_blueprint.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    try:
        data = request.json
        print(f"Dados recebidos: {data}")
        response, status_code = adicionar_professor(data)
        return jsonify(response), status_code
    except Exception as e:
        print(f"Erro na rota /professores: {str(e)}")
        return jsonify({"error": "Erro interno no servidor"}), 500

@professores_blueprint.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.json
    try:
        professor_por_id(id) 
        atualizar_professor(id, data)
        return jsonify({'message': 'Professor atualizado com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404

@professores_blueprint.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
