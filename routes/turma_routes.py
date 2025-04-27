from flask import Blueprint, request, jsonify
from model.turma import (
    Turma,
    TurmaNaoEncontrada,
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma
)
from model.professor import Professor
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return jsonify(turmas)

@turmas_blueprint.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    try:
        turma = turma_por_id(id)
        professor = Professor.query.get(turma['professor_id'])
        if professor is None:
            return jsonify({'message': 'Professor não encontrado'}), 404
        return jsonify({"turma": turma, "professor": professor.to_dict()})
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    try:
        data = request.json
        print(f"Dados recebidos: {data}")
        response, status_code = adicionar_turma(data)
        return jsonify(response), status_code
    except Exception as e:
        print(f"Erro na rota /turmas: {str(e)}")
        return jsonify({"error": "Erro interno no servidor"}), 500

@turmas_blueprint.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.json
    try:
        turma_por_id(id)  
        atualizar_turma(id, data)
        return jsonify({'message': 'Turma atualizada com sucesso'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404


@turmas_blueprint.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
