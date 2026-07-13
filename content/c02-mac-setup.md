# Mac 安装与配置：从裸机到 Claude Code 跑起来

本章假设一台**全新的 Mac**。四步：装 Homebrew → 装工具 → 配置 Claude Code → 启动。全程在「终端」App 里完成（`⌘ + 空格` 搜 Terminal 打开）。

## 第 1 步：安装 Homebrew

Homebrew 是命令行世界的「App Store」（详见第一课·话题 4）。粘贴执行：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 过程中会要求输入**开机密码**（输入时屏幕不显示任何字符，是正常的，输完回车）。
- 国内网络如果卡住，先开代理，或使用中科大镜像安装脚本（搜「Homebrew 中科大镜像」）。
- 装完后按提示把 brew 加入 PATH（安装器最后会打印两行以 `echo` 开头的命令，照着粘贴执行）。

验证：`brew --version` 能打印版本号即成功。

## 第 2 步：安装工具三件套

```bash
brew install git gh node          # git 版本管理 / gh GitHub 命令行 / node 运行环境
npm install -g @anthropic-ai/claude-code   # Claude Code 本体
```

逐个说明：

| 命令 | 装了什么 | 干什么用 |
|------|---------|---------|
| `git` | 版本管理工具 | 记录文件的每一次修改，把代码推到 GitHub |
| `gh` | GitHub 官方命令行 | 在终端里登录 GitHub、建仓库、开 Pages |
| `node` | JavaScript 运行环境 | Claude Code 和很多网页工具（如 Slidev）的地基 |
| `claude-code` | AI 编程助手 | 本课主角，能真正操作你的电脑干活 |

验证：`claude --version` 有输出即成功。

## 第 3 步：配置 API（课堂代理方案）

Claude 官方 API 在国内无法直接访问，课堂提供代理服务器。在终端执行（**秘钥向老师索取**，不要使用别人的、也不要把自己的发到网上）：

```bash
export ANTHROPIC_BASE_URL="https://crs.sat1600ap5.online/api"   # 把请求发到代理服务器
export ANTHROPIC_AUTH_TOKEN="cr_********************************"  # 你自己的秘钥
```

两行命令的含义：

- `export` 是设置**环境变量**——当前这个终端窗口里的「便签」，程序启动时会来读。
- `ANTHROPIC_BASE_URL` 告诉 Claude Code「去哪个服务器要 AI」；
- `ANTHROPIC_AUTH_TOKEN` 是你的通行证，代理靠它识别你、计费。

⚠️ **`export` 只对当前窗口有效**，关掉终端就失效。想永久生效，把这两行追加到 `~/.zshrc` 文件末尾（`echo 'export ...' >> ~/.zshrc`），以后每个新终端窗口自动加载。

⚠️ **秘钥是敏感信息**：等同于「能花你钱的密码」。不要发群里、不要写进要公开的代码仓库、不要出现在截图里。本站所有示例都做了打码。

## 第 4 步：启动 Claude Code

```bash
cd ~/Projects/my-first-project    # 先进入你的项目文件夹（没有就 mkdir 一个）
claude --dangerously-skip-permissions
```

关于 `--dangerously-skip-permissions`（跳过权限确认模式）：

- **默认模式**下，Claude 每次要改文件、跑命令都会先请求你批准——安全，但频繁点确认很打断节奏。
- **加了这个参数**，它就不再逐条询问，自主干活——课堂演示用它是为了流畅，但它名字里的 dangerously 是认真的：AI 可以不经确认地修改、删除文件。
- **给新手的建议**：只在专门的项目文件夹里用这个模式（别在桌面、别在文档目录），重要文件先备份；等熟练后改用默认模式 + 按需批准，或在设置里精细配置白名单。

常用启动变体：

```bash
claude                                        # 默认模式（每步询问，最安全）
claude --dangerously-skip-permissions         # 跳过确认（快，风险自负）
claude --dangerously-skip-permissions --continue   # 接着上一次对话继续
```

`--continue` 非常实用：Claude Code 的对话是有记忆的，关掉终端后用它可以**恢复上次聊到一半的工作**，不必从头解释。

## 完成检查清单

- [ ] `brew --version` 有输出
- [ ] `git --version`、`gh --version`、`node --version` 都有输出
- [ ] `claude --version` 有输出
- [ ] 在项目文件夹里启动 `claude`，随便问它一句话，能正常回答

下一章：GitHub 账号与 gh 命令行登录。
