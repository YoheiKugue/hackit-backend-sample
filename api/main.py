from fastapi import FastAPI

from api.handler import task
from api.handler import note

app = FastAPI()
app.include_router(task.router)
app.include_router(note.router)
#app.include_router(done.router)