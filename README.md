
# Task Manager API

## 1. Overview

Task Manager API is a RESTful API service built using FastAPI and SQLite Database. It includes services for creating, reading, updating and deleting tasks. Users can create tasks with **title**, **description** and **completed** status


## 2. Implementation

**FastAPI** – Web framework for API development.
    
**Pydantic** – Data validation and serialization.
    
**SQLAlchemy** – ORM for database models and queries.

**SQLite** – Local database for persistent storage.


## 3. API Documentation

Request Type, endpoints, and response/request body in JSON format. Created with the help of FastAPI Swagger UI

### 3.1 Create Task

**POST** **`/tasks/`**

**Request JSON Body**

```json
{
  "title": "Apply for Internship",
  "description": "Looks for Linkedin job postings",
  "completed": false
}
```

**Response JSON Body (201 Created)**

```json
{
  "Detail": "Task successfully Created"
}
```

### 3.2 Get All Tasks

GET `/tasks/`

**Response JSON Body (200 OK)**

```json
[
  {
    "title": "Apply for Internship",
    "description": "Look for Linkedin job postings",
    "completed": false,
    "task_id": 1
  },
  {
    "title": "Clean my room",
    "description": "Use Air Freshner also",
    "completed": true,
    "task_id": 2
  }
]
```


### 3.3 Get Task by ID

**GET `/tasks/{id}`**

**Response JSON Body (200 OK)**

**GET `/tasks/3`**
```json
{
  "title": "Party",
  "description": "Have Fun",
  "completed": true
}
```

**Error (404 Not Found)**

**GET `/tasks/1000000`**
```json

{
  "detail": "Task with id 1000000 not found"
}
```


### 3.4 Update Task by ID

**PUT `/tasks/{id}`**

**Request JSON Body**

**PUT `/tasks/4`**
```json
{
  "title": "Updated Title",
  "description": "Updated Description",
  "completed": true
}
```

**Response JSON Body ( 200 OK)**

```json
{
  "message": "Successfully updated task with id : 4"
}
```

**Response JSON Body (404 Error  : Not Found)**

**PUT `/tasks/345`**
```json
{
  "status_code": 404,
  "detail": "Task with id : 345 not found",
  "headers": null
}
```

### 3.5 Delete Task by ID

**DELETE `/tasks/{id}`**

**`DELETE /tasks/2`**

**Response JSON Body (200 OK)**

```json
{
  "details": "Successfully deleted task with id : 2"
}
```

**Response JSON Body (404 Error : Not Found)**

**DELETE `/tasks/420`**
```json
{
  "status_code": 404,
  "detail": "Task with id : 420 not found",
  "headers": null
}
```



## 4. Validations

## 4.1 Title minimum character length

A validation logic is implemented which prohibits users from creating tasks with **title** less than 3 characters

It was done with the **Pydantic** helper function  known as **Field**

```python
title : str = Field(...,min_length=3)
```

If user tries to create, or update their task's title with less than 3 characters ; 

**POST` /tasks/ ` or  PUT `/tasks/{id}`**
```json
{
  "title": "ab",
  "description": "Nice 3 letter title you got there",
  "completed": false
}
```

**Response Body (422 : Unprocessable Entity)**

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "title"
      ],
      "msg": "String should have at least 3 characters",
      "input": "s",
      "ctx": {
        "min_length": 3
      }
    }
  ]
}
```


## 5. Run Locally

- ### Clone this repository
```bash
git clone https://github.com/GuyVanced/taskmanager-api
```

- ### Go to /taskmanager-api
```bash
cd taskmanager-api
```

- ### Create a virtual environment
```bash
python -m venv venv
```

- ### Activate the virtual environment
```bash
.\venv\Scripts\Activate
```

- ### Install the dependencies
```bash
pip install requirements.txt
```

- ### Run the uvicorn server
```bash
uvicorn app.main:app --reload
```

### Done! Visit 127.0.0.1/tasks/docs for FastAPI Swagger UI

# Thank You!
***GuyVanced***


