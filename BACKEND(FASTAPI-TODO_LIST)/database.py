from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

database = client.TodoList

collection = database.todo

async def fetch_one_todo(title: str):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor =  collection.find({})

    async for doc in cursor:
        todos.append(Todo(**doc))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result

async def update_todo(title, desc):
    result = await collection.update_one({"title": title}, {"$set": {"description": desc}})
    if result.modified_count:
        document = await collection.find_one({"title": title}) 
        return document
    return None  

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True