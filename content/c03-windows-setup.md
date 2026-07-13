# Windows 方案：WSL2 + Ubuntu

Windows 和 Mac/Linux 是两套不互通的体系（原因见第一课·话题 1）。好消息是微软官方提供了 **WSL（Windows Subsystem for Linux）**——在 Windows 里原生运行一个真正的 Linux。装好之后，本课所有 Mac/Linux 命令**原样可用**，你和 Mac 同学的操作完全一致。

## 总览：三步走

1. 启用 WSL2 并安装 Ubuntu（微软官方 Linux 发行版渠道）
2. 在 Ubuntu 里装工具链（对应 Mac 的第 2 步）
3. 配置并启动 Claude Code（与 Mac 完全相同）

## 第 1 步：安装 WSL2 + Ubuntu

**要求**：Windows 10 2004 以上或 Windows 11。

1. 右键开始菜单 →「终端（管理员）」或「PowerShell（管理员）」；
2. 执行一条命令：

```powershell
wsl --install
```

这条命令会自动完成：启用 WSL 功能 → 安装 WSL2 内核 → 从微软商店安装 Ubuntu。**重启电脑**。

3. 重启后系统会自动打开 Ubuntu 窗口做初始化，让你设置一个 **Linux 用户名和密码**（和 Windows 密码无关；输入密码时屏幕不显示，正常）。

> 如果 `wsl --install` 报错或商店不可用：打开 Microsoft Store，搜索「Ubuntu」，手动安装「Ubuntu 24.04 LTS」，再在管理员 PowerShell 里跑 `wsl --set-default-version 2`。

以后每次要用命令行，就从开始菜单打开 **Ubuntu**（或在 Windows Terminal 里选 Ubuntu 标签）——那就是你的 Linux 终端。

## 第 2 步：在 Ubuntu 里装工具链

Ubuntu 用 `apt` 做包管理（相当于 Mac 的 brew）。逐条执行：

```bash
sudo apt update && sudo apt upgrade -y        # 更新软件源（sudo = 用管理员权限执行）
sudo apt install -y git curl                  # git 和下载工具

# 安装 gh（GitHub CLI 官方源）
(type -p wget >/dev/null || sudo apt install wget -y) \
  && sudo mkdir -p -m 755 /etc/apt/keyrings \
  && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
  && sudo apt update && sudo apt install gh -y

# 安装 Node.js（用 nvm，避免 apt 里版本太老）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install --lts

# 安装 Claude Code
npm install -g @anthropic-ai/claude-code
```

## 第 3 步：配置与启动（与 Mac 相同）

```bash
export ANTHROPIC_BASE_URL="https://crs.sat1600ap5.online/api"
export ANTHROPIC_AUTH_TOKEN="cr_********************************"   # 秘钥向老师索取
claude --dangerously-skip-permissions
```

想永久生效，追加到 `~/.bashrc`（Ubuntu 默认 shell 是 bash，不是 zsh）：

```bash
echo 'export ANTHROPIC_BASE_URL="https://crs.sat1600ap5.online/api"' >> ~/.bashrc
echo 'export ANTHROPIC_AUTH_TOKEN="cr_你的秘钥"' >> ~/.bashrc
```

## WSL 专属注意事项

- **文件放哪**：把项目放在 Linux 侧（如 `~/Projects/`），**不要**放在 `/mnt/c/...`（即 Windows 的 C 盘）里干活——跨系统文件读写慢好几倍，还容易出权限问题。
- **怎么和 Windows 互传文件**：在 Ubuntu 里执行 `explorer.exe .` 会用 Windows 资源管理器打开当前 Linux 目录，直接拖拽即可。
- **VS Code**：在 Windows 装 VS Code + 「WSL」扩展，然后在 Ubuntu 目录里敲 `code .`，体验和 Mac 完全一致。
- **代理**：Windows 上开的代理默认不管 WSL 内部流量。如果 brew/GitHub 连不上，需在代理软件里开启「允许局域网连接」并在 Ubuntu 里设置 `http_proxy` 环境变量（各代理软件文档都有 WSL 教程）。

装完后，回到第 4 章继续 GitHub 配置——从那里开始，Windows 和 Mac 殊途同归。
