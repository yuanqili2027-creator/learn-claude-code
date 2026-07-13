# VS Code 编辑器 与 Python 基础入门

这一讲把两件事讲透：一个是**写代码的工具**（VS Code），一个是**能运行的编程语言**（Python）。学会它俩，你就能在电脑上真正「动手」了。

## 一、VS Code 是什么

VS Code（全名 Visual Studio Code）是微软出的一款**免费、开源**的代码/文本编辑器。你可以把它理解成一个「加强版的记事本」：

- 和**记事本 / TextEdit** 比：VS Code 会给代码上色（语法高亮）、能开多个文件、内置终端、能装插件，功能强太多。
- 和 **Word** 比：Word 是排版工具，会往文件里塞一堆格式信息；写代码要的是「纯文本」，VS Code 存的就是干干净净的纯文本。
- 和 **PyCharm 这类 IDE** 比：IDE（集成开发环境）是「全家桶」，重、功能全、启动慢；VS Code 是「轻量但强大」，装了插件后照样能干专业开发的活，启动快、上手快，非常适合新手。

一句话：写代码、记 Markdown 笔记、改配置文件、看日志……只要是文本，VS Code 都能干。

## 二、安装 VS Code

两种方式，任选其一：

- **官网下载**：打开 [code.visualstudio.com](https://code.visualstudio.com/)，点 Download，把下载的 App 拖进「应用程序」文件夹即可。
- **命令行安装（推荐会用终端的人）**：

```bash
brew install --cask visual-studio-code
```

首次打开会看到欢迎页（Welcome），可以先关掉，我们直接上手。

## 三、界面导览（小白向）

打开后从左到右、从上到下认几个区域：

1. **资源管理器 / 文件树**（最左边的图标）：显示你打开的文件夹里有哪些文件，点一下就能打开。
2. **编辑区**（中间大块）：真正写字、写代码的地方。
3. **命令面板**：按 `Cmd+Shift+P`，弹出一个搜索框，几乎所有功能都能在这里搜名字执行——记不住快捷键时就靠它。
4. **集成终端**：菜单栏「终端 → 新建终端」，或按 `` Ctrl+` ``，一个内置的命令行直接嵌在窗口下方，不用再切到别的 App。
5. **设置**：`Cmd+,` 打开，改主题、字号等。

## 四、code 命令：让命令行和编辑器联动

装好 App 后，还要装一个 `code` 命令，才能在终端里用它。做法：

1. 按 `Cmd+Shift+P` 打开命令面板；
2. 输入 `shell command`，选择 **Shell Command: Install 'code' command in PATH**；
3. **重启终端**让设置生效。

之后就能这样用：

```bash
code .          # 用 VS Code 打开「当前文件夹」（. 表示当前目录）
code hello.py   # 打开某个具体文件
code --help     # 查看所有用法
```

这就是「命令行 ↔ 编辑器」的联动：你在终端 `cd` 到某个项目文件夹，敲 `code .`，整个文件夹就在编辑器里打开了。不想用命令也行——**直接把文件夹拖进 VS Code 窗口**同样能打开。左上角文件树顶部还有「新建文件 / 新建文件夹」的小按钮，点一下就能建。

## 五、必装扩展（小白向）

扩展就是插件。点左侧那个「四个方块」图标（扩展市场），搜名字后点 Install 即可。新手建议先装这三个：

- **Chinese (Simplified) 中文语言包**：把菜单界面变成中文。
- **Python**（微软官方）：写 Python 时的语法高亮、补全、一键运行。
- **Markdown 相关**：VS Code 自带 Markdown 支持，写笔记很方便。

## 六、Markdown 预览

Markdown 是一种用简单符号写格式的纯文本（`#` 是标题，`-` 是列表）。写好一个 `.md` 文件后：

- 按 `Cmd+K` 松开，再按 `V`：在**右侧并排**打开预览；
- 或点编辑区**右上角的预览小图标**。

左边改字，右边实时看效果，写文档非常爽。

## 七、Python 基础

### Python 是什么

Python 是一门**易学、强大**的编程语言，语法接近自然英语，广泛用于数据分析、人工智能、网站后端、自动化脚本等。它是很多零基础者的第一门语言。

### 系统自带 vs Homebrew 安装

Mac 一般自带一个 python3，但那是「系统在用」的，版本旧、不方便管理。**开发建议自己装一个独立版**：

```bash
brew install python3
python3 --version   # 查看版本，能打印出版本号就说明装好了
```

为什么要独立版？避免动到系统的 Python 把系统搞坏，同时你能自由升级、装库。

### 写第一个程序 hello.py

在 VS Code 里新建文件 `hello.py`，输入：

```python
print("hello world")

for i in range(3):
    print("第", i, "次循环")
```

说明：`print(...)` 是打印到屏幕；`range(3)` 生成 0、1、2 三个数；`for` 会把它们依次取出。注意 `for` 下面那行**前面要有缩进**（4 个空格）——Python 靠缩进区分代码层级，这点很重要。

保存后，在终端运行：

```bash
python3 hello.py
```

你会看到：

```
hello world
第 0 次循环
第 1 次循环
第 2 次循环
```

### 交互式 REPL（即时试验场）

在终端直接输入 `python3` 回车，就进入了交互式环境（叫 REPL，「读取-求值-输出」循环），敲一行立刻出结果，特别适合试语法：

```
>>> 1 + 2
3
>>> print("hi")
hi
>>> exit()
```

输入 `exit()` 回车即可退出，回到普通终端。想写完整程序时，还是用 `.py` 文件更好。

### 一句话认识 pip 和 venv

- **pip**：Python 的「应用商店」，装别人写好的第三方库，比如 `pip3 install requests`。
- **venv**：虚拟环境，给每个项目单独一套库，互不干扰。现在知道有这俩东西就行，用到时再细学。

## 参考资料

- [在 macOS 上安装 VS Code（官方中文文档）](https://vscode.js.cn/docs/setup/mac) — 安装步骤与 `code` 命令的权威说明。
- [VS Code 命令行界面 CLI（官方文档）](https://code.visualstudio.com/docs/editor/command-line) — `code .`、`code --help` 等命令用法。
- [VSCode 集成终端（菜鸟教程）](https://www.runoob.com/vscode/vscode-terminal.html) — 内置终端的中文图文讲解。
- [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/index.html) — 最权威的入门材料，含 print、循环、REPL。
- [廖雪峰 Python 教程](https://liaoxuefeng.com/books/python/basic/index.html) — 面向小白的中文入门，for/while 循环讲得清楚。
- [菜鸟教程 Python3](https://www.runoob.com/python3/python3-tutorial.html) — 含 pip、venv 虚拟环境等专题，可随查随用。
