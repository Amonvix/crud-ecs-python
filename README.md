# 📋 crud-ecs-python

Aplicação FastAPI para gerenciamento de tarefas, com interface web, API RESTful e empacotamento pronto para deploy em ambientes Docker e AWS ECS.

> 💡 Projeto faz parte do conjunto de três microserviços preparados para serem implantados em uma infraestrutura automatizada com Terraform + AWS.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.12
- ⚡ FastAPI
- 🔧 Uvicorn
- 🛢️ SQLite
- 🧠 Jinja2 (Templates HTML)
- 🐳 Docker
- 🌩️ Pronto para deploy via AWS ECS

---

## 📦 Como Rodar Localmente

### Sem Docker:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
