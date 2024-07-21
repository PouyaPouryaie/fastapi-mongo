from fastapi import FastAPI, APIRouter, HTTPException
from connection_db import collection
from database.schemas import all_tasks
from database.models import Todo
from bson import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted": False})
    return all_tasks(data)

@router.post("/")
async def create_task(new_task: Todo):

    try:
        response = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(response.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:

        # Validate task ID format (if necessary)
        if not ObjectId.is_valid(task_id):
            return HTTPException(status_code=400, detail="Invalid task ID format")

        id = ObjectId(task_id)

        # Find existing document with filtering for active tasks
        check_doc = collection.find_one({"_id": id, "is_deleted": False})
        if not check_doc:
            return HTTPException(status_code=404, detail=f"Task with ID {task_id} not found or is deleted")
        
        updated_task.update_at = int(datetime.timestamp(datetime.now()))

        # Update document with optimistic locking (optional)
        result = collection.update_one({"_id": id, "is_deleted": False}, {"$set": dict(updated_task)})

        if result.matched_count == 0:
            # Handle potential race conditions (optional)
            # Consider retry logic or conflict resolution mechanisms
            return HTTPException(status_code=409, detail="Optimistic locking conflict: Task might be updated by another process")

        return {"status_code": 200, "message": "task Updated Successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:

        # Validate task ID format (if necessary)
        if not ObjectId.is_valid(task_id):
            return HTTPException(status_code=400, detail="Invalid task ID format")

        id = ObjectId(task_id)

        # Find existing document with filtering for active tasks
        # check_doc = collection.find_one({"_id": id, "is_deleted": False})
        # if not check_doc:
        #     return HTTPException(status_code=404, detail=f"Task with ID {task_id} not found or is deleted")
        
        # result = collection.update_one({"_id": id}, {"$set": {"is_deleted": True, "update_at": int(datetime.timestamp(datetime.now()))}})
        
        result = collection.find_one_and_update({"_id": id}, {"$set": {"is_deleted": True, "update_at": int(datetime.timestamp(datetime.now()))}})

        return {"status_code": 200, "message": "Task deleted Successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

app.include_router(router)