# GitHub 与 gh 命令行：让 AI 替你管理代码仓库

## GitHub 是什么

**GitHub（github.com）是世界最大的代码托管平台**——可以粗糙地理解为「程序员的网盘 + 朋友圈」：文件放上去有完整的修改历史，可以公开分享，别人能围观、复制、参与你的项目。全球几乎所有开源软件都住在这里。对本课来说，它还有一个杀手级赠品：**免费网站托管（GitHub Pages，下一章）**。

三个高频词先解释：

- **仓库（repository / repo）**：一个项目一个仓库，本质是「一个带修改历史的文件夹」。
- **git**：本地的版本管理工具，负责记录修改、与 GitHub 同步。GitHub 是网站，git 是工具，两者不是一个东西。
- **推送（push）**：把本地的修改上传到 GitHub。

## 第 1 步：注册账号

去 [github.com](https://github.com/) 用邮箱注册，记住你的**用户名**——它会出现在你所有网站的网址里（`你的用户名.github.io`），起名慎重。

## 第 2 步：命令行登录（gh auth login）

`gh` 是 GitHub 官方命令行工具，登录一次，之后 Claude Code 就能全权替你操作 GitHub。

```bash
gh auth login
```

交互式提问按下面选：

1. **What account do you want to log into?** → `GitHub.com`
2. **Preferred protocol?** → `HTTPS`（比 SSH 少配置，gh 自动管理凭证）
3. **Authenticate Git with your GitHub credentials?** → `Yes`（关键！让 `git push` 也免密）
4. **How would you like to authenticate?** → `Login with a web browser`

终端会显示一个 8 位一次性码，回车后自动打开浏览器，粘贴该码并授权即完成。

> 这一步必须**你自己**在终端里操作（涉及浏览器授权），是整门课极少数 AI 无法代劳的步骤之一。

验证：

```bash
gh auth status            # 显示已登录账号和权限
gh api user --jq .login   # 从 GitHub 服务器读回你的用户名
```

## 第 3 步：配置 git 身份

每次提交（commit）都会署名，全局设置一次：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

**隐私技巧**：不想公开真实邮箱，用 GitHub 提供的马甲邮箱。格式是 `数字ID+用户名@users.noreply.github.com`，数字 ID 可用 `gh api user --jq .id` 查到。用它做 `user.email`，提交照样正确归属到你的账号，但真实邮箱不泄露。

## 常用命令速览（Claude Code 会替你敲，但你要看得懂）

```bash
# 仓库
gh repo create 仓库名 --public          # 建一个公开仓库
gh repo create 仓库名 --public --source . --push   # 把当前文件夹建成仓库并推上去
gh repo delete 仓库名 --yes             # 删除仓库（危险，不可逆）
gh repo list                            # 列出你的所有仓库

# 日常三连（修改 → 记录 → 上传）
git add -A                              # 把所有修改放入「待提交区」
git commit -m "说明这次改了什么"          # 记录一次快照
git push                                # 推送到 GitHub

# 其他
gh api user                             # 读取账号信息（JSON）
gh auth switch -u 用户名                 # 多账号之间切换
gh auth refresh -s workflow             # 给 token 补充权限（如需要操作 CI）
```

## 和 Claude Code 的配合方式

登录配置完成后，你在 Claude Code 里只需要说人话：

- 「帮我把这个文件夹建成一个公开仓库并推送到 GitHub」
- 「提交当前所有修改，写好提交说明」
- 「帮我看看我的账号下有哪些仓库」

它会自动组合上面的命令。你的工作是**看它执行前的说明，确认它要做的事符合预期**——尤其是任何带「删除」字样的操作。
