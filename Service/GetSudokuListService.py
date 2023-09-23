import threading
from Modules.SudokuGenerateModule import SudokuGenerator
def test_multiThreadSudoku(self):
    ansList = []
    threads = []
    for x in range(10):
        t = SudokuGenerator()
        p = threading.Thread(target=t.generate, args=(ansList,))
        threads.append(p)
        p.start()

    while len(ansList) < 9:
        for t in threads:
            if not t.is_alive():
                threads.remove(t)

                t = SudokuGenerator()
                p = threading.Thread(target=t.generate, args=(ansList,))
                threads.append(p)
                p.start()

    print(ansList)

    for x in ansList:
        p = SudokuGenerator()
        print(p.getFormattedAnswer(x))
    return ansList