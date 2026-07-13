# 课程总览：一个下午，从零到三个网站

这一课的全部内容，来自一次真实的完整实战：**一台电脑 + 一个全新注册的 GitHub 账号 + Claude Code**，在一个下午里陆续完成了下面这些事。本页是故事线总览，每一步用到的技术都有专门章节展开。

## 今天实际做成的事

| 步骤 | 产出 | 用到的技术 |
|------|------|-----------|
| 1. 注册 GitHub 并配置命令行 | `gh` 登录成功，git 身份配置完毕 | GitHub 账号、gh CLI、git config |
| 2. 发布第一个网页（测试） | hello-pages 仓库 + 一个 Hello World 页面 | `gh repo create`、GitHub Pages |
| 3. 个人学术主页 | [yuanqili2027-creator.github.io](https://yuanqili2027-creator.github.io/) | 需求访谈 → 设计确认 → 后台 subagent 施工 |
| 4. 第一个幻灯片站（非洲史） | [slides-african-history](https://yuanqili2027-creator.github.io/slides-african-history/) | Slidev、数据图表、截图自查 |
| 5. 论文转幻灯片（Bézier 曲线） | [slides-bezier-curves](https://yuanqili2027-creator.github.io/slides-bezier-curves/) | 读 LaTeX 论文、KaTeX 公式、图片迁移 |
| 6. 本教学站 | 你正在看的这个网站 | 全流程整合 + 联网调研 |

## 这条路线为什么值得学

传统印象里，「做一个网站」「做一份漂亮的幻灯片」是两种完全不同的技能，各要学几个月。但今天的路线把它们统一成了**同一件事**：

1. **一切内容都是文本文件**（HTML / Markdown / CSS），AI 最擅长生成文本文件；
2. **发布就是把文件推到 GitHub**，`git push` 一条命令；
3. **GitHub Pages 免费把文件变成网站**，全世界可访问的链接，一分钟内生效。

你要做的只是：把需求讲清楚（第 7 章专门讲怎么讲），剩下的交给 Claude Code。

## 学习路径建议

- **完全没碰过命令行** → 先读「第一课·电脑基本功」的话题 1–3（操作系统、命令行、文件系统），再回来。
- **有一点基础** → 直接从第 2 章（Mac）或第 3 章（Windows）开始装环境，装完按第 4、5 章跑通 GitHub 发布，最后看第 7 章学怎么提问。
- **只想抄作业** → 「Prompt 模板」页有今天用过的核心提示词，可直接下载改用。

## 一个诚实的提醒

今天所有的产出，都不是「一句话生成」的。真实流程是：**讲清需求 → AI 提问澄清 → 确认方案 → AI 干活 → 检查结果 → 指出问题 → 修正**。AI 极大压缩了「干活」环节的时间，但「讲清楚要什么」和「验收」始终是你的工作。这门课教的正是这两头。
