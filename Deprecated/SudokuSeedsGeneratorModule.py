import json
import threading

from Modules.SudokuGenerateModule import SudokuGenerator, getFormattedAnswer


def generateSudokuSeed():
    ansList = []
    threads = []
    for x in range(16):
        t = SudokuGenerator()
        p = threading.Thread(target=t.generate, args=(ansList,))
        threads.append(p)
        p.start()

    while len(ansList) < 1000:
        print(f"Current progress: {len(ansList)} / 1000\n")
        for t in threads:

            # 获取线程状态，若线程已死亡则开辟新进程，直到满足9个数独的条件为止。

            if not t.is_alive():
                threads.remove(t)

                t = SudokuGenerator()
                p = threading.Thread(target=t.generate, args=(ansList,))
                threads.append(p)
                p.start()

    dictToWrite = {}
    counter = 0
    for item in ansList:
        dictToWrite[counter] = getFormattedAnswer(item).tolist()
        counter += 1

    with open("seeds.json", "w") as fd:
        fd.write(json.dumps(dictToWrite, indent=4))


if __name__ == '__main__':
    generateSudokuSeed()
