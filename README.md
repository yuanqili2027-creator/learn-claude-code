# 和 AI 一起用电脑 · 实战课综合笔记

面向电脑新手的 Claude Code 教学站：从命令行零基础到建站、发布幻灯片、完成真实工作。

- **线上地址**：https://yuanqili2027-creator.github.io/learn-claude-code/
- 内容来源：两堂真实课程（2026-06 电脑基本功 + 2026-07 Claude Code 实战）的整理笔记，外加联网调研的案例与最佳实践。

## 维护说明（写给未来的 Claude Code 会话）

- 章节正文在 `content/*.md`（第一课 topic1-8，第二课 c01-c11），Prompt 模板在 `prompts/*.md`。
- **改完 md 必须跑 `python3 build.py` 重新生成 HTML**（依赖 pandoc），HTML 输出在仓库根目录，与 md 一起提交推送。
- 新增章节：在 `build.py` 的 `LESSON1/LESSON2` 列表里登记 `(文件id, 标题, 副标题, 图标, 侧栏简称)`，再写 `content/<id>.md`。
- 样式：`assets/style.css`，瑞士风（白底 `#ffffff` / 近黑 `#0a0a0a` / 瑞士红 `#e30613`，Helvetica 栈，粗黑分隔线）。不引入框架。
- **安全红线：任何 API token、秘钥不得出现在本仓库**（示例一律打码为 `cr_****…`）。提交前 `grep -rn "cr_[a-z0-9]\{20,\}" content prompts` 应无结果。
- GitHub Pages 从 main 分支根目录发布。
