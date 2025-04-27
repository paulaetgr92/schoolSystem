import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import create_app, db
from model.professor import Professor
import pytest


@pytest.fixture(scope='module')
def app_context():
    app = create_app()
    with app.app_context():  
        db.create_all()  
        yield app  
        db.session.remove()  # 
        db.drop_all()  


@pytest.fixture
def professor_exemplo(app_context):
    professor = Professor(nome="Professor A", idade=40, materia="Matemática", observacoes="Observações")
    db.session.add(professor)
    db.session.commit()
    return professor


def test_adicionar_professor(app_context):
    professor = Professor(nome="Professor B", idade=35, materia="Física", observacoes="Professor de Física")
    db.session.add(professor)
    db.session.commit()
    assert professor.id is not None  

def test_listar_professores(app_context):
    professores = Professor.query.all()
    assert len(professores) > 0  


def test_buscar_professor_por_id(app_context, professor_exemplo):
    professor = Professor.query.get(professor_exemplo.id)
    assert professor is not None  
    assert professor.nome == "Professor A"  


def test_atualizar_professor(app_context, professor_exemplo):
    professor_exemplo.nome = "Professor A Atualizado"
    db.session.commit()
    assert professor_exemplo.nome == "Professor A Atualizado"  

def test_excluir_professor(app_context, professor_exemplo):
    db.session.delete(professor_exemplo)
    db.session.commit()
    professor = Professor.query.get(professor_exemplo.id)
    assert professor is None  