# 命令速查表：今天出现过的每一条命令

按场景分组。左边是命令，右边是人话解释。看不懂的名词回第一课查。

## 环境安装

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
安装 Homebrew。`curl` 下载安装脚本，`bash -c` 立即执行它。

```bash
brew install git gh node        # 一次装多个软件
npm install -g @anthropic-ai/claude-code   # -g = 全局安装，任何目录都能用 claude 命令
wsl --install                   # （Windows）一条命令装好 WSL2 + Ubuntu
sudo apt install git            # （Ubuntu）apt 是 Ubuntu 的 brew；sudo = 以管理员身份
```

## Claude Code

```bash
export ANTHROPIC_BASE_URL="https://…/api"    # 设置环境变量：API 服务器地址
export ANTHROPIC_AUTH_TOKEN="cr_…"           # 设置环境变量：你的秘钥（保密！）
claude                                       # 默认模式启动（每个操作请求批准）
claude --dangerously-skip-permissions        # 跳过批准，全自动（风险自担）
claude --dangerously-skip-permissions --continue   # 恢复上一次对话
```

在 Claude Code 对话中还有斜杠命令：`/model` 换模型、`/clear` 清空重来、`!命令` 直接执行一条终端命令并把结果带进对话。

## GitHub 身份与登录

```bash
gh auth login                    # 交互式登录（选 HTTPS + 浏览器授权 + Yes 授权 git）
gh auth status                   # 查看登录状态、当前账号、token 权限
gh auth switch -u 用户名          # 多账号切换
gh api user --jq .login          # 调 GitHub API 读自己的用户名（--jq 提取字段）
gh api user --jq .id             # 读数字 ID（拼 noreply 邮箱用）
git config --global user.name  "名字"   # 全局提交署名
git config --global user.email "邮箱"   # 推荐用 ID+用户名@users.noreply.github.com
```

## 仓库日常

```bash
git init -b main                 # 把当前文件夹初始化为仓库，主分支叫 main
git add -A                       # 暂存全部修改（A = all）
git commit -m "说明"              # 记录一次快照
git push                         # 上传到 GitHub
git push -u origin main          # 第一次推送（-u 记住对应关系，以后裸 push 即可）
gh repo create 名字 --public                     # 建远程仓库
gh repo create 名字 --public --source . --push   # 建仓 + 绑定当前目录 + 直接推
gh repo delete 名字 --yes                        # 删仓库（不可逆！）
```

## GitHub Pages

```bash
gh api repos/用户/仓库/pages -X POST -f "source[branch]=main" -f "source[path]=/"
# 开启 Pages：从 main 分支根目录发布；path 也可以是 /docs

curl -s -o /dev/null -w "%{http_code}" https://用户.github.io/仓库/
# 探测网站状态码：200=已上线 404=未生效或路径错
```

## Slidev 幻灯片

```bash
npm install @slidev/cli @slidev/theme-default   # 装进当前项目
npx slidev                                      # 本地预览（写作时开着）
npx slidev build --base /仓库名/ --out docs      # 构建静态站到 docs/
npx slidev export --format png --per-slide      # 逐页导出 PNG（AI 自查用）
```

## 常用小工具

```bash
pwd / ls / cd 目录 / mkdir 目录     # 我在哪 / 有什么 / 去哪 / 建文件夹（第一课·话题 2）
echo '一行文字' >> 文件              # 把文字追加到文件末尾（配置 .zshrc 用）
cat 文件                            # 打印文件内容
open .                              # （Mac）用访达打开当前目录
explorer.exe .                      # （WSL）用 Windows 资源管理器打开当前目录
which 命令名                         # 查一个命令装在哪、装没装
```
