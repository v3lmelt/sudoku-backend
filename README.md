# Sudoku - Backend
本后端使用FastAPI制作。
## 说明
由于我们在编码过程中使用了Code With Me功能来实现结对编程，而此功能是共享文档制的，因此没有两个人独立的Commit。
## 运行
`clone`之后，首先我们需要安装一些FastAPI的依赖项。
```
pip install "fastapi[all]"
```
安装完毕之后，使用`uvicorn main:app --reload`运行服务器。
请注意，后端将会占用你的`8000`端口，请不要占用此端口。
## 主要的文件结构说明
```
.
├─ Deprecated
│	├─ AIGC_Sudoku_Algorithms // 原先由AI生成的算法
│	└─ SudokuSeedsGeneratorModule.py // 生成种子文件(seeds.json)的模块
├─ Modules
│	├─ FastSudokuGenerateModule.py // 基于种子文件的快速生成数独算法
│	├─ SudokuGenerateAlgorithmModule.py // DanceLinkX算法的实现，参考了知乎文章
│	└─ SudokuGenerateModule.py // 数独生成模块的封装
│	
├─ Service
│	└─GetSudokuListService.py // 服务	
└─ Unittests
 	└─ SudokuGenerateTest.py // 单元测试
```


