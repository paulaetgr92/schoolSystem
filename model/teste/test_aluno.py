import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))  
from config import create_app, db
from model.aluno import Aluno, listar_alunos
from model.professor import Professor
import pytest

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


def test_adicionar_aluno(app_context, professor_exemplo):
    
    data_nascimento = datetime.strptime('2005-06-15', '%Y-%m-%d').date()

    aluno = Aluno(
        nome="Aluno A", 
        idade=18, 
        data_nascimento=data_nascimento, 
        nota_primeiro_semestre=7.5, 
        nota_segundo_semestre=8.0,
        turma_id=1  
    )
    db.session.add(aluno)
    db.session.commit()


    aluno_adicionado = Aluno.query.filter_by(nome="Aluno A").first()
    assert aluno_adicionado is not None
    assert aluno_adicionado.nome == "Aluno A"
    assert aluno_adicionado.idade == 18
    assert aluno_adicionado.data_nascimento == data_nascimento

def test_listar_alunos(app_context, professor_exemplo):
    
    data_nascimento = datetime.strptime('2005-06-15', '%Y-%m-%d').date()
    aluno = Aluno(
        nome="Aluno A", idade=18, 
        data_nascimento=data_nascimento, 
        nota_primeiro_semestre=7.5, nota_segundo_semestre=8.0,
        turma_id=1  
    )
    db.session.add(aluno)
    db.session.commit()

    alunos = listar_alunos()  
    assert len(alunos) > 0  
    assert alunos[0]['nome'] == "Aluno A"


def test_buscar_aluno_por_id(app_context, professor_exemplo):
   
    data_nascimento = datetime.strptime('2005-06-15', '%Y-%m-%d').date()
    aluno = Aluno(
        nome="Aluno A", idade=18, 
        data_nascimento=data_nascimento, 
        nota_primeiro_semestre=7.5, nota_segundo_semestre=8.0,
        turma_id=1 
    )
    db.session.add(aluno)
    db.session.commit()

    aluno_id = aluno.id
    aluno_buscado = Aluno.query.get(aluno_id)
    assert aluno_buscado is not None
    assert aluno_buscado.id == aluno_id