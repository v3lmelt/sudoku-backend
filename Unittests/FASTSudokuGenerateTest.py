import unittest

from Modules.FASTSudokuGenerateModule import fastSudokuGenerate


class FASTSudokuGenerateTest(unittest.TestCase):
    def test_FASTGenerate(self):
        fastSudokuGenerate()


if __name__ == '__main__':
    unittest.main()
