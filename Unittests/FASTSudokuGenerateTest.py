import unittest

from Modules.FASTSudokuGenerateModule import fastSudokuGenerate
from Service.GetSudokuListService import fastGenerateSudokuService


class FASTSudokuGenerateTest(unittest.TestCase):
    def test_FASTGenerate(self):
        fastSudokuGenerate()

    def test_fastGenerateSudokuService(self):
        fastGenerateSudokuService()


if __name__ == '__main__':
    unittest.main()
