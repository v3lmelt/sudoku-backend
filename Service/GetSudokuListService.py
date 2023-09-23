import threading
import unittest

from fastapi.encoders import jsonable_encoder

from Modules.SudokuGenerateModule import SudokuGenerator, getFormattedAnswer


# 多线程生成数独
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

    formattedResult = []

    for x in ansList:
        p = SudokuGenerator()
        formattedResult.append(getFormattedAnswer(x).tolist())

    # print(formattedResult)
    return formattedResult


class testGetSudokuService(unittest.TestCase):
    def test_GetSudokuService(self):
        generateSudokuService()
