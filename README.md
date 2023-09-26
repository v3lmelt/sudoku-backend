# Sudoku - Backend
本后端使用FastAPI制作。

## 构建并运行
`clone`之后，首先我们需要安装一些FastAPI的依赖项。
```
pip install "fastapi[all]"
```
安装完毕之后，使用`uvicorn main:app --reload`运行服务器。

请注意，后端将会占用你的`8000`端口，请不要占用此端口。

## 主要的文件结构说明
```
/sudoku-backend
|-/AIGC-Sudoku_Algorithms // @DEPRECATED! 这个文件夹原先装的是AI生成的算法，但是并没有在实际工程中采用，已废弃。
|-/Modules // 后端的核心模块
|-/Modules/FastSudokuGenerateModule.py // 基于种子的快速生成算法的实现
|-/Modules/SudokuGenerateAlgorithmModule.py // 舞蹈链 (DanceLinkX) 算法的实现
|-/Modules/SudokuGenerateModule.py // 数独生成算法的核心部分
|-/Modules/SudokuSeedsGeneratorModule.py // @DEPRECATED! 生成给算法提供初值信息的数独的模块，已废弃。
|-/Service // 服务层
|-/Service/GetSudokuListService.py // 提供给前端的两个接口均在这个文件中
|-main.py // FastAPI服务器的入口


```
