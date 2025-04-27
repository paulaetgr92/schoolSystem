import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from model.professor import Professor
from model.turma import Turma, adicionar_turma, atualizar_turma, excluir_turma, TurmaNaoEncontrada
from config import create_app, db

@pytest.fixture(scope='module')
def app_context():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

@pytest.fixture
def professor_exemplo(app_context):
    professor = Professor(nome="Professor A", idade=40, materia="Matemática", observacoes="Professor de exemplo")
    db.session.add(professor)
    db.session.commit()
    return professor

def test_criar_turma(app_context, professor_exemplo):
    dados_turma = {
        "descricao": "Turma Teste",
        "professor_id": professor_exemplo.id,
        "ativo": True
    }
    response = adicionar_turma(dados_turma)  
    assert response[1] == 201  
    assert response[0]['message'] == "Turma criada com sucesso!"  

def test_buscar_turma(app_context):
    turma = db.session.get(Turma, 1)  
    response = turma_por_id(turma.id)  
    assert response['descricao'] == "Turma Teste"  

def test_atualizar_turma(app_context, professor_exemplo):
    turma = db.session.get(Turma, 1)  
    novos_dados = {
        "descricao": "Turma Atualizada",
        "professor_id": professor_exemplo.id,
        "ativo": True
    }
    response = atualizar_turma(turma.id, novos_dados) 
    assert response[1] == 200  
    assert response[0]['message'] == "Turma atualizada com sucesso!"  


def test_excluir_turma(app_context, professor_exemplo):
    turma = db.session.get(Turma, 1) 
    response = excluir_turma(turma.id)  
    assert response[1] == 200  
    assert response[0]['message'] == "Turma excluída com sucesso!"  
    assert db.session.get(Turma, turma.id) is None  


def turma_por_id(id_turma):
    turma = db.session.get(Turma, id_turma)  
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada')
    return turma.to_dict()
