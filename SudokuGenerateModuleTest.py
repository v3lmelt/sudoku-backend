import unittest
import threading
from SudokuGenerateModule import *


class MyTestCase(unittest.TestCase):

    def test_multithreadTimeElapsed(self):
        # sync_lock = threading.Lock()
        answer_arr = []

        def multithreadGenerateSudoku():
            while len(answer_arr) < 9:
                ans = []
                loc_dic = initLocationDict(17)
                head = getSudokuLinkList(loc_dic)
                dance_link(head, ans)
                # sync_lock.acquire(True)
                if len(ans):
                    arr = getFormattedAnswer(ans)
                    print(arr)
                    answer_arr.append(arr)
                else:
                    print("no result")
                # sync_lock.release()

        for i in range(9):
            t = threading.Thread(target=multithreadGenerateSudoku)
            t.start()

    def test_singleThreadTimeElapsed(self):
        for i in range(9):
            ans = []
            loc_dic = initLocationDict(11)
            head = getSudokuLinkList(loc_dic)
            dance_link(head, ans)
            if len(ans):
                arr = getFormattedAnswer(ans)
                print(arr)
            else:
                print("no result")


if __name__ == '__main__':
    unittest.main()
