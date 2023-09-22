import random
import unittest

import numpy as np
from DanceLinkAlgorithm import initCol, appendRow, dance_link

'''
生成数独部分
'''


class SudokuGenerator:
    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.sudoku = np.zeros((9, 9), dtype=int)
        self.counter = 0

    def generate(self, slot_to_remove):
        loc_dic = self.__initLocationDict(17)
        head = self.__getSudokuLinkList(loc_dic)
        ans = []
        dance_link(head, ans)
        if len(ans):
            arr = self.__getFormattedAnswer(ans)
            self.__removeSlotFromSudoku(arr, slot_to_remove)
            print(arr)
        else:
            print("no result")

    # 初始化词典，将限制条件转化为行列关系，并根据限制条件摆放指定数量的初值

    def __initLocationDict(self, init_count):
        dic = {}
        s = set()
        while len(dic) < init_count:

            i = random.randint(0, 8)
            j = random.randint(0, 8)
            k = random.randint(1, 9)

            a = i * 9 + j

            if a in s:
                continue
            b = i * 9 + k + 80
            if b in s:
                continue
            c = j * 9 + k + 161
            if c in s:
                continue
            d = (i // 3 * 3 + j // 3) * 9 + k + 242
            if d in s:
                continue

            s.add(a)
            s.add(b)
            s.add(c)
            s.add(d)

            dic[(i, j)] = k

        return dic

    # 根据词典生成十字交叉链表

    def __getSudokuLinkList(self, loc_dic):
        # 初始化头结点和列节点
        head = initCol(324)

        for i in range(9):
            for j in range(9):
                if (i, j) in loc_dic:
                    k = loc_dic[(i, j)]
                    a = i * 9 + j
                    b = i * 9 + k + 80
                    c = j * 9 + k + 161
                    d = (i // 3 * 3 + j // 3) * 9 + k + 242
                    row_id = (i * 9 + j) * 9 + k - 1
                    appendRow(head, row_id, [a, b, c, d])
                else:
                    for k in range(1, 10):
                        a = i * 9 + j
                        b = i * 9 + k + 80
                        c = j * 9 + k + 161
                        d = (i // 3 * 3 + j // 3) * 9 + k + 242
                        row_id = (i * 9 + j) * 9 + k - 1
                        appendRow(head, row_id, [a, b, c, d])
        return head

    # 获取格式化的答案
    def __getFormattedAnswer(self, ans):
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

    def __removeSlotFromSudoku(self, sudoku, slot_count):
        counter = 0
        while counter < slot_count:
            row = np.random.randint(0, 9)
            col = np.random.randint(0, 9)
            if sudoku[row, col] != 0:
                sudoku[row, col] = 0
                counter += 1


class test_SudokuGenerator(unittest.TestCase):
    def test_Generator(self):
        p = SudokuGenerator()
        p.generate(slot_to_remove=10)