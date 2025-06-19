# main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from logger import logger
from routers import task as task_router
from database import Base, engine, SessionLocal
from models.task import TaskModel



# Initialize FastAPI application instance
app = FastAPI()
app.include_router(task_router.router)


templates = Jinja2Templates(directory="templates")

# Register the task router under the default prefix
app.include_router(task_router.router)

# Enable direct execution via `python main.py`
if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Application started")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



@app.get("/form", response_class=HTMLResponse)
async def show_form(request:Request):
    db: Session = SessionLocal()
    tasks = db.query(TaskModel).order_by(TaskModel.id.desc()).all()
    db.close()
    return templates.TemplateResponse("form.html", {"request": request, "tasks": tasks})

@app.post("/submit")
async def submit_form(
    title: str = Form(...),
    description: str = Form(None),
    status: str = Form(...),
):
    db: Session = SessionLocal()
    try:
        new_task = TaskModel(title=title, description=description, status=status)
        db.add(new_task)
        db.commit()
    finally:
        db.close()
    return RedirectResponse(url="/form", status_code=303)

@app.get("/", include_in_schema=False)
def redirect_to_form():
    return RedirectResponse(url="/form")

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
