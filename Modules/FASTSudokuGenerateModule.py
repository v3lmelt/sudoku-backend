"""
基于种子的数独快速生成实现
"""
import json
import random

import numpy as np

from Modules.SudokuGenerateAlgorithmModule import dance_link
from Modules.SudokuGenerateModule import getSudokuLinkList, getFormattedAnswer

SEED_FILE = "../seeds.json"


def fastSudokuGenerate():
    locationDict = {}
    with open(SEED_FILE, "r") as fd:

        seedList = json.loads(fd.read())

    # print(seedList)
    # 生成一个随机选择的数独ID
    randomSelectID = random.randint(0, len(seedList) - 1)

    # 从中读取一个数独，注意索引应当是一个字符串
    sudoku = np.array(seedList[str(randomSelectID)])

    # 选取至少30-40个数字加入locationDict中
    counter = 0
    initValueCount = random.randint(30, 35)
    while counter < initValueCount:
        randX = random.randint(0, 8)
        randY = random.randint(0, 8)

        if (randX, randY) not in locationDict:
            locationDict[(randX, randY)] = sudoku[randX][randY]
            counter += 1
        else:
            continue

    # 一旦有了初值信息就可以尝试生成数独了
    head = getSudokuLinkList(locationDict)
    ans = []

    dance_link(head, ans)

    print("生成的数独\n")
    print(getFormattedAnswer(ans))

    print("原始数独\n")
    print(sudoku)

    print("是否一致?\n")
    print(sudoku == getFormattedAnswer(ans))
