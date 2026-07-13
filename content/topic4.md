# Homebrew：macOS 的命令行「应用商店」

在 Mac 上装软件，大多数人习惯去官网下载一个 `.dmg`，拖进「应用程序」文件夹。这套流程对付图形软件够用，但如果你想装命令行工具（比如 `python3`、`wget`、`git`），就会发现无处下载、无处安装。Homebrew 就是解决这个问题的工具，它是 macOS 上最流行的**命令行包管理器**。macOS 不自带它，必须自己装一次。

## 一、什么是「包管理器」，为什么需要它

想象你要装一个命令行工具，手动做法是：去官网找下载链接 → 下载压缩包 → 解压 → 把可执行文件放到系统能找到的目录 → 配置环境变量 → 如果它依赖别的库，还得把依赖也一个个装好。装 3 个软件就够你折腾一下午，而且卸载、升级同样麻烦。

**包管理器**把这一切自动化了。你只需一句话：「帮我装 wget」，它就自动下载、解压、安装、连同依赖一起处理好，还记录了装过什么、装在哪，方便日后升级和卸载。

用「应用商店」类比很贴切，但有两点区别：

- 应用商店是图形界面点点鼠标，Homebrew 是在**终端里敲命令**。
- 应用商店主要给普通用户装图形 App，Homebrew 更擅长装**开发者和极客用的命令行工具**（当然它也能装图形软件）。

## 二、Homebrew 能装什么：formula vs cask

Homebrew 里有两类「软件包」，理解这个区别很重要：

- **formula（公式）**：命令行工具，比如 `python3`、`node`、`git`、`ffmpeg`。用 `brew install xxx` 安装。
- **cask（酒桶）**：图形界面的 macOS 应用，比如 VS Code、Chrome、微信。用 `brew install --cask xxx` 安装，效果等同于你自己下载 `.dmg` 拖进「应用程序」，只是全自动。

一句话：`brew install` 装命令行工具，`brew install --cask` 装图形 App。

## 三、安装 Homebrew

### 第 1 步：装 Xcode Command Line Tools（命令行工具）

Homebrew 编译和安装软件时需要一套苹果官方的开发者基础工具（编译器、`git` 等），叫 **Command Line Tools（CLT）**。首次安装 Homebrew 时它通常会自动帮你装；你也可以提前手动装：

```bash
xcode-select --install
```

回车后会弹窗，点「安装」等它下载完即可。它不是完整的 Xcode（那个有十几 GB），只是一小套命令行必需组件。

### 第 2 步：运行官方安装命令

打开「终端」（在「启动台」搜 Terminal），粘贴 [官网 brew.sh](https://brew.sh) 首页那条命令并回车：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

这条命令在做什么？拆开看：`curl -fsSL 一个网址` 是从 Homebrew 官方仓库**下载一个安装脚本**，`/bin/bash -c "..."` 是**用 bash 运行这个脚本**。脚本会先告诉你它准备做什么，然后暂停等你确认，是很透明的。

**为什么要输开机密码、而且输入时屏幕不动？** 安装过程需要在系统目录创建文件，属于管理员权限操作，所以要验证你的身份。终端里输密码时**不显示任何字符（连圆点都没有）是 macOS 的正常安全设计**，不是卡住了——你正常盲打，打完回车即可。

## 四、Apple Silicon（M 系列芯片）的特殊之处

如果你的 Mac 是 M1/M2/M3 等 Apple Silicon 芯片，Homebrew 会装在 **`/opt/homebrew`**（老的 Intel 芯片装在 `/usr/local`）。问题是：系统默认不知道去 `/opt/homebrew` 找命令，所以装完后你直接敲 `brew` 可能会报 `command not found`。

解决办法是把 Homebrew 加进 **PATH**（系统搜索命令的路径清单）。安装脚本结束时会提示你运行两行命令，照抄即可：

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

第一行把配置**永久写入**你的终端配置文件 `~/.zprofile`，第二行让它**在当前窗口立即生效**。这也是为什么很多教程让你「装完重开一个终端窗口」——重开后配置文件会被自动加载，`brew` 命令才能被认出来。

## 五、国内网络问题专题（重要）

Homebrew 的软件从 GitHub 和境外服务器下载。在国内**不挂代理/VPN 的情况下，几乎会卡住或失败**。而且要特别注意：**给浏览器开了代理，不等于终端也走代理**——命令行的流量需要单独配置。两种思路：

**思路一：让终端走代理。** 假设你的代理软件在本机 `7890` 端口（具体端口看你的软件设置），在终端执行：

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890
```

这只对当前窗口有效。之后再跑安装命令或 `brew install` 就会走代理。

**思路二：换成国内镜像源。** 用国内高校的镜像服务器替代境外源，不需要代理，速度快。以 [清华 TUNA 镜像](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/) 为例，首次安装前先设置环境变量：

```bash
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
```

再运行安装脚本即可。已经装好的用户，也可以换成中科大源（见参考资料）。

> **安全提醒**：安装命令务必**从官网 brew.sh 复制**，镜像配置从清华/中科大等可信镜像站的官方帮助页复制。网上来路不明的「一键脚本」可能夹带私货，往终端粘贴前一定要看清楚它是什么——终端命令权限很大，别乱执行。

## 六、常见坑

- **`command not found: brew`**：几乎都是 PATH 没配好。回到第四节，重新运行那两行 `brew shellenv` 命令，然后重开终端。
- **权限问题 / sudo**：Homebrew 装在自己的目录里，日常用 `brew` 命令**不需要也不应该加 `sudo`**。如果提示权限报错，通常是目录属主不对，可用 `brew doctor` 诊断，按它给的建议修。

## 七、核心命令讲透

装好后，日常就是这几条命令。下面每条都给例子和预期效果：

- `brew install python3`：装命令行工具。跑完你敲 `python3 --version` 能看到版本号。
- `brew install --cask visual-studio-code`：装图形 App。跑完「应用程序」里会出现 VS Code。
- `brew uninstall wget`：卸载 wget。
- `brew list`：列出你已经装了哪些包，检查「我装过什么」。
- `brew search node`：搜索有没有叫 node 相关的包，装之前先确认名字。
- `brew info wget`：查看某个包的说明、版本、依赖、官网。
- `brew update`：更新 Homebrew 自身和软件清单（不升级你装的软件）。
- `brew upgrade`：把你装的所有软件升级到最新版；`brew upgrade wget` 只升级指定的一个。
- `brew doctor`：体检命令。出问题时先跑它，它会指出隐患并给修复建议。

一个典型流程：`brew update`（先刷新清单）→ `brew search 名字`（确认包名）→ `brew install 名字`（安装）→ 用一阵子后 `brew upgrade`（升级）。

## 常用命令速查表

| 命令 | 作用 | 示例 |
| --- | --- | --- |
| `brew install <名字>` | 安装命令行工具（formula） | `brew install python3` |
| `brew install --cask <名字>` | 安装图形应用（cask） | `brew install --cask visual-studio-code` |
| `brew uninstall <名字>` | 卸载软件 | `brew uninstall wget` |
| `brew list` | 列出已安装的包 | `brew list` |
| `brew search <关键词>` | 搜索软件包 | `brew search node` |
| `brew info <名字>` | 查看包的详细信息 | `brew info ffmpeg` |
| `brew update` | 更新 Homebrew 和软件清单 | `brew update` |
| `brew upgrade` | 升级已安装的软件 | `brew upgrade` |
| `brew doctor` | 检查环境、诊断问题 | `brew doctor` |

## 参考资料

- [Homebrew 官网 brew.sh](https://brew.sh) — 官方主页，首页即提供权威安装命令，一切以此为准。
- [Homebrew 官方安装文档 docs.brew.sh/Installation](https://docs.brew.sh/Installation) — 英文官方文档，详解安装路径（Apple Silicon 为 `/opt/homebrew`）、PATH 配置与前置条件。
- [清华大学 TUNA 镜像 · Homebrew 帮助](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/) — 国内首选镜像，环境变量方式，对 M 系列芯片有专门说明，首次安装最全。
- [中科大 USTC 镜像换源方法](https://www.zzxworld.com/posts/available-cn-mirrors-for-homebrew) — 已装好 Homebrew 后用 git 换源，附国内各镜像源对比与选择建议。
- [2025 Homebrew 国内镜像源配置指南（腾讯云社区）](https://cloud.tencent.com/developer/article/2486985) — 中文图文教程，覆盖清华/中科大/阿里云多种镜像与常见问题。
- [Homebrew CN 一键安装（社区工具）](https://brew-cn.mintimate.cn/) — 内置多镜像的一键安装脚本，适合怕折腾的新手（使用前请核对来源）。
