# Sudoku - Backend
本后端使用FastAPI制作。
## 说明
由于我们在编码过程中使用了Code With Me功能来实现结对编程，而此功能是共享文档制的，因此没有两个人独立的Commit。
## 运行
`clone`之后，首先我们需要配置FastAPI。

`pip install "fastapi[all]"`

若遇到安装错误的情况，请尝试以下带有镜像源的指令:

`pip install "fastapi[all]" -i https://pypi.tuna.tsinghua.edu.cn/simple`

安装完毕之后，使用 `uvicorn main:app --reload` 运行服务器。
请注意，后端将会占用你的`8000`端口，请不要占用此端口。

若遇到`8000`端口占用的情况，你也可以使用以下指令自定义端口，但请注意一旦后端修改了端口，前端也必须在配置文件中修改。
`uvicorn main:app --host 0.0.0.0 --port [端口号] --reload`

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


