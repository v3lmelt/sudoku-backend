import unittest

from Modules.FastSudokuGenerateModule import fastSudokuGenerate
from Modules.SudokuGenerateModule import SudokuGenerator
from Service.GetSudokuListService import fastGenerateSudokuService, generateSudokuService

'''
测试相关算法
'''

class SudokuGenerateAlgorithmTest(unittest.TestCase):
    # 面向对象模式的测试
    def test_generateSudokuAlgorithmOO(self):
        worker = SudokuGenerator()
        ansList = []

        while len(ansList) < 1:
            worker.generate(ansList)

        print(ansList)

    # 注意，在调用此测试时需要更改seeds.json的文件路径!
    def test_generateSudokuAlgorithmFast(self):
        print(fastSudokuGenerate())


'''
测试相关服务
'''
class SudokuGenerateServiceTest(unittest.TestCase):


    # 测试能否正常生成数独，普通接口
    def test_generateSudokuService(self):
        generateSudokuService("easy")
        generateSudokuService("normal")
        generateSudokuService("hard")

    # 测试能否正常生成数独，快速接口
    def test_fastGenerateSudokuService(self):
        fastGenerateSudokuService("easy")
        fastGenerateSudokuService("normal")
        fastGenerateSudokuService("hard")
