
# API using FastAPI and python

## Important tools and dependencies

- pipenv
- fastapi
- uvicorn
- pydantic
- typing

## Project setup


### Creating a directory for out project
```
mkdir create fastApiProject && cd fastApiProject
```

### Creating and activating a virtual environment

Install dependencies
```
pipenv install fastapi uvicorn
```

Activate environment

```
pipenv shell
```


### Create a file

Create a main.py file and add the following lines

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

```

## Run our project

```
uvicorn main:app
```

### Test

Open a window and access the url

```
http://localhost:8000
```

You will see the json

```json
{ 
  "message": "Hello World"
}
```

## Endpoints documentation

### Add blog

Url

```
http://localhost:8000/blog
```

Body
```json
{
  "id": 1,
  "title": "Getting started with Django",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}
```

Response

```json
{
  "id": 1,
  "title": "Getting started with Django",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}
```

Curl

```
curl --location --request POST 'http://localhost:8000/blog' \
--header 'Content-Type: application/json' \
--data-raw '{
  "id": 1,
  "title": "Getting started with Django",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}'
```

### Update blog

Url

```
http://localhost:8000/blog
```

Body
```json
{
  "id": 1,
  "title": "Getting started with Django, updating data",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}
```

Response

```json
{
  "id": 1,
  "title": "Getting started with Django, updating data",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}
```

Curl

```
curl --location --request PUT 'http://localhost:8000/blog' \
--header 'Content-Type: application/json' \
--data-raw '{
  "id": 1,
  "title": "Getting started with Django, updating data",
  "author": "Ousseynou DIOP",
  "content": "Hello Django",
  "created_at": "2021-03-01T18:17:45.194020",
  "published_at": "2021-03-01T18:17:58.887Z",
  "published": true
}'
```


### Blog list 

Url

```
http://localhost:8000/blog
```


Response

```json
[
    {
        "id": 1,
        "title": "Getting started with Django",
        "author": "Ousseynou DIOP",
        "content": "Hello Django",
        "created_at": "2021-03-01T18:17:45.194020",
        "published_at": "2021-03-01T18:17:58.887000+00:00",
        "published": true
    }
]
```

Curl

```
curl --location --request GET 'http://localhost:8000/blog'
```

### blog details

Url

```
http://localhost:8000/blog/details/{post_id}
```

Response

```json
{
    "id": 1,
    "title": "Getting started with Django",
    "author": "Ousseynou DIOP",
    "content": "Hello Django",
    "created_at": "2021-03-01T18:17:45.194020",
    "published_at": "2021-03-01T18:17:58.887000+00:00",
    "published": true
}
```

Curl

```
curl --location --request GET 'http://localhost:8000/blog/details/1'
```

### Delete a blog

Url

```
http://localhost:8000/blog/{post_id}
```

Response

```json
{
    "message": "The blog with id 1 has been deleted successfully"
}
```

Curl

```
curl --location --request DELETE 'http://localhost:8000/blog/1'
```
