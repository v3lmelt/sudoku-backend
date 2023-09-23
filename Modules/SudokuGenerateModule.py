import random
import threading

import numpy as np
from func_timeout import func_timeout, FunctionTimedOut

from Modules.SudokuGenerateAlgorithmModule import initCol, appendRow, dance_link

'''
生成数独部分
'''
syncLock = threading.Lock()


# 获取格式化后的解
def getFormattedAnswer(ans):
    ans.sort()
    arr = np.empty((9, 9), dtype=np.int32)
    for row_id in ans:
        loc = row_id // 9
        i = loc // 9
        j = loc % 9
        k = row_id % 9 + 1
        arr[i, j] = k
    return arr


# 从数独中挖空，生成数独谜题
def removeSlotFromSudoku(sudoku, slot_count):
    counter = 0
    while counter < slot_count:
        row = np.random.randint(0, 9)
        col = np.random.randint(0, 9)
        if sudoku[row, col] != 0:
            sudoku[row, col] = 0
            counter += 1


def getSudokuLinkList(dict):
    head = initCol(324)
    for x in range(9):
        for y in range(9):
            if (x, y) in dict:
                appendRow(head, getRowIDByCoord(x, y, dict[(x, y)]),
                          getColListByCoord(x, y, dict[(x, y)]))
            else:
                for i in range(0, 10):
                    appendRow(head, getRowIDByCoord(x, y, i), getColListByCoord(x, y, i))

    return head


# 约束a, 某个格子(x,y)是否存在数字
def numberExistInCellToColID(x, y, num):
    return x * 9 + y


# 约束b, 第x行是否存在数字[1,2,3,...,9]
def numberExistInRowToColID(x, num):
    return x * 9 + num + 80


# 约束c, 第y列是否存在数字[1,2,3,...,9]
def numberExistInColToColID(y, num):
    return y * 9 + num + 161


# 约束d, 九宫格i是否存在数字[1,2,3,4,...9]
def numberExistInGridToColID(x, y, num):
    return (x // 3 * 3 + y // 3) * 9 + num + 242


# 通过x, y, num获得约束条件对应的列ID
def getColListByCoord(x, y, num):
    return [numberExistInCellToColID(x, y, num), numberExistInRowToColID(x, num),
            numberExistInColToColID(y, num), numberExistInGridToColID(x, y, num)]


def getRowIDByCoord(x, y, num):
    return (x * 9 + y) * 9 + num - 1


'''
Class SudokuGenerator:
    封装数独的一些过程，封装成类方便生成方法进行一些操作。
    上方也提供了解耦后的函数，方便其他模块的设计。
'''
class SudokuGenerator:
    def __init__(self):
        self.counter = 0

    def generate(self, ansList: list):
        loc_dic = self.__initLocationDict(17)
        head = self.__getSudokuLinkList(loc_dic)
        ans = []
        try:
            func_timeout(0.1, dance_link, args=(head, ans))
        except FunctionTimedOut:
            pass
        else:
            if len(ans):
                with syncLock:
                    ansList.append(ans)

    '''
    建立约束条件与格子, 行, 列, 宫格的关系
    '''

    # 约束a, 某个格子(x,y)是否存在数字
    def __numberExistInCellToColID(self, x, y, num):
        return x * 9 + y

    # 约束b, 第x行是否存在数字[1,2,3,...,9]
    def __numberExistInRowToColID(self, x, num):
        return x * 9 + num + 80

    # 约束c, 第y列是否存在数字[1,2,3,...,9]
    def __numberExistInColToColID(self, y, num):
        return y * 9 + num + 161

    # 约束d, 九宫格i是否存在数字[1,2,3,4,...9]
    def __numberExistInGridToColID(self, x, y, num):
        return (x // 3 * 3 + y // 3) * 9 + num + 242

    # 生成数独内的初值，并将其映射为行的关系

    def __initLocationDict(self, init_count: int):
        if init_count < 11:
            init_count = 11

        # 存放初值使用的词典, 键为(x,y)的二元组, 值为[1,2,3,...,9]的数字
        dict = {}

        # 存放已经使用的行ID
        usedColID = set()

        # 尝试往数独中添加init_count个初值，并且保证每个初值所在的行ID不重复
        while len(dict) < init_count:

            x = random.randint(0, 8)
            y = random.randint(0, 8)
            k = random.randint(1, 9)

            # 约束a, 某个格子(x,y)是否存在数字
            if self.__numberExistInCellToColID(x, y, k) in usedColID:
                continue
            # 约束b, 某行是否存在数字
            if self.__numberExistInRowToColID(x, k) in usedColID:
                continue
            # 约束c, 某列是否存在数字
            if self.__numberExistInColToColID(y, k) in usedColID:
                continue
            # 约束d, 某个九宫格是否存在数字
            if self.__numberExistInGridToColID(x, y, k) in usedColID:
                continue

            # 否则将此数字添加至约束条件的列中
            for item in self.__getColListByCoord(x, y, k):
                usedColID.add(item)

            # 将此初值添加至词典中
            dict[(x, y)] = k
        return dict

    # 通过x, y, num获得约束条件对应的列ID
    def __getColListByCoord(self, x, y, num):
        return [self.__numberExistInCellToColID(x, y, num), self.__numberExistInRowToColID(x, num),
                self.__numberExistInColToColID(y, num), self.__numberExistInGridToColID(x, y, num)]

    def __getRowIDByCoord(self, x, y, num):
        return (x * 9 + y) * 9 + num - 1

    # 根据词典生成十字交叉链表

    def __getSudokuLinkList(self, dict):
        head = initCol(324)
        for x in range(9):
            for y in range(9):
                if (x, y) in dict:
                    appendRow(head, self.__getRowIDByCoord(x, y, dict[(x, y)]),
                              self.__getColListByCoord(x, y, dict[(x, y)]))
                else:
                    for i in range(0, 10):
                        appendRow(head, self.__getRowIDByCoord(x, y, i), self.__getColListByCoord(x, y, i))

        return head
