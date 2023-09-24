import threading
import unittest
from concurrent.futures import ThreadPoolExecutor

from fastapi.encoders import jsonable_encoder

from Modules.FASTSudokuGenerateModule import fastSudokuGenerate
from Modules.SudokuGenerateModule import SudokuGenerator, getFormattedAnswer

'''
原始的基于Dance Link X的数独生成服务
'''
def generateSudokuService():
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

    resultDict = {}
    formattedAnswer = []

    counter = 0
    for x in ansList:
        formattedAnswer.append(getFormattedAnswer(x).tolist())

    resultDict["sudoku"] = formattedAnswer

    return resultDict


'''
基于种子的快速生成服务
'''


def fastGenerateSudokuService():
    lock = threading.Lock()
    threads = []
    result = []

    def threadWork():
        with lock:
            result.append(fastSudokuGenerate().tolist())

    for x in range(10):
        t = threading.Thread(target=threadWork)
        threads.append(t)
        t.start()

    for x in threads:
        x.join()
    resultDict = {"sudoku": result}

    return resultDict
