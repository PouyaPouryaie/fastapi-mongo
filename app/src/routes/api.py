from fastapi import APIRouter
from .todo import todo_root
from .entry import entry_root


router = APIRouter()

router.include_router(entry_root, prefix="/health_check", tags=["HealthCheck"])
router.include_router(todo_root, prefix="/todo", tags=["Todo"])