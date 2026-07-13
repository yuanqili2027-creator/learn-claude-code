# 命令行核心命令与操作：从零学会用「敲字」指挥电脑

平时你用鼠标点图标、拖文件；命令行（Terminal / 终端）则是用**打字**来指挥电脑。它看起来像「黑客界面」，其实原理很简单：你敲一行字、按回车，电脑就执行一个动作。学会它，你能更快、更精确地操作文件，也是学编程绕不开的第一步。

---

## 一、先建立心智模型

打开终端（Mac 上按 `Command + 空格`，输入「终端」或「Terminal」回车），你会看到一行结尾是 `$` 或 `%` 的文字，这叫**提示符**，意思是「我准备好了，请下命令」。

**当前工作目录**是核心概念：终端任何时候都「站」在某个文件夹里，你不写完整路径时，命令默认就对这个文件夹生效。就像你在文件管理器里打开了某个窗口，操作的就是这个窗口里的东西。

一条命令通常由三部分组成：

```
命令   选项(flag)   参数
ls     -l          Desktop
（做什么）（怎么做）  （对谁做）
```

选项前面的横杠 `-` 就是「flag（标志）」，用来微调命令行为，比如 `-l` 让 `ls` 显示详细信息。**注意：命令区分大小写，各部分之间用空格隔开。**

---

## 二、逐个讲透核心命令

### pwd —— 我现在在哪
- **全称**：print working directory（打印工作目录）
- **作用**：显示当前所在文件夹的完整路径
- **例子**：`pwd`
- **输出**：`/Users/xiaoming/Desktop` —— 你正站在小明桌面这个文件夹里。迷路时先敲它。

### ls —— 看看这里有什么
- **全称**：list（列出）
- **作用**：列出当前目录里的文件和文件夹
- **常用组合**：
  - `ls` 简单列出可见文件
  - `ls -a` 连隐藏文件也显示（以 `.` 开头的文件默认藏起来）
  - `ls -l` 长格式，一行一个，显示详细信息
  - `ls -lh` 在 `-l` 基础上把大小显示成人类易读的 `4.0K`、`2.3M`（h = human）
- **怎么读 `ls -l` 的每一列**（示例一行）：

```
-rw-r--r--  1  xiaoming  staff  1024  7 11 09:30  note.txt
   ①        ②     ③       ④     ⑤       ⑥          ⑦
```

  - ① 权限：第一个字符 `-` 是文件、`d` 是文件夹；后面九个字符表示读(r)/写(w)/执行(x)权限
  - ② 链接数（新手可忽略）
  - ③ 所有者：谁的文件
  - ④ 所属组
  - ⑤ 大小（字节，配 `-h` 更好读）
  - ⑥ 最后修改日期时间
  - ⑦ 文件名

### cd —— 进出文件夹
- **全称**：change directory（切换目录）
- **作用**：走进/走出文件夹
- **用法大全**：
  - `cd Desktop` 进入当前目录下的 Desktop 文件夹
  - `cd ..` 返回上一级
  - `cd ~` 或直接 `cd` 回到用户主目录（你的「家」）
  - `cd /` 去往根目录（整块硬盘的最顶层）
  - `cd -` 回到上一次待的目录（在两个目录间来回跳很方便）

### mkdir —— 新建文件夹
- **全称**：make directory
- **作用**：创建新文件夹
- **例子**：`mkdir photos` 建一个 photos 文件夹；`mkdir a b c` 一次建三个
- **进阶 `-p`**：`mkdir -p work/2026/jan` 一次性创建多层嵌套文件夹，父文件夹不存在也会自动补齐，不报错。

### rm —— 删除（⚠️ 最危险的命令）
- **全称**：remove
- **作用**：删除文件或文件夹
- **例子**：
  - `rm note.txt` 删一个文件
  - `rm -r photos` 删一个文件夹及里面所有东西（r = recursive 递归）
  - `rm -rf photos` 强制删除、不询问（f = force）
- **⚠️ 核心警告**：命令行的 `rm`**没有回收站/废纸篓，删了就是永久消失，无法恢复**。更安全的做法：删前先用 `ls` 确认路径，或加 `-i` 让它每删一个都问你一次：`rm -i note.txt`。

### open —— 用默认软件打开
- **作用**：像双击一样，用系统默认程序打开文件/文件夹（macOS 专属）
- **例子**：`open note.txt`（用文本编辑器打开）、`open .`（在访达里打开当前文件夹）

### 小白必备的几个补充命令

| 命令 | 作用 | 例子 |
|------|------|------|
| `cat` | 直接在终端里显示文件内容 | `cat note.txt` |
| `cp` | 复制文件（复制文件夹要加 `-r`） | `cp a.txt b.txt` / `cp -r dir1 dir2` |
| `mv` | 移动文件，或重命名（Linux/Mac 没有单独的改名命令） | `mv old.txt new.txt`（改名）/ `mv a.txt ~/Desktop/`（移动） |
| `touch` | 新建一个空文件 | `touch note.txt` |
| `man` | 查看某命令的说明书（manual），按 `q` 退出 | `man ls` |
| `clear` | 清屏（等同 `Ctrl+L`） | `clear` |

---

## 三、路径：绝对 vs 相对

- **绝对路径**：从根目录 `/` 写起的完整地址，无论你在哪敲都指向同一处，如 `/Users/xiaoming/Desktop/note.txt`。
- **相对路径**：相对「当前所在位置」来写，如你已在 Desktop 里，直接写 `note.txt` 即可。

四个特殊符号务必记牢：

| 符号 | 含义 |
|------|------|
| `.` | 当前目录 |
| `..` | 上一级目录 |
| `~` | 你的用户主目录（家） |
| `/` | 根目录（硬盘最顶层） |

**文件名带空格或中文怎么办？** 两种办法：① 用引号包起来 `cd "my folder"`；② 用反斜杠转义空格 `cd my\ folder`。中文文件名通常直接写即可，但善用下面的 Tab 补全最省心。

---

## 四、效率技巧（老手和新手的差距全在这）

- **Tab 自动补全**：敲一半按 `Tab`，自动补全命令或文件名，既快又能避免打错。名字太长时先敲头几个字母再按 Tab。
- **上/下方向键**：翻看并重复执行历史命令，不用重敲。
- **Ctrl + L**：清屏，界面太乱时按一下。
- **Ctrl + C**：终止当前正在运行的程序（卡住、跑不停时的「急停键」）。
- **Ctrl + A / Ctrl + E**：光标跳到行首 / 行尾。
- **Cmd + T / Cmd + W**：新建标签页 / 关闭当前标签页（Mac 终端）。

---

## 五、安全警告专题：别把自己电脑删了

网上流传一句臭名昭著的「恶作剧命令」：

```
rm -rf /
```

它的意思是「从根目录 `/` 开始，强制、递归地删除一切」——也就是**删光整块硬盘的所有文件**，系统直接报废。类似危险的还有 `rm -rf ~`（删光你的主目录）、`rm -rf *`（删光当前目录所有东西）。

**为什么危险**：`rm` 不进回收站、不可恢复；`-r` 让它钻进每一层子文件夹，`-f` 让它不再向你确认，一路删到底。

**如何避免误删**：

1. 敲 `rm` 前先用 `pwd` + `ls` 确认「我在哪、要删的是不是它」。
2. 新手养成用 `rm -i`（逐个确认）的习惯。
3. **绝不复制粘贴看不懂的命令**，尤其带 `sudo rm -rf` 的——`sudo` 会赋予最高权限，破坏力更大。
4. 重要文件先备份，练手就在专门建的测试文件夹里操作。

---

## 命令速查表

| 命令 | 全称 | 作用 | 常用例子 |
|------|------|------|----------|
| `pwd` | print working directory | 显示当前所在目录 | `pwd` |
| `ls` | list | 列出目录内容 | `ls -lh` |
| `cd` | change directory | 切换目录 | `cd ..` / `cd ~` / `cd -` |
| `mkdir` | make directory | 新建文件夹 | `mkdir -p a/b/c` |
| `rm` | remove | 删除文件/文件夹（⚠️无回收站） | `rm -i note.txt` |
| `open` | open | 用默认软件打开 | `open .` |
| `cat` | concatenate | 显示文件内容 | `cat note.txt` |
| `cp` | copy | 复制 | `cp -r dir1 dir2` |
| `mv` | move | 移动 / 重命名 | `mv old.txt new.txt` |
| `touch` | touch | 新建空文件 | `touch note.txt` |
| `man` | manual | 查看命令说明书 | `man ls` |
| `clear` | clear | 清屏 | `clear` |

**上手练习流程**（复制到终端一步步敲，最后自己清理）：

```bash
pwd              # 看我在哪
cd ~             # 回家
mkdir test       # 建练习文件夹
cd test          # 进去
touch a.txt      # 建个空文件
ls -l            # 查看，读一读每一列
cd ..            # 退回上级
rm -ri test      # 逐个确认着删掉练习文件夹
```

---

## 参考资料

- [The Linux Command Handbook – freeCodeCamp](https://www.freecodecamp.org/news/the-linux-commands-handbook/) —— 英文经典入门手册，系统讲解 ls/cd/cp/mv/rm 等命令及其原理。
- [50+ Essential Linux Commands – DigitalOcean](https://www.digitalocean.com/community/tutorials/linux-commands) —— 权威社区教程，命令齐全、例子清晰，适合当查询字典。
- [Basic Linux Commands – GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/basic-linux-commands/) —— 逐命令配示例截图，讲解 `-p`、`-r` 等常用选项。
- [面向初学者的命令行教程 – freeCodeCamp 中文](https://www.freecodecamp.org/chinese/news/command-line-for-beginners/) —— 中文，解释终端/shell/CLI 的区别与基本原理，含危险命令警示。
- [玩转 Terminal 终端：入门指南及进阶技巧 – 少数派](https://sspai.com/post/45534) —— 中文，专为 Mac 用户，讲清哪些能碰、哪些是雷区，附实用技巧。
- [3分钟学会打开终端（Windows & Linux 全攻略）– Bilibili 视频](https://www.bilibili.com/video/BV1RGQvBQErC/) —— 3 分钟短视频，手把手教多种系统打开终端并附快捷键速查。
