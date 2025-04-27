from flask import Blueprint, request, jsonify
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db, create_app 
from model.aluno import Aluno, adicionar_aluno
from model.turma import Turma


alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])


@alunos_blueprint.route('/alunos/<int:id>', methods=['GET'])
def aluno_por_id(id):
    aluno = Aluno.query.get(id)
    if aluno is None:
        return jsonify({"error": "Aluno não encontrado"}), 404
    return jsonify(aluno.to_dict())

@alunos_blueprint.route('/alunos', methods=['POST'])
def criar_aluno():
    novos_dados = request.get_json()  
    return adicionar_aluno(novos_dados)


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    data = request.json
    aluno = Aluno.query.get(id_aluno)
    if aluno is None:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    

    aluno.nome = data.get('nome', aluno.nome)
    aluno.idade = data.get('idade', aluno.idade)
    aluno.data_nascimento = data.get('data_nascimento', aluno.data_nascimento)
    aluno.turma_id = data.get('turma_id', aluno.turma_id)
    aluno.ativo = data.get('ativo', aluno.ativo)
    
    db.session.commit()
    
    return jsonify({'message': 'Aluno atualizado com sucesso'}), 200


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno is None:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    
    db.session.delete(aluno)
    db.session.commit()
    
    return jsonify({'message': 'Aluno excluído com sucesso'}), 200
