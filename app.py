from flask import Flask
from config import create_app
from swagger.swagger_config import configure_swagger

from routes.professor_routes import professores_blueprint
from routes.turma_routes import turmas_blueprint
from routes.aluno_routes import alunos_blueprint

app = create_app()

configure_swagger(app)

app.register_blueprint(professores_blueprint, url_prefix="/professores")
app.register_blueprint(turmas_blueprint, url_prefix="/turmas")
app.register_blueprint(alunos_blueprint, url_prefix="/alunos")

if __name__ == "__main__":
    app.run(debug=True)
