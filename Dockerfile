FROM python:3.10-slim

# Criar e acessar o diretório da aplicação
WORKDIR /app

# Copiar os arquivos da aplicação para o contêiner
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Criar um usuário sem privilégios de root
RUN useradd -m appuser

# Definir o usuário não root para rodar a aplicação
USER appuser

# Definir a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]


