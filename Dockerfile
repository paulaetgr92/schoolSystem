# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usa
EXPOSE 5000

# Comando para iniciar o app
CMD ["python", "app.py"]

