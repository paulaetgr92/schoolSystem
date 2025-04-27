from flask import Flask, request, Response
from swagger import api
from swagger.namespaces.aluno_namespace import alunos_ns
from swagger.namespaces.professor_namespace import professores_ns
from swagger.namespaces.turma_namespace import turmas_ns

# Definindo os namespaces e suas rotas
namespaces = [
    (alunos_ns, "/alunos"),
    (professores_ns, "/professores"),
    (turmas_ns, "/turmas"),
]

def configure_swagger(app):
    api.init_app(app)

    # Adicionando os namespaces ao API
    for ns, path in namespaces:
        api.add_namespace(ns, path=path)
    
    # Desabilitando a máscara do Swagger para personalizações
    api.mask_swagger = False  

    # Aplicando o tema escuro no Swagger
    @app.after_request
    def aplicar_tema_escuro(response: Response):
        if request.path == "/swagger" and response.content_type.startswith("text/html"):
            response.set_data(
                response.get_data().replace(b"theme: 'flattop'", b"theme: 'dark'")
            )
        return response  # Não esqueça de retornar a resposta após a modificação

