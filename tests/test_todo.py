from fastapi.testclient import TestClient
from app.main import app
from app.src.models.todo_model import Todo
import json

client = TestClient(app)

ENDPOINT = "/todo"

def test_get_all_todos():
    response = client.get("/todo")
    assert response.status_code == 200
    
    print(response.json())

def test_create_todo():
    # create Task
    sample_todo = dict(create_sample_task())
    response = create_task(sample_todo)
    data = response.json()
    print(data)

    # get Task and check value
    task_id = data["body"]["id"]
    find_todo_response = get_task(task_id)
    assert response.status_code == 200
    todo = find_todo_response.json()
    assert todo['body']['title'] == sample_todo['title']

def test_update_todo():
    # create Task
    sample_todo = create_sample_task()
    create_todo_response = create_task(dict(sample_todo))
    assert create_todo_response.status_code == 200
    data = create_todo_response.json()

    # update Task
    task_id = data["body"]["id"]
    sample_todo.description = "this is a new description"
    update_todo_response = update_task(task_id=task_id, payload=dict(sample_todo))
    assert update_todo_response.status_code == 200

    # get Task and check value
    find_todo_response = get_task(task_id)
    assert find_todo_response.status_code == 200
    todo = find_todo_response.json()
    assert todo['body']['description'] == sample_todo.description

def test_delete_todo():
    # create Task
    sample_todo = dict(create_sample_task())
    create_task_response = create_task(sample_todo)

    # delete Task
    task_id = create_task_response.json()["body"]["id"]
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # get Task and check value is not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404



def create_task(payload):
    return client.post(ENDPOINT, json=payload)

def get_task(task_id):
    return client.get(ENDPOINT + f"/{task_id}")

def update_task(task_id, payload):
    return client.put(ENDPOINT + f"/{task_id}", json=payload)

def delete_task(task_id):
    return client.delete(ENDPOINT + f"/{task_id}")

def create_sample_task():
    return Todo(
        title="test_task",
        description="test_description"
    )