# 不同任务类型的 Prompt 经验

> 好提示词的共同点：具体、可验证、给足上下文。下面按任务类型给出可以直接照抄或套用的模式，每条附"为什么有效"。

## 一、编程

### 模式 1：从"模糊求助"改写成"文件 + 场景 + 验证步骤"

[官方 Before/After 示例](https://code.claude.com/docs/en/best-practices)：

- 差：`fix the login bug`（修一下登录 bug）
- 好：`users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it`（用户反馈会话超时后登录失败。检查 src/auth/ 的鉴权流程，尤其是 token 刷新。先写一个能复现问题的失败测试，再修复它。）

**为什么有效**：指定了文件范围、触发场景和"先复现再修"的验证顺序，Claude 不必大范围扫描猜测，且修复有测试兜底。

### 模式 2：指向代码库里的既有范式

[官方示例](https://code.claude.com/docs/en/best-practices)：`look at how existing widgets are implemented on the home page. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget`（看看首页现有组件怎么实现的，HotDogWidget.php 是个好例子，照这个模式实现一个日历组件。）

**为什么有效**：与其凭空描述风格要求，不如给一个真实样板——Claude 模仿现成代码比理解抽象描述准确得多。[Simon Willison 的经验](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)同理：把几个相关的现成例子贴进去，然后说 "use them as inspiration"。

### 模式 3：内置可运行的验证目标

[官方示例](https://code.claude.com/docs/en/best-practices)：不要说 "implement a function that validates email addresses"，而要说 `write a validateEmail function. example test cases: user@example.com is true, invalid is false. run the tests after implementing`（写一个 validateEmail 函数。测试样例：user@example.com 为真，invalid 为假。实现后运行测试。）

**为什么有效**：给了 Claude 自己能跑的判分标准，它可以迭代到通过为止，把"看起来完成"变成"检查通过才算完成"。进阶版是 [TDD 提示](https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/)："用 TDD 实现 X：先写一个会失败的测试并运行确认它失败，贴出失败输出，然后再写最小实现"——必须真的看到红色才能写代码，防止代理幻觉测试结果。

### 模式 4：大功能先"被面试"，产出 spec 再执行

[官方模板](https://code.claude.com/docs/en/best-practices)：`I want to build [X]. Interview me in detail using the AskUserQuestion tool... Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.` [Harper Reed 的变体](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)：`Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea.` 之后开新会话干净地执行 spec。

**为什么有效**：一次只问一个问题，逼你把没想清楚的需求想清楚；spec 落成文件后，执行会话不必背负讨论过程的全部上下文。整个流程约 15 分钟，但能防止代理在大任务上跑偏。

## 二、写作与文档

### 模式 1：先讨论、后产出的"思考伙伴"式提示

来自 [Department of Product 的非工程用法](https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering)：不要一上来就说"写一份 PRD"，而是先和它讨论思路、让它读你的资料文件夹，再让它产出需求文档和任务工单。

**为什么有效**：把 Claude Code 当思考伙伴而非生成器，产出会基于你的真实材料而不是通用模板。

### 模式 2：访谈式收敛 + 汇总成文

[Harper Reed 的两段式](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)：先 `Ask me one question at a time...`（一次问我一个问题，把这个想法打磨成详尽的分步规格），结束后 `compile our findings into a comprehensive, developer-ready specification`（把我们的讨论汇总成一份完整的规格文档）。

**为什么有效**：写作最难的是把脑中的模糊想法externalize——让 AI 提问比让你自己空想更快抵达结构。

### 模式 3：让 Claude 反复"批评—修改"自己的稿子

来自[学术写作模板仓库](https://github.com/pedrohcgs/claude-code-my-workflow)：用 `/review-paper` 模拟同行评审，让审阅代理走"实现→验证→审查→修复"循环，直到质量达标。

**为什么有效**：单次生成的初稿质量有限，多轮对抗式自审能系统性抬高下限——这也是该仓库内置 18 个审阅代理的原因。

## 三、研究与数据

### 模式 1：用自然语言描述"数据 + 想回答的问题"

[Alan Jones 分析伦敦 78 年气象记录](https://technofile.substack.com/p/data-analysis-with-claude-code-and)的全部输入，就是用英语描述数据是什么、想回答什么问题——产出是完整的书面报告、统计分析和多张图表，全程没写一行代码。

**为什么有效**：把 Claude Code 当"会执行的分析师"而非"代码生成器"，你的核心技能从编程变成了清晰地描述数据和提问。

### 模式 2：多来源对照综述，要求注明出处

可照抄的提示词（[CC for Everyone](https://ccforeveryone.com/guides/claude-code-for-non-developers)）："读完这个文件夹里的所有资料，写一个 compare.md：差异对照表、每个来源的观点、证据倾向哪边，并注明出处文件名。"

**为什么有效**：指定了输出文件、结构（对照表）和溯源要求，结论可以逐条核查而不是一团模糊的总结。

### 模式 3："信任但核查"+ 主动管理上下文

[耶鲁经济学家 Paul Goldsmith-Pinkham 的经验](https://paulgp.substack.com/p/getting-started-with-claude-code)：统计方法的输出必须亲自核查关键数字；读的文件越多、对话越长，输出质量下降越明显，要主动 `/compact` 而不是被动等它塞满。另一条铁律：受 IRB 保护的数据和个人身份信息绝不进入 Claude Code。

**为什么有效**：研究场景里错误代价高，上下文窗口是"隐形杀手"——提示词再好，也救不了被污染的长会话。

## 四、幻灯片与排版

### 模式 1：先"面试"再出初稿

[Omer Rosenbaum 的 Marp 工作流](https://www.freecodecamp.org/news/how-to-use-claude-code-and-marp-to-think-through-presentations/)：他的 `/create-marp-deck` 技能先问他目标、听众、要点，再生成 Marp Markdown 初稿供他反应和修改。

**为什么有效**：幻灯片最难的是叙事结构，不是排版——先被提问逼着想清楚"讲给谁、讲什么"，初稿才不会跑偏；Markdown 幻灯片的强约束还逼你精简表达。

### 模式 2：对话级微调版式

同一来源的迭代方式："第 6 页太密了，把算法对比拆成两页"、"给第一页加一个『为什么选令牌桶』的标注"。

**为什么有效**：用自然语言直接指挥改版式，比在 PPT 里手动拖拽快，且改动范围明确、可逐条验收；最终可一键导出 md/html/pptx 三种格式。

### 模式 3：用 LaTeX/Beamer 换取专业排版

[Towards Data Science 的技巧](https://towardsdatascience.com/how-to-apply-claude-code-to-non-technical-tasks/)：让 Claude Code 写 LaTeX/Beamer 代码生成 PDF 演示文稿，比让它直接做 PPT 更可控、排版更专业。写课件的还可以直接用 [claude-code-my-workflow 仓库](https://github.com/pedrohcgs/claude-code-my-workflow)的 `/create-lecture` 命令。

**为什么有效**：代码化的排版是 Claude 的强项——每处改动都是可审查的文本 diff，而不是黑盒的所见即所得操作。

### 模式 4：把历史作品放同一文件夹当风格参照

[同一来源](https://towardsdatascience.com/how-to-apply-claude-code-to-non-technical-tasks/)：把所有演示文稿放在一个文件夹里，Claude 能参考你以前的作品，自动保持公司模板和风格一致。

**为什么有效**：这是排版版的"指向既有范式"——给样板比描述风格准确得多。

## 五、日常自动化

### 模式 1：账单转报表，一句话搞定

可照抄的提示词（[Every.to](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required)）：下载信用卡账单 CSV 后说"**把上周的所有支出按类别整理成一个简单的网页报表**"，Claude 会自动生成可以直接打开的 HTML 页面。

**为什么有效**：说清输入（CSV）、处理方式（按类别）和输出形态（网页报表），Claude 自己补齐全部技术细节。配套习惯：为每类事务建专门文件夹（如"报销"），在其中启动 Claude Code，上下文干净又不会误读无关文件。

### 模式 2：批量整理文件——先出计划、明令禁删

可照抄的提示词（[CC for Everyone](https://ccforeveryone.com/guides/claude-code-for-non-developers)）："看看我桌面上的截图，根据每张图的内容重命名"；"提出一个按类型和年份分子文件夹的整理方案，**先给我看完整计划再动手，永远不要删除任何东西**"。

**为什么有效**："先计划后执行 + 明确禁删"给批量操作加了双保险——模糊的"帮我清理"可能被理解成删除，具体的边界指令不会。

### 模式 3：票据转结构化数据——允许"不确定"，禁止硬猜

可照抄的提示词（[同上](https://ccforeveryone.com/guides/claude-code-for-non-developers)）："读取每张收据，生成 expenses.csv，列为：日期、商家、金额、类别；**读不清的单独列出来，不要猜**。"

**为什么有效**：明确给了输出 schema，并给了 Claude 一个"承认不确定"的出口——否则它会为了完成任务而编造数字。

### 模式 4：养成"这事能不能让 Claude Code 做"的反射

[Towards Data Science 的建议](https://towardsdatascience.com/how-to-apply-claude-code-to-non-technical-tasks/)：遇到任何电脑上的重复劳动，先问自己"这件事能不能让 Claude Code 做"；配置好邮箱、Notion、云盘的访问权限后，一句话可以同时搜索多个平台；并且在旧项目基础上迭代，而不是每次从零开始。

**为什么有效**：自动化的最大门槛不是提示词技巧，而是想不起来用——而复用旧项目让每次的提示词越来越短。
