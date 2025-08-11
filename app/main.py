from fastapi import FastAPI
from .routers import task as task_router
from .models import task
from .core.database import Base, engine

app = FastAPI()

# To create all the tables
Base.metadata.create_all(engine)

# To include toute to endpoints defined in task router
app.include_router(task_router.router, prefix="/api")

@app.get("/", status_code=200)
def main():
    return {"message" : "Welcome"}

