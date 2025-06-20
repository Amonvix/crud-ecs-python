# Usar imagem leve do Python
FROM python:3.12-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos pro container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do FastAPI
EXPOSE 8002

# Rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
