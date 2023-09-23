import unittest
import numpy as np


class SudokuGenerator:
    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sudoku = np.zeros((9, 9), dtype=int)
        self.counter = 0
        self.recursionCounter = 0
        self.correct = False
        self.solved = False

    # Generate a random sudoku board
    def generate(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.sudoku = np.zeros((9, 9), dtype=int)
        self.counter = 0
        self.recursionCounter = 0
        self.correct = False
        self.solved = False
        self.fillDiagonal()
        self.fillRemaining(0, 3)
        self.removeDigits()
        return self.sudoku

    # Generate diagonal boxes

    def fillDiagonal(self):
        for i in range(0, 9, 3):
            self.fillBox(i, i)

    # Generate boxes

    def fillBox(self, row, col):

        # Generate numbers for each box
        for i in range(3):
            for j in range(3):

                # Generate random number
                while True:
                    num = self.numbers[np.random.randint(0, 9)]
                    if self.isSafe(row, col, num):
                        break

                # Add number to board
                self.board[row + i][col + j] = num
                self.counter += 1

    def isSafe(self, row, col, num):
        return not self.usedInRow(row, num) and not self.usedInCol(col, num) and not self.usedInBox(row - row % 3,
                                                                                                    col - col % 3, num)

    def usedInRow(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return True
        return False

    def usedInCol(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return True
        return False

    def usedInBox(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == num:
                    return True
        return False

    def fillRemaining(self, i, j):

        # Check if we have reached the end of the board

        if j >= 9 and i < 8:
            i += 1
            j = 0
        if i >= 9 and j >= 9:
            return True

        # Check if we have reached the end of a box

        if i < 3:
            if j < 3:
                j = 3
        elif i < 6:
            if j == int(i / 3) * 3:
                j += 3
        else:
            if j == 6:
                i += 1
                j = 0
                if i >= 9:
                    return True

        # Generate numbers for each box

        for num in range(1, 10):

            # Check if number is safe to add

            if self.isSafe(i, j, num):
                self.board[i][j] = num

                # Check if we can fill the rest with the board
                if self.fillRemaining(i, j + 1):
                    return True
                self.board[i][j] = 0
        return False

    # Remove digits from the board
    def removeDigits(self):

        # Remove digits until we have reached the desired difficulty

        while self.counter > 0:
            row = np.random.randint(0, 9)
            col = np.random.randint(0, 9)
            if self.board[row][col] != 0:
                self.counter -= 1
                self.board[row][col] = 0
                self.recursionCounter = 0
                self.solve()
                if self.recursionCounter != 1:
                    self.board[row][col] = self.sudoku[row][col]
                    self.counter += 1

    def solve(self):

        self.recursionCounter += 1

        # Check if we have reached the end of the board
        for i in range(9):
            for j in range(9):

                # Check if we have reached an empty cell
                if self.sudoku[i][j] == 0:

                    # Generate numbers for each cell
                    for num in range(1, 10):
                        if self.isSafe(i, j, num):
                            self.sudoku[i][j] = num

                            # Check if we can solve the rest of the board
                            if self.solve():
                                return True
                            self.sudoku[i][j] = 0
                    return False
        return True

    def printBoard(self):
        print(self.board)


'''

Tests

'''




class MyTestCase(unittest.TestCase):
    def test_generator(self):
        p = SudokuGenerator()
        p.generate()

        self.assertEqual(p.printBoard(), "")


if __name__ == '__main__':
    unittest.main()
