import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db, create_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(500))

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def __repr__(self):
        return f'<Professor {self.nome}>'

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'materia': self.materia, 'observacoes': self.observacoes}
  
class ProfessorNaoEncontrado(Exception):
    pass

def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(f'Professor não encontrado')
    return professor

def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(novos_dados):
    novo_professor = Professor(
        nome=novos_dados['nome'],
        idade=novos_dados['idade'],
        materia=novos_dados['materia'],
        observacoes=novos_dados['observacoes']
    )

    db.session.add(novo_professor)
    db.session.commit()
    return {"message": "Professor adicionado com sucesso!"}, 201

def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado

    professor.nome = novos_dados['nome']
    professor.idade = novos_dados['idade']
    professor.materia = novos_dados['materia']
    professor.observacoes = novos_dados['observacoes']
    
    db.session.commit()

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(f'Professor não encontrado')

    db.session.delete(professor)
    db.session.commit()
