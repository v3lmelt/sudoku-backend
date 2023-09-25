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


@app.get("/sudoku-list/{difficulty}")
async def getSudokuList(difficulty: str):
    return generateSudokuService(difficulty)


@app.get("/fast-sudoku-list/{difficulty}")
async def fastGetSudokuList(difficulty: str):
    return fastGenerateSudokuService(difficulty)
