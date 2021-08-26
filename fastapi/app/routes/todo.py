from fastapi import APIRouter, Body, HTTPException, Request, status

from ..schemas.todo import Todo
from ..cruds.todo import fetch_all_todos, fetch_one_todo, create_todo, update_todo, remove_todo

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.get("/")
async def get_todo():
    response = await fetch_all_todos()
    return response

@router.get("/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@router.post("/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@router.put("/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@router.delete("/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")