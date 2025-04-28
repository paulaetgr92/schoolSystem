from flask import Flask
from config import create_app
from swagger.swagger_config import configure_swagger

from routes.professor_routes import professores_blueprint
from routes.turma_routes import turmas_blueprint
from routes.aluno_routes import alunos_blueprint

import os

app = create_app()

configure_swagger(app)


# 🛠️ Registrando os blueprints
app.register_blueprint(professores_blueprint, url_prefix="/professores")
app.register_blueprint(turmas_blueprint, url_prefix="/turmas")
app.register_blueprint(alunos_blueprint, url_prefix="/alunos")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
