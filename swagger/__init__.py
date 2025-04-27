from flask_restx import Api

api = Api(
    title="School System API",
    version="1.0",
    description="API para gerenciamento de alunos, professores e turmas",
    doc="/swagger"  
)
