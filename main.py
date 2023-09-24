from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Service.GetSudokuListService import generateSudokuService, fastGenerateSudokuService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
#
# @app.get("/sudoku")
# async def getSudoku():
#     return {"sudoku": generateSudokuService()}

@app.get("/sudoku-list")
async def getSudokuList():
    return generateSudokuService()


@app.get("/fast-sudoku-list")
async def fastGetSudokuList():
    return fastGenerateSudokuService()
