from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Text

# Start the application by using
# uvicorn main:app

app = FastAPI()

#Constante para manejar blogs
blog = "/blog"

# Creating our fake database

postDb = []

class Post(BaseModel):
    id: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False




@app.get(blog)
async def get_post():
    return postDb


@app.post(blog)
async def add_post(post: Post):
    postDb.append(post.dict())
    # Los indices de las listas empiezan en 0
    # Retornamos el ultimo elemento agregado
    return postDb[-1]

@app.put(blog)
async def update_post(post: Post):
    postDb[post.id - 1] = post
    # Los indices de las listas empiezan en 0
    # Retornamos el ultimo elemento agregado
    return postDb[post.id -1]


@app.delete(blog+"/{post_id}")
async def delete_post(post_id: int):
    postDb.pop(post_id -1)
    return {"message": f"The blog with id {post_id} has been deleted successfully"}


@app.get(blog+"/details/{post_id}")
async def details_post(post_id: int):
    return postDb[post_id -1]

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/testing/{name}")
async def testing(name: str):
    return {"message": f"Hey {name} we are testing this API"}
