import numpy as np
import threading
import json
import random

from Modules.FASTSudokuGenerateModule import fastSudokuGenerate

# 假设你的fastSudokuGenerate函数已经定义好了
# 我们需要一个锁对象来保证线程安全
lock = threading.Lock()

# 我们需要一个列表来存储生成的数独
sudoku_list = []


# 我们定义一个线程类，继承自threading.Thread
class SudokuThread(threading.Thread):
    # 重写构造方法，传入线程名
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    # 重写run方法，调用fastSudokuGenerate函数，并将结果加入到sudoku_list中
    def run(self):
        # 调用锁的acquire方法，获取锁
        lock.acquire()
        # 打印线程开始的信息
        print(f"{self.name} started.")
        # 调用fastSudokuGenerate函数，得到一个数独
        sudoku = fastSudokuGenerate()
        # 将数独加入到sudoku_list中
        sudoku_list.append(sudoku)
        # 打印线程结束的信息
        print(f"{self.name} finished.")
        # 调用锁的release方法，释放锁
        lock.release()


# 我们定义一个函数，用来创建和启动9个线程
def create_and_start_threads():
    # 创建一个空的线程列表
    threads = []
    # 循环9次，创建9个线程对象，并加入到线程列表中
    for i in range(9):
        # 创建一个线程对象，传入线程名
        thread = SudokuThread(f"Thread-{i + 1}")
        # 将线程对象加入到线程列表中
        threads.append(thread)
    # 循环线程列表，启动每个线程
    for thread in threads:
        thread.start()
    # 循环线程列表，等待每个线程结束
    for thread in threads:
        thread.join()
    # 返回线程列表
    return threads


# 我们调用create_and_start_threads函数，得到线程列表
threads = create_and_start_threads()
# 我们打印sudoku_list的长度，应该是9
print(len(sudoku_list))
# 我们打印sudoku_list的内容，应该是9个数独矩阵
print(sudoku_list)