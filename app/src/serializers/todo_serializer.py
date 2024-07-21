# one todo
def task(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["is_completed"]
    }

# all todos
def all_tasks(todos) -> list:
    return [task(todo) for todo in todos]