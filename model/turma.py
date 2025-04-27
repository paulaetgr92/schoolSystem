import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db
from model.professor import Professor

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    professor = db.relationship('Professor', backref='turmas', lazy=True)

    def __init__(self, descricao, ativo, professor_id):
        self.descricao = descricao
        self.ativo = ativo
        self.professor_id = professor_id

    def __repr__(self):
        return f'<Turma {self.descricao}>'

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'ativo': self.ativo, 'professor_id': self.professor_id}

class TurmaNaoEncontrada(Exception):
    pass

def turma_por_id(id_turma):
    turma = db.session.get(Turma, id_turma)
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada')
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(novos_dados):
    professor = db.session.get(Professor, novos_dados['professor_id'])  
    if not professor:
        return {"message": "Professor não existe"}, 404

    nova_turma = Turma(
        descricao=novos_dados['descricao'],
        ativo=novos_dados['ativo'],
        professor_id=novos_dados['professor_id']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return {"message": "Turma criada com sucesso!"}, 201

def atualizar_turma(id_turma, novos_dados):
    turma = db.session.get(Turma, id_turma)  
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada')

    turma.descricao = novos_dados['descricao']
    turma.ativo = novos_dados['ativo']
    turma.professor_id = novos_dados['professor_id']

    db.session.commit()
    return {"message": "Turma atualizada com sucesso!"}, 200

def excluir_turma(id_turma):
    turma = db.session.get(Turma, id_turma)
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada')

    db.session.delete(turma)
    db.session.commit()
    return {"message": "Turma excluída com sucesso!"}, 200
