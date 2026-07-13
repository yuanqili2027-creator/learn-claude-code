# LaTeX 专业排版与 Overleaf

## 一、LaTeX 是什么

LaTeX 是一套专业的**排版系统**（typesetting system），专门用来生成印刷级质量的文档——学术论文、数学书籍、简历、幻灯片都能做。它不是一款「软件」那么简单，而是一门用纯文本描述文档的「语言」加上一套负责把文本变成精美 PDF 的引擎。

**读音**：读作 "lay-tech" 或 "lah-tech"。结尾的 "tech" 来自希腊词根 τέχνη（technē，也是 technology 的来源），发的是「科技」的 tech 音，**不读成 "lay-tecks"**（不是复数 techs）。

**和 TeX 的关系**：底层引擎叫 TeX，由高德纳（Donald Knuth）在 1978 年为排版自己的书而创造。TeX 功能强大但命令繁琐。1980 年代 Leslie Lamport 在 TeX 之上封装了一套更好用的高层命令，取名 LaTeX（La 来自 Lamport）。你平时写的就是 LaTeX，它最终仍由 TeX 引擎编译。

**主要用途**：数学/物理/计算机等理工科的学术论文、含大量公式的教材与专著、格式规范的简历/CV、会议幻灯片（Beamer）。凡是对公式、排版一致性、参考文献要求高的场景，LaTeX 都是首选。

## 二、「内容与排版分离」vs Word「所见即所得」

Word 是 **WYSIWYG**（所见即所得，What You See Is What You Get）：你一边敲字一边手动调字号、加粗、行距，屏幕上长什么样，打印出来就是什么样。好处是直观，坏处是你被迫时刻分心去管样式，且长文档里格式极易前后不一致。

LaTeX 是**标记式（markup）**思路：你只负责写**内容**并用命令标注它的**语义**——「这是一个章节标题」「这是一段引用」「这是一个公式」——具体怎么排版（标题多大、目录怎么生成、公式怎么居中编号）交给 LaTeX 自动完成。

学术界偏爱 LaTeX 的三大原因：

- **数学公式**：复杂公式的排版能力无出其右，源码即所写即所得的数学语义。
- **参考文献**：配合 BibTeX/BibLaTeX，引用和文献列表自动生成、自动编号、自动按期刊格式调整。
- **排版一致性**：全文标题、字体、间距由文档类统一控制，几百页也不会跑偏；换个期刊模板，内容一字不改就能换装。

## 三、最小可运行文档结构

一份 LaTeX 文件分两大块：**导言区（preamble）** 和**正文（document 环境）**。

```latex
\documentclass{article}      % 文档类：article/report/book/beamer
\usepackage{amsmath}         % 导言区：加载宏包，做全局设置
\title{我的第一篇文档}
\author{张三}
\date{\today}                % \today 自动填今天日期
\begin{document}             % 正文开始
\maketitle                   % 根据上面的 title/author/date 生成标题块
Hello, \LaTeX!
\end{document}               % 正文结束
```

逐条说明：

- `\documentclass{article}`：**必需的第一行**，声明文档类型。`article`（短文/论文）、`report`（含章 chapter 的报告）、`book`（书籍）、`beamer`（幻灯片）。可带参数，如 `\documentclass[12pt,a4paper]{article}`。
- **导言区**：从 `\documentclass` 到 `\begin{document}` 之间的部分，用来 `\usepackage{}` 加载功能宏包、定义全局设置。例如 `\usepackage{amsmath}` 加载数学增强包，`\usepackage{graphicx}` 用于插图。
- `\title{} \author{} \date{}`：登记标题、作者、日期这三项元信息（只是登记，还没显示）。
- `\begin{document} ... \end{document}`：正文只能写在这对命令之间，之外的内容不会出现在 PDF 里。
- `\maketitle`：把前面登记的 title/author/date 真正排版成标题块。

> 中文提示：要排版中文，把文档类换成 `ctexart`（或加 `\usepackage{ctex}`），并用 **XeLaTeX** 编译。在 Overleaf 里可在菜单 Menu → Compiler 选 XeLaTeX。

## 四、常用命令

**章节与目录**

```latex
\section{引言}          % 一级标题（自动编号）
\subsection{研究背景}   % 二级标题
\tableofcontents        % 自动生成目录（放在正文开头）
\newpage                % 强制换页
```

**文字格式**

```latex
\textbf{加粗}   \textit{斜体}   \texttt{等宽字体（代码风格）}
段末空一行 = 新段落；行内强制换行用 \\
```

**列表**

```latex
\begin{itemize}          % 无序列表（圆点）
  \item 第一点
  \item 第二点
\end{itemize}

\begin{enumerate}        % 有序列表（自动编号 1. 2. 3.）
  \item 第一步
  \item 第二步
\end{enumerate}
```

**需要转义的特殊字符**：这十个字符在 LaTeX 里有特殊含义，直接打会出错或效果异常，要在前面加反斜杠：

```latex
\#  \$  \%  \&  \_  \{  \}   % 这七个直接反斜杠转义
\textasciitilde  \textasciicircum  \textbackslash   % ~ ^ \ 需用命令
```

比如你想在正文里打个井号 `#`，必须写成 `\#`，否则报错。

## 五、数学公式

数学要写在**数学模式**里，模式内空格被忽略、字符自动获得恰当间距。

- **行内公式**：用一对 `$` 包住，与文字同行。如 `质能方程 $E=mc^2$ 揭示……`
- **行间公式**：用 `\[ ... \]` 单独成行居中；要**带编号**用 `equation` 环境。
- **上标 `^`、下标 `_`**：多于一个字符时用花括号包起来，如 `x^{2n}`、`a_{ij}`。

常见符号：`\frac{分子}{分母}` 分式、`\sum` 求和、`\int` 积分、`\sqrt{}` 根号、希腊字母 `\alpha \beta \pi \theta`、`\infty` 无穷。

完整例子一（行内 + 分式 + 希腊字母）：

```latex
圆的面积为 $S = \pi r^2$，其中 $r$ 为半径，比值 $\frac{S}{r^2}=\pi$。
```

完整例子二（带编号的行间公式，求和与积分）：

```latex
\[
  \sum_{i=1}^{n} i = \frac{n(n+1)}{2}
\]

\begin{equation}
  \int_{0}^{1} x^2 \, \mathrm{d}x = \frac{1}{3}
\end{equation}
```

## 六、Overleaf 上手

**Overleaf** 是一个**在线 LaTeX 编辑器**，网址 [https://www.overleaf.com](https://www.overleaf.com)。强烈推荐新手先用它，原因：

- **免安装**：本地装完整 TeX 发行版（如 TeX Live/MacTeX）要 4–7 GB 甚至十几 GB，还要配环境；Overleaf 浏览器打开即用。
- **实时预览**：左边写源码，右边看 PDF。
- **协作**：像 Google Docs 一样多人同时编辑，适合论文合作。

操作步骤：

1. 注册登录 → 点 **New Project**（新建项目）。
2. 选 **Blank Project**（空白）或 **Example Project**，也可从模板库选。
3. 界面分两栏：**左边编辑区**写 LaTeX 源码，**右边 PDF 区**显示排版结果。
4. 改完点绿色的 **Recompile**（重新编译）按钮，几秒后右侧刷新出新 PDF。
5. 编译失败时，看报错日志里的行号，通常是漏了 `}`、拼错命令或忘了转义特殊字符。

## 七、用模板做简历

简历特别适合用 LaTeX：排版整齐、留白讲究、导出 PDF 到哪都不变形。做法是「照着模板替换」而非从零写：

1. 打开 Overleaf 模板库 [https://www.overleaf.com/latex/templates](https://www.overleaf.com/latex/templates)，搜索 **CV** 或 **Resume**。
2. 挑一个喜欢的（如经典的 *Awesome-CV*、*Deedy Resume*），点 **Open as Template** 复制到自己账户。
3. 在源码里找到姓名、邮箱、教育经历、工作经历等字段，把里面的示例文字**逐段换成你自己的信息**，结构命令不用动。
4. 点 Recompile，右侧就是你的简历 PDF，直接下载。

不懂每条命令没关系——模板已经把排版调好，你只填内容。

## 八、现代用法：让 AI 生成 LaTeX

你甚至不必手写命令。可以让 AI（如 Claude、Claude Code）直接生成 LaTeX 源码：描述你要的文档——「帮我写一份含公式的实验报告」「生成一份软件工程师简历的 LaTeX 代码」——AI 输出源码，你粘进 Overleaf 点 Recompile 即得 PDF。需要 Word 版时，再用 Pandoc（`pandoc report.tex -o report.docx`）转换。这样你专注内容，格式和命令都交给 AI 与编译器。

## 常用命令速查表

| 命令 | 作用 |
|------|------|
| `\documentclass{article}` | 声明文档类型（必需，第一行） |
| `\usepackage{amsmath}` | 导言区加载宏包 |
| `\begin{document}...\end{document}` | 正文区 |
| `\title{} \author{} \date{}` `\maketitle` | 登记并生成标题块 |
| `\section{} \subsection{}` | 章节标题（自动编号） |
| `\tableofcontents` | 自动生成目录 |
| `\newpage` | 强制换页 |
| `\textbf{} \textit{} \texttt{}` | 加粗 / 斜体 / 等宽 |
| `\\` | 行内强制换行 |
| `itemize / enumerate` | 无序 / 有序列表 |
| `$...$` / `\[...\]` | 行内 / 行间公式 |
| `^  _` | 上标 / 下标 |
| `\frac \sum \int \sqrt` | 分式 / 求和 / 积分 / 根号 |
| `\#  \$  \%  \&  \_  \{  \}` | 转义特殊字符 |

## 参考资料

- [Overleaf 官网](https://www.overleaf.com) —— 在线 LaTeX 编辑器主页，免安装、可协作，新手首选。
- [Learn LaTeX in 30 minutes（Overleaf）](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) —— Overleaf 官方 30 分钟入门教程，零基础，几乎每个示例都能一键在 Overleaf 打开编辑。
- [Overleaf Learn 文档中心](https://www.overleaf.com/learn) —— 官方知识库，涵盖数学公式、参考文献、图表、模板等各主题的权威说明。
- [Overleaf 模板库](https://www.overleaf.com/latex/templates) —— 海量现成模板，含大量 CV/Resume、论文、幻灯片模板，可「照着替换」。
- [LaTeX 入门 —— OI Wiki](https://oi-wiki.org/tools/latex/) —— 对中文用户友好的入门教程，讲清引擎、宏包、中文支持与数学符号。
- [LaTeX 公式手册（博客园）](https://www.cnblogs.com/1024th/p/11623258.html) —— 号称「全网最全」的数学符号命令速查，写公式时随手对照。
- [LaTeX video tutorial for beginners（Overleaf 视频）](https://www.overleaf.com/learn/latex/LaTeX_video_tutorial_for_beginners_(video_1)) —— 官方新手视频系列，跟着从零建文档。
