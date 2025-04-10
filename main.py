from fastapi import FastAPI

import models
from database import engine
models.Base.metadata.create_all(bind=engine)

import board.board_router as board_router

app = FastAPI()

app.include_router(board_router.app, tags=["board"])

@app.get("/")
def read_root():
    return {"Hello":"World"}