import threading
import unittest
from concurrent.futures import ThreadPoolExecutor

from fastapi.encoders import jsonable_encoder

from Modules.FASTSudokuGenerateModule import fastSudokuGenerate
from Modules.SudokuGenerateModule import SudokuGenerator, getFormattedAnswer, removeSlotFromSudoku

'''
原始的基于Dance Link X的数独生成服务
'''
EASY_SLOT_REMOVE = 25
NORMAL_SLOT_REMOVE = 40
HARD_SLOT_REMOVE = 64


def generateSudokuService(difficulty: str):
    ansList = []
    threads = []
    for x in range(10):
        t = SudokuGenerator()
        p = threading.Thread(target=t.generate, args=(ansList,))
        threads.append(p)
        p.start()

    while len(ansList) < 9:
        for t in threads:

            # 获取线程状态，若线程已死亡则开辟新进程，直到满足9个数独的条件为止。

            if not t.is_alive():
                threads.remove(t)

                t = SudokuGenerator()
                p = threading.Thread(target=t.generate, args=(ansList,))
                threads.append(p)
                p.start()

    formattedAnswer = []
    result = []

    # 先保存一份答案
    for x in ansList:
        formattedAnswer.append(getFormattedAnswer(x).tolist())

    # 再根据难度从生成好的数独中挖空
    for x in ansList:
        arr = getFormattedAnswer(x)

        if difficulty == "easy":
            removeSlotFromSudoku(arr, slot_count=EASY_SLOT_REMOVE)
        elif difficulty == "normal":
            removeSlotFromSudoku(arr, slot_count=NORMAL_SLOT_REMOVE)
        elif difficulty == "hard":
            removeSlotFromSudoku(arr, slot_count=HARD_SLOT_REMOVE)

        result.append(arr.tolist())

    resultDict = {"sudoku": result, "answer": formattedAnswer}

    return resultDict


'''
基于种子的快速生成服务
'''


def fastGenerateSudokuService(difficulty: str):
    lock = threading.Lock()
    threads = []
    generateResult = []
    result = []

    answer = []

    def threadWork():
        with lock:
            generateResult.append(fastSudokuGenerate())

    for x in range(10):
        t = threading.Thread(target=threadWork)
        threads.append(t)
        t.start()

    for x in threads:
        x.join()

    # 先保存一份答案
    for item in generateResult:
        answer.append(item.tolist())

    # # 再根据难度从生成好的数独中挖空
    for item in generateResult:
        if difficulty == "easy":
            removeSlotFromSudoku(item, slot_count=EASY_SLOT_REMOVE)
        elif difficulty == "normal":
            removeSlotFromSudoku(item, slot_count=NORMAL_SLOT_REMOVE)
        elif difficulty == "hard":
            removeSlotFromSudoku(item, slot_count=HARD_SLOT_REMOVE)

        result.append(item.tolist())

    resultDict = {"sudoku": result, "answer": answer}

    return resultDict
