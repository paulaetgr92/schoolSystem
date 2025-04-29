import os
from flask import Flask
from config import create_app, db
from swagger.swagger_config import configure_swagger

from routes.professor_routes import professores_blueprint
from routes.turma_routes import turmas_blueprint
from routes.aluno_routes import alunos_blueprint
from routes.api_rooutes import api_dp

# Cria a aplicação Flask
app = create_app()

# Inicializa a extensão SQLAlchemy com o app
db.init_app(app)

# Cria todas as tabelas (somente durante o desenvolvimento)
with app.app_context():
    db.create_all()

# Configura o Swagger
configure_swagger(app)

# Registra os blueprints das rotas
app.register_blueprint(professores_blueprint, url_prefix="/professores")
app.register_blueprint(turmas_blueprint, url_prefix="/turmas")
app.register_blueprint(alunos_blueprint, url_prefix="/alunos")
app.register_blueprint(api_dp)

# Apenas executa se for rodar diretamente (não executa no gunicorn, etc.)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
