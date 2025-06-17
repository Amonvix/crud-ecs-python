# main.py

from fastapi import FastAPI
from routers import task as task_router
from models import task  
from fastapi.responses import RedirectResponse
from database import Base, engine


# Initialize FastAPI application instance
app = FastAPI(
    title="ToDo API",
    description="A simple task management API using FastAPI and SQLite",
    version="1.0.0"
)

# Register the task router under the default prefix
app.include_router(task_router.router)

# Enable direct execution via `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
    