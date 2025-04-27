from flask_restx import Namespace, Resource, fields
from model.turma import listar_turmas, adicionar_turma, turma_por_id, atualizar_turma, excluir_turma

turmas_ns = Namespace("turmas", description="Operações relacionadas às turmas")

turma_model = turmas_ns.model("Turma", {
    "descricao": fields.String(required=True, description="Descrição da turma", example="Turma A - Ensino Médio"),
    "professor_id": fields.Integer(required=True, description="ID do professor responsável", example=1),
    "ativo": fields.Boolean(required=True, description="Status da turma (ativa ou não)", example=True),
})

turma_output_model = turmas_ns.model("TurmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "descricao": fields.String(description="Descrição da turma"),
    "ativo": fields.Boolean(description="Status de atividade da turma"),
    "professor_id": fields.Integer(description="ID do professor associado"),
})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    @turmas_ns.response(200, "Lista de turmas obtida com sucesso")
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()

    @turmas_ns.expect(turma_model)
    @turmas_ns.response(201, "Turma criada com sucesso")
    def post(self):
        """Cria uma nova turma"""
        data = turmas_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turmas_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    @turmas_ns.response(200, "Turma encontrada")
    @turmas_ns.response(404, "Turma não encontrada")
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        return turma_por_id(id_turma)

    @turmas_ns.expect(turma_model)
    @turmas_ns.response(200, "Turma atualizada com sucesso")
    @turmas_ns.response(404, "Turma não encontrada para atualização")
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = turmas_ns.payload
        atualizar_turma(id_turma, data)
        return {"message": "Turma atualizada com sucesso"}, 200

    @turmas_ns.response(200, "Turma excluída com sucesso")
    @turmas_ns.response(404, "Turma não encontrada para exclusão")
    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        excluir_turma(id_turma)
        return {"message": "Turma excluída com sucesso"}, 200
