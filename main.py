from fastapi import FastAPI

from Service.GetSudokuListService import generateSudokuService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/sudoku")
async def getSudoku():
    return {"sudoku": generateSudokuService()}
