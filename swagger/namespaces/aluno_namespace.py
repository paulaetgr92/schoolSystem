from flask_restx import Namespace, Resource, fields
from model.aluno import listar_alunos, adicionar_aluno, aluno_por_id, atualizar_aluno, excluir_aluno

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

aluno_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do aluno", example="João da Silva"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)", example="2005-06-15"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre", example=7.5),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre", example=8.0),
    "turma_id": fields.Integer(required=True, description="ID da turma associada", example=1),
})

aluno_output_model = alunos_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média final do aluno"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    @alunos_ns.response(200, "Lista de alunos obtida com sucesso")
    def get(self):
        """Lista todos os alunos"""
        return listar_alunos()

    @alunos_ns.expect(aluno_model)
    @alunos_ns.response(201, "Aluno criado com sucesso")
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        response, status_code = adicionar_aluno(data)
        return response, status_code

@alunos_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    @alunos_ns.response(200, "Aluno encontrado")
    @alunos_ns.response(404, "Aluno não encontrado")
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return aluno_por_id(id_aluno)

    @alunos_ns.expect(aluno_model)
    @alunos_ns.response(200, "Aluno atualizado com sucesso")
    @alunos_ns.response(404, "Aluno não encontrado para atualização")
    def put(self, id_aluno):
        """Atualiza um aluno pelo ID"""
        data = alunos_ns.payload
        atualizar_aluno(id_aluno, data)
        return {"message": "Aluno atualizado com sucesso"}, 200

    @alunos_ns.response(200, "Aluno excluído com sucesso")
    @alunos_ns.response(404, "Aluno não encontrado para exclusão")
    def delete(self, id_aluno):
        """Exclui um aluno pelo ID"""
        excluir_aluno(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200
