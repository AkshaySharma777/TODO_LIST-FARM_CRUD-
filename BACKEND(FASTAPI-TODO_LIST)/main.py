from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

from database import (
  fetch_one_todo,
  fetch_all_todos,
  create_todo,
  update_todo,
  remove_todo
)

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_headers = ['*'],
    allow_methods = ["*"],
    allow_credentials = True
)

@app.get("/")
def get_index():
    return {
        "Message": "Hello!, Welcome to Home Page",
    }

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"There is no TODO item with the title '{title}'")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return todo
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"There is no TODO item with the title '{title}'")

@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return 'Successfully deleted ' + title +  'todo item'
    raise HTTPException(status_code=404, detail=f"There is no TODO item with the title '{title}'")