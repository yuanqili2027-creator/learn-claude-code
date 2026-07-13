# 文件系统结构：你的电脑就是一棵大树

## 一、心智模型：文件系统是一棵倒着长的树

想象一棵树，但它是**头朝下、根朝上**长的。最顶上有一个总的起点，叫「根目录」，写作一个斜杠 `/`。从这个根往下，长出一根根树枝（文件夹），树枝上又分出更细的枝（子文件夹），最末梢挂着一片片叶子（文件，比如 `hello.py`、一张照片、一份 PDF）。

关键规则只有一条：**每一层之间用斜杠 `/` 隔开**。所以当你看到 `/Users/yuanqili/Desktop/hello.py`，其实是在读一条「从树根走到某片叶子」的路线：

```
/                         ← 根目录（整棵树的起点）
└── Users/                ← 所有用户的家都在这
    └── yuanqili/         ← 你的家（用户主目录）
        └── Desktop/      ← 桌面文件夹
            └── hello.py  ← 一个具体的文件（叶子）
```

「文件夹」和「目录」是同一个东西的两个叫法：Finder 里叫文件夹，命令行里叫目录（directory）。心里知道它们等价即可。

## 二、根目录 `/` 下有哪些主要「树枝」

打开根目录，你会看到一堆系统文件夹。你**平时基本不用碰它们**，但认识一下能消除神秘感：

```
/
├── System/         ← macOS 的心脏，系统本体，只读，别动
├── Applications/   ← 你装的图形应用（如 Chrome、VS Code）都在这
├── Users/          ← 所有用户的主目录，你天天用的就是这里 ★
├── Library/        ← 全体用户共享的配置/支持文件
├── usr/            ← Unix 命令行工具和库（如 /usr/bin 里的小程序）
├── bin/            ← 最基础的命令（如 ls、cp）
├── etc/            ← 系统级配置文件
└── tmp/            ← 临时文件，重启可能被清空
```

一句话记忆：**带大写字母的（System / Applications / Users / Library）是苹果风格的、给人看的；全小写的（usr / bin / etc / tmp）是老 Unix 传统、给系统用的。** 我们的主战场只有一个：`/Users/你的用户名/`。

## 三、你的家：用户主目录 `~`

`/Users/你的用户名/` 就是你的「家」，专属于你、你有完全控制权。这个路径太常用了，于是有个简写符号 **波浪号 `~`**，它永远代表「当前用户的主目录」。所以 `~/Desktop` 和 `/Users/yuanqili/Desktop` 指的是同一个地方。

家里出厂自带这几个标准文件夹：

```
~/  (= /Users/yuanqili/)
├── Desktop/     桌面 —— 屏幕上看到的那些图标就放这
├── Documents/   文稿 —— 文档、表格、PPT 的默认归宿
├── Downloads/   下载 —— 浏览器下载的东西默认落这
├── Movies/      影片 —— 视频
├── Music/       音乐 —— 音频
├── Pictures/    图片 —— 照片、截图
├── Public/      公共 —— 想和别人共享的文件放这
└── Library/     资源库 —— 你的个人配置（默认隐藏，别乱删）
```

`Library` 默认是隐藏的（藏起来是怕新手误删），里面存的是各种应用的偏好设置和数据。记住「不要手动删 Library 里的东西」就够了。

## 四、路径怎么读：绝对、相对、还有 `~`

一个文件的「地址」有三种写法，理解它们能少踩很多坑：

- **绝对路径**：从根 `/` 开始写全，像身份证号一样唯一。例：`/Users/yuanqili/Projects/hello.py`。任何时候、在任何地方用它都指向同一个文件。
- **相对路径**：从「你现在所在的位置」出发，不以 `/` 开头。如果你人在 `~/Projects/`，那 `hello.py` 就够了；`../` 表示「上一级文件夹」。它更短，但含义取决于你站在哪。
- **`~` 展开**：`~` 是绝对路径的贴心简写，系统会自动把它替换成 `/Users/你的用户名`。`~/Desktop/hello.py` 完全等价于 `/Users/yuanqili/Desktop/hello.py`。

读路径的诀窍：**从左往右，每遇到一个 `/` 就「进入下一层文件夹」，最后一段通常是文件本身。**

## 五、iCloud「桌面与文稿」同步：好用，但别拿来放代码

macOS 有个功能，可以把你的 **桌面（Desktop）和文稿（Documents）自动同步到 iCloud**（系统设置 → 你的名字 → iCloud → 云盘 → 打开「桌面与文稿文件夹」）。好处很实在：换设备也能看到文件、自动云备份、iPhone 上也能打开。对普通文档，这是好功能。

但**对写代码的人，这是个坑**，原因是：

1. **文件会被「卸载」偷偷搬走**：iCloud 为省本地空间，会把不常用文件替换成一个「占位符」，需要时再下载。可编辑器、编译器（VS Code、Xcode 等）默认文件就在本地、能立刻读到——结果就是「昨晚还能跑的项目，早上打开文件是空的」。
2. **海量小文件同步不可靠**：一个代码项目里 `node_modules`、`.git` 动辄成千上万个碎文件，频繁读写。iCloud 同步这些时极易冲突，甚至把文件另存成「副本」造成重复和混乱。
3. **可能损坏 Git 仓库**：`.git` 里的版本信息被同步搞得残缺，仓库就坏了。
4. **占满 iCloud 空间**：一次大型构建就可能塞满你的 iCloud 配额。

**结论与建议**：**代码项目不要放在桌面和文稿里**，单独建一个不被同步的文件夹（下面第七节讲）；真正的「备份」用 Git + 远程仓库（GitHub 等），那才是给代码设计的版本管理。

## 六、命名规范：为什么别用空格、中文、标点

图形界面里你叫文件夹「我的 项目（第1版）」似乎没问题，可一旦进入命令行或代码里，麻烦就来了：

- **空格会被误解成「分隔符」**：命令行里 `cd 我的 项目` 会被当成两个东西，报错。
- **中文和标点在某些工具/系统里会乱码或不被支持**，跨设备协作尤其容易出问题。
- **括号、`#`、`&` 等符号在命令行里有特殊含义**，会引发莫名其妙的错误。

推荐用 **kebab-case（短横线小写）**：全部小写字母、单词间用连字符 `-` 连接。

```
✅ 推荐                       ❌ 避免
my-first-project            我的第一个项目
learn-python                Learn Python (含空格)
todo-app-2026               todo_app（下划线也行，但团队里 - 更通用）
notes-draft                 notes(草稿).txt
```

一句话：**小写 + 连字符，不要空格、不要中文、不要标点。** 养成这个习惯，未来省无数麻烦。

## 七、推荐的项目组织方式

在你的**主目录**下，专门建一个放代码的文件夹（名字用 `Projects` 或 `development` 都行），每个项目一个子文件夹，互不干扰：

```
~/  (/Users/yuanqili/)
├── Desktop/          （日常文件，会同步 iCloud）
├── Documents/        （文档，会同步 iCloud）
└── Projects/         ★ 你的开发大本营（不同步，专放代码）
    ├── learn-python/
    │   ├── hello.py
    │   └── notes.md
    ├── my-website/
    └── todo-app/
```

这样做的好处：代码和日常文件彻底分开、不受 iCloud 折腾、找项目一目了然。以后写代码，第一步就是「回到 `~/Projects` 里给新项目开个文件夹」。

## 参考资料

1. [Add your Desktop and Documents files to iCloud Drive — Apple 官方支持](https://support.apple.com/en-us/109344)：苹果官方讲「桌面与文稿」同步到 iCloud 的设置方法与注意事项，第五节内容的权威来源。
2. [Store files in iCloud Drive on Mac — Apple 官方 Mac 使用手册](https://support.apple.com/guide/mac-help/store-files-in-icloud-drive-mchle5a61431/mac)：苹果官方讲 iCloud 云盘如何存取文件，理解同步机制的一手资料。
3. [macOS 目录结构详解 — CSDN](https://blog.csdn.net/greenspan/article/details/151333739)：中文详解根目录下各文件夹用途，以及 Catalina 之后的只读系统卷宗变化。
4. [Mac 文件系统结构及各主要目录位置 — CSDN](https://blog.csdn.net/qq_31908651/article/details/104484083)：讲清 macOS 的四大区域（User/Local/Network/System）与 `~` 符号的含义。
5. [Syncing Developer Projects with iCloud Drive — Apple 官方社区讨论](https://discussions.apple.com/thread/255625170)：真实开发者反馈 iCloud 同步代码导致文件消失、构建失败的案例，第五节踩坑的现实佐证。
6. [MacOS 文件目录 — 个人技术博客](https://chendot.github.io/post/2020/0614-mac-dir/)：面向开发者的简明目录结构梳理，可作为轻量参考。
