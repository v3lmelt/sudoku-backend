from pydantic import BaseModel
from typing import Union


class sudokuArray(BaseModel):
    sudoku: Union[list, list[list[int]]]