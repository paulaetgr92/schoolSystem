from flask_restx import Namespace, Resource, fields
from model.professor import listar_professores, adicionar_professor, professor_por_id, atualizar_professor, excluir_professor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor", example="Maria Souza"),
    "materia": fields.String(required=True, description="Matéria ensinada pelo professor", example="Matemática"),
})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "materia": fields.String(description="Matéria ensinada"),
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    @professores_ns.response(200, "Lista de professores obtida com sucesso")
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @professores_ns.expect(professor_model)
    @professores_ns.response(201, "Professor criado com sucesso")
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    @professores_ns.response(200, "Professor encontrado")
    @professores_ns.response(404, "Professor não encontrado")
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return professor_por_id(id_professor)

    @professores_ns.expect(professor_model)
    @professores_ns.response(200, "Professor atualizado com sucesso")
    @professores_ns.response(404, "Professor não encontrado para atualização")
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        atualizar_professor(id_professor, data)
        return {"message": "Professor atualizado com sucesso"}, 200

    @professores_ns.response(200, "Professor excluído com sucesso")
    @professores_ns.response(404, "Professor não encontrado para exclusão")
    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        excluir_professor(id_professor)
        return {"message": "Professor excluído com sucesso"}, 200
