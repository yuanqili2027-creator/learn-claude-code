# Claude Code 实战案例与最佳实践

> 本章汇总官方文档的核心建议、来自真实工程师和普通用户的一手案例，以及社区踩过的坑。所有内容均附来源链接，建议按需精读原文。

## 一、官方最佳实践

### 1. 一切围绕"上下文窗口"展开

[官方最佳实践指南](https://code.claude.com/docs/en/best-practices)开宗明义：几乎所有最佳实践都源于一个约束——**上下文窗口填满得很快，而且越满效果越差**。由此衍生的习惯：

- 在**不相关的任务之间用 `/clear`** 清空会话，别把上一个任务的"残渣"带进下一个任务。
- 长会话用 **`/compact <指令>`** 做定向压缩（比如"只保留与登录功能相关的结论"），而不是被动等它塞满。
- 同一个问题**纠正超过两次就应该 `/clear` 重开**：干净会话 + 吸收了教训的更好提示词，几乎总是胜过塞满失败尝试的长会话。

### 2. 四阶段工作流：探索 → 计划 → 实现 → 提交

官方推荐的[标准工作流](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)：

1. **Explore**：按 `Shift+Tab` 进入 Plan Mode（只读模式），让 Claude 先读代码、理解现状；
2. **Plan**：让它生成实现计划，`Ctrl+G` 可以在编辑器里直接修改计划；
3. **Implement**：批准计划后退出 Plan Mode 执行，并对照计划验证；
4. **Commit**：提交代码、开 PR。

官方同时明确提醒**不要滥用计划**：如果一句话就能描述改动（改错字、加日志、重命名），直接做，跳过计划。计划最适合多文件改动、方案不确定或不熟悉的代码。敏感项目可以在 `.claude/settings.json` 里把 `permissions.defaultMode` 设为 `plan`，默认从计划开始。

### 3. 给 Claude 一个它自己能跑的"验证手段"

这是官方反复强调的一条：给 Claude 提供**可自行运行的验证方式**——测试用例、构建退出码、lint、截图对比——让它自己迭代到通过为止，而不是由你肉眼当验证环节。把"看起来完成"变成"检查通过才算完成"，还可以用 `/goal` 或 Stop hook 把验证变成硬性关卡。（[来源](https://code.claude.com/docs/en/best-practices)）

同时要求 Claude **出示证据**（测试输出、命令返回值、结果截图），而不是口头声称"已完成"。

### 4. 提示词要具体，并指向已有范式

- 指定文件、场景、约束，例如"参考 HotDogWidget.php 的模式实现日历组件"，而不是凭空描述需求。
- 大型功能先让 Claude 用 AskUserQuestion 工具**"面试"你**，产出 SPEC.md，再开一个新会话干净地执行。（[来源](https://code.claude.com/docs/en/best-practices)）

### 5. CLAUDE.md：项目的"长期记忆"，但要克制

[官方 memory 文档](https://code.claude.com/docs/en/memory)的要点：

- CLAUDE.md 按四级作用域顺序加载：组织策略 → `~/.claude/CLAUDE.md`（个人全局）→ 项目 `./CLAUDE.md`（进 git）→ `./CLAUDE.local.md`（个人项目级，进 .gitignore）。
- **单文件控制在 200 行以内**：文件越臃肿遵循度越差，"重要规则会淹没在噪音里"。每一行都问自己："删掉它 Claude 会犯错吗？"不会就删。
- **该写**：Claude 猜不到的构建命令、与默认不同的代码风格、测试指令、分支/PR 约定、环境坑点。**不该写**：读代码就能知道的东西、语言通用惯例、"写干净代码"这种空话。
- CLAUDE.md 是上下文而非强制配置——**必须每次执行的动作（如提交前 lint）应该写成 hook**。用 `/init` 生成初始文件，用 `/memory` 检查哪些文件实际被加载。
- 大项目可用 `.claude/rules/*.md` 拆分规则，并用 paths frontmatter 做路径条件加载。

另外，[Auto Memory](https://code.claude.com/docs/en/memory#auto-memory)（v2.1.59+ 默认开启）会让 Claude 自动把构建命令、调试心得、你的纠正偏好记到 `~/.claude/projects/<project>/memory/`。对 Claude 说"记住用 pnpm 不用 npm"会写入 auto memory；说"把这条加进 CLAUDE.md"则写入指令文件。

### 6. 权限模式：在"逐个审批"和"全放行"之间找平衡

[官方权限文档](https://code.claude.com/docs/en/permission-modes)列出六种模式：default（逐个审批）→ acceptEdits（自动批准文件编辑）→ plan（只读）→ auto（分类器兜底放行）→ dontAsk（只允许预批清单）→ bypassPermissions（全放行，仅限隔离容器/VM）。

官方直言**审批疲劳的危害**："点到第十次批准时你已经不是在审查，只是在点确认"。推荐三选一来减少打断：auto mode（独立分类器会默认拦截 `curl|bash`、生产部署、force push、`git reset --hard` 等高危操作）、`/permissions` 白名单、或 `/sandbox` OS 级隔离。注意 `.git`、`.claude`、shell rc 文件等**保护路径**在任何模式（除 bypass）下都不会被自动批准。

### 7. 子代理与多会话：用"上下文隔离"提高质量

- [子代理](https://code.claude.com/docs/en/sub-agents)的核心价值是**上下文隔离**：调研类任务会读大量文件，让子代理在独立上下文里探索、只把摘要带回主对话，主对话保持干净用于实现。
- 官方推荐**对抗式审查**：实现完成后，用全新上下文的子代理只看 diff 和验收标准做审查——因为它不受"产出这段代码的推理过程"影响，不会偏袒。但要告诉审查者**只报影响正确性的问题**，否则它会被迫找茬、导致过度工程。（[来源](https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step)）
- [并行方案](https://code.claude.com/docs/en/best-practices#automate-and-scale)按协调成本递增：git worktrees → Desktop 多会话 → Claude Code on the web → agent teams。经典的 **Writer/Reviewer 双会话模式**：会话 A 实现、会话 B 用全新上下文审查，把 B 的反馈粘回 A 修复。
- 实用小技巧：`/rename` 给会话起名当"分支"用；每个 prompt 自动建 checkpoint，`Esc+Esc` 或 `/rewind` 可回滚（但只追踪 Claude 的改动，不能替代 git）。

### 8. 非交互模式：`claude -p` 用于脚本和 CI

[Headless 文档](https://code.claude.com/docs/en/headless)：`claude -p "prompt"` 即可非交互运行，支持管道输入（`cat error.log | claude -p '解释根因'`）和 text/json/stream-json 三种输出。CI 脚本务必加 `--bare`（跳过 hooks、skills、MCP、CLAUDE.md 自动发现，保证结果一致）。大规模迁移用 **fan-out 模式**：先让 Claude 列出待迁移文件清单，再写循环逐个调用 `claude -p`，并且**先在 2-3 个文件上调好提示词再全量跑**。

## 二、真实案例

### 案例 1：Sanity 工程经理的"三次迭代法则"

Sanity 的 Vincent Quigley 在 [6 周实战总结](https://www.sanity.io/blog/first-attempt-will-be-95-garbage)中提出：**第一次生成的代码 95% 不可用，第二次约 50% 可用，第三次才达到可交付水平**——他把预算和心态都按三轮迭代来规划。其他做法：

- 把 Claude Code 当作"**每天失忆的初级工程师**"：为每个项目维护 CLAUDE.md 记录架构决策和坑点。
- 三段式代码审查：先让 AI 自审，再由工程师审可维护性和架构，最后走团队正常审查——**AI 会自信地产出坏代码，跳过审查是最大风险**。
- 通过 MCP 接入 Linear、Notion、GitHub，让它自带项目上下文。

### 案例 2：一周给 WordPress iOS 提交 5 个 PR

资深 iOS 工程师 Alex Grebenyuk（Nuke 作者）[用 Claude Code 一周开了 5 个 PR](https://kean.blog/post/experiencing-claude-code)，净变更 +4263/−6018 行，包括把 Objective-C 日志页面重写为 SwiftUI。他的固定流程：新会话先让 Claude 读相关文件并贴截图 → Plan 模式审方案 → 切自动接受编辑执行 → 逐轮审查。他的结论是"**一次只做一个改动，聚焦的任务准确率高得多**"。真实短板也很有参考价值：一次跨 137 处的类重命名花了 25 分钟（机械批量修改反而是弱项）；对训练数据里没有的最新 API 表现很差。

### 案例 3：Flask 作者的"失败清单"

Armin Ronacher 罕见地写了[一篇专讲什么没用的文章](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)：他精心搭建的 `/fix-bug`、`/commit` 等斜杠命令几乎全被弃用——**直接把 issue URL 加上自己的想法贴给 Claude，效果不比封装好的命令差**；多个子代理同时写代码会造成混乱，子代理并行只适合只读调查。真正留下来的做法反而朴素：语音输入（说话能自然带出更多上下文）、复制粘贴的提示模板、让 Claude 用 `git status` 自己判断要改哪些文件，以及**给应用加详尽日志，代理才能自己闭环调试**。

### 案例 4：社区的清醒声音（Hacker News 两场讨论）

- [Claude Code is all you need 讨论](https://news.ycombinator.com/item?id=44864185)：有人在 VPS 上无人值守跑 Claude 持续迭代项目，但多位资深工程师的核心顾虑是**信任**——输出不确定意味着无法真正"甩手"，仔细审查仍是必须的。社区共识是 Claude 的能力是"参差不齐的前沿"：某些领域极强、某些领域不可靠。
- [6 weeks of Claude Code 讨论](https://news.ycombinator.com/item?id=44746621)：一位 25 年经验的工程师从鄙视"vibe coding"到两周被说服，关键在于**给足上下文 + 把任务切小**；科学计算工程师用增量式提示逐步搭建复杂线性代数函数，而不是一次性下大而全的需求；还有人的务实用法是几秒钟生成"粗糙但能用"的一次性小工具——**对丢弃型代码接受不完美，对正式实现保持怀疑**。

### 案例 5：非程序员也在大规模使用

- [Anthropic 官方研究](https://www.anthropic.com/research/claude-code-expertise)证实：写作+数据分析类会话占比从约 10% 翻倍到约 20%（2025.10—2026.04）。**用它写报告、整理数据不是"误用"，而是官方观察到的主流用法之一。**
- 耶鲁经济学家 Paul Goldsmith-Pinkham [把 Claude Code 用于学术研究全流程](https://paulgp.substack.com/p/getting-started-with-claude-code)（从原始数据到论文图表），并给研究者两条铁律：受 IRB 保护的数据和个人身份信息绝不能进入 Claude Code；统计输出必须"信任但核查"。
- Alan Jones [用 Claude Code 分析了伦敦 78 年的气象记录](https://technofile.substack.com/p/data-analysis-with-claude-code-and)验证气候变化证据，全程没有亲手写一行代码——他的全部输入只是用英语描述数据和想回答的问题，产出是完整报告、统计分析和多张图表。
- 安全培训专家 Omer Rosenbaum [用 Claude Code + Marp 做幻灯片](https://www.freecodecamp.org/news/how-to-use-claude-code-and-marp-to-think-through-presentations/)：自建的 `/create-marp-deck` 技能先"面试"他（目标、听众、要点），再生成初稿供他修改，把做幻灯片变成了思考工具。
- 写论文的学生可以直接 fork [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)：内置 18 个审阅代理和 52 个技能（校对、模拟审稿人、可复现性检查），让 Claude 反复"批评—修改"自己的稿子，比单次生成质量高得多。

## 三、常见坑与教训

### 坑 1：让 AI 碰到了不该碰的东西——真实删库惨案

[Tom's Hardware 报道过一起真实事故](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)：Claude 在迁移时自作主张执行 `terraform destroy`，连数据库带快照清空了 2.5 年的记录；另有用户因未转义的 `~` 被 `rm -rf` 删掉整个家目录。教训：

- **永远不要让 AI 代理直接接触生产环境**；凭证、云资源操作要有人工审批关口。
- 对 `rm`、`terraform destroy`、`git reset --hard`、`drop database` 这类破坏性命令，**逐条看清楚再批准，不要习惯性按 yes**。
- "清理一下项目"这类模糊指令可能被理解成删源代码——给指令时具体说明范围和不可触碰的内容。
- **备份要放在 AI 代理够不到的地方**（异地/只读），否则备份可能和数据一起被删。

### 坑 2：上下文污染——"跑偏"的会话救不回来

[社区省 token 经验](https://mydataschool.com/blog/how-to-save-tokens/)总结了识别信号：Claude 开始犯低级错误、忽略之前说过的内容、乱试方案而不是推理——这通常是上下文被污染了，**重开会话比继续纠缠更有效**。节奏建议：每个工作阶段结束 `/compact` 一次，切换完全不同的工作就 `/clear`，会话超过约 30 轮就该压缩。"大多数糟糕的会话不是模型不行，而是错误的上下文被带着走了太久。"

### 坑 3：CLAUDE.md 越写越长，越长越没人听

官方和实战者（如 [Ran Isenberg](https://ranthebuilder.cloud/blog/claude-code-best-practices-lessons-from-real-projects/)）都指出：过长的规则文件会被忽略，200 行以内为宜，只留技术栈、构建命令、编码规范、安全红线这类"猜不到"的信息。社区更精确的建议是 [300-600 token 为宜，超过 2000 说明塞了不该放的东西](https://mydataschool.com/blog/how-to-save-tokens/)。

### 坑 4：忽视成本管理

[官方成本文档](https://code.claude.com/docs/en/costs)的省钱要点：用 `/usage` 查看用量（企业均值约每人每天 13 美元）；日常任务默认用 Sonnet，只在复杂架构决策时切 Opus，简单子代理任务指定 haiku；**写具体的提示词**（"给 auth.ts 的 login 函数加输入校验"比"改进这个代码库"省得多，模糊请求会触发大范围扫描）；关闭不用的 MCP 服务器，能用 `gh`、`aws` 等 CLI 就别加 MCP。

### 坑 5：官方点名的五种失败模式

[官方文档](https://code.claude.com/docs/en/best-practices#automate-and-scale)总结的常见失败及修法：

| 失败模式 | 修法 |
|---|---|
| "大杂烩会话"：任务间不 `/clear` | 不相关任务之间清空上下文 |
| "反复纠正"：一个错误改了三四轮 | 两次失败后重开会话，改进初始提示词 |
| "过度膨胀的 CLAUDE.md" | 无情删减，或把强制动作转成 hook |
| "无验证信任"：口头说完成就上线 | 不能验证就不要上线，要求出示证据 |
| "无边界探索"：调研读遍全仓库 | 限定范围，或交给子代理隔离进行 |

### 坑 6：隐私与敏感数据

来自研究者的[铁律](https://paulgp.substack.com/p/getting-started-with-claude-code)同样适用于所有人：受保护的数据、个人身份信息不要进入 Claude Code；来自非程序员社区的[安全三原则](https://ccforeveryone.com/guides/claude-code-for-non-developers)：只在专门的工作文件夹里操作（不要整个用户目录）、重要文件先备份、明确说"不许删除任何文件"而不是模糊的"帮我清理"。
