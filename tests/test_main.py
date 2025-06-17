from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Testar endpoint",
        "description": "Primeiro teste automatizado",
        "completed": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Testar endpoint"
    assert "id" in data

def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_task_by_id():
    # Create first
    post = client.post("/tasks", json={
        "title": "Tarefa única",
        "description": "Buscar por ID",
        "completed": False
    })
    task_id = post.json()["id"]

    # Than search
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    
def test_update_task():
    # Create a task
    post = client.post("/tasks", json={
        "title": "Original",
        "description": "Desc",
        "completed": False
    })
    task_id = post.json()["id"]

    # Atualize a task
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Atualizado",
        "description": "Atualizado com sucesso",
        "completed": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Atualizado"
    assert data["completed"] is True

def test_delete_task():
    # Create a task
    post = client.post("/tasks", json={
        "title": "Para deletar",
        "description": "Temporária",
        "completed": False
    })
    task_id = post.json()["id"]

    # Delete a task
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Task deleted successfully"

    # Ensures it was deleted
    get = client.get(f"/tasks/{task_id}")
    assert get.status_code == 404
