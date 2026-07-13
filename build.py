#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建「和 AI 一起用电脑」教学站（瑞士风 · 左侧边栏）。
输出：index.html 及各章节页至仓库根目录。
用法：python3 build.py
"""
import os, re, subprocess, html

BASE = os.path.dirname(os.path.abspath(__file__))

_P = ('<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
      'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{}</svg>')
ICONS = {
    "terminal": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3"/><path d="M13 15h4"/>',
    "cli": '<polyline points="5 8 9 12 5 16"/><line x1="12" y1="16" x2="19" y2="16"/>',
    "files": '<path d="M4 5a1 1 0 0 1 1-1h4l2 2h3a1 1 0 0 1 1 1v2"/><rect x="7" y="9" width="14" height="11" rx="1.5"/>',
    "package": '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5"/><path d="M12 12v9"/><path d="M12 12L4 7.5"/>',
    "spark": '<path d="M12 3l1.9 5.6L19.5 10l-5.6 1.4L12 17l-1.9-5.6L4.5 10l5.6-1.4z"/>',
    "hash": '<line x1="9" y1="4" x2="7" y2="20"/><line x1="17" y1="4" x2="15" y2="20"/><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/>',
    "doc": '<path d="M14 3v5h5"/><path d="M14 3H7a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V8z"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="13" y2="17"/>',
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "book": '<path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H19a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a2 2 0 0 0-2 2z"/><path d="M6 20a2 2 0 0 1-2-2"/>',
    "arrow": '<line x1="5" y1="12" x2="18" y2="12"/><polyline points="12 6 18 12 12 18"/>',
    "search": '<circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.6" y2="16.6"/>',
    "menu": '<line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/>',
    "logo": '<polyline points="6 8 10 12 6 16"/><line x1="12" y1="16" x2="18" y2="16"/>',
    "rocket": '<path d="M5 15l-1 5 5-1"/><path d="M9 14l-4 4"/><path d="M14 4c3 0 6 3 6 6-2 5-7 9-11 9l-4-4c0-4 4-9 9-11z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
    "windows": '<rect x="3" y="4" width="8" height="7"/><rect x="13" y="4" width="8" height="7"/><rect x="3" y="13" width="8" height="7"/><rect x="13" y="13" width="8" height="7"/>',
    "github": '<path d="M12 3a9 9 0 0 0-3 17.5c.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.2-3.4-1.2-.4-1.1-1-1.4-1-1.4-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.3 1 2.9.8.1-.6.3-1 .6-1.3-2.2-.3-4.6-1.1-4.6-5a3.8 3.8 0 0 1 1-2.7 3.6 3.6 0 0 1 .1-2.6s.8-.3 2.7 1a9.4 9.4 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1a3.6 3.6 0 0 1 .1 2.6 3.8 3.8 0 0 1 1 2.7c0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.8V20c0 .3.2.6.7.5A9 9 0 0 0 12 3z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18z"/>',
    "slides": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4"/><path d="M8 20h8"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-8 8H5l-2 2V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8z"/>',
    "star": '<path d="M12 3l2.7 5.8 6.3.7-4.7 4.3 1.3 6.2-5.6-3.2-5.6 3.2 1.3-6.2L3 9.5l6.3-.7z"/>',
    "list": '<line x1="9" y1="6" x2="20" y2="6"/><line x1="9" y1="12" x2="20" y2="12"/><line x1="9" y1="18" x2="20" y2="18"/><circle cx="5" cy="6" r="1"/><circle cx="5" cy="12" r="1"/><circle cx="5" cy="18" r="1"/>',
    "download": '<path d="M12 3v12"/><path d="M7 11l5 4 5-4"/><path d="M5 21h14"/>',
}
def icon(name):
    return _P.format(ICONS.get(name, ""))

# (文件id, 完整标题, 副标题, 图标, 侧栏简称)
LESSON1 = [
    ("topic1", "操作系统 & 终端", "为什么用 Mac、Unix/Linux/Windows 的关系、什么是命令行终端", "terminal", "操作系统 & 终端"),
    ("topic2", "命令行核心命令", "cd / ls / pwd / mkdir / rm / open、路径与快捷键，照着敲就会", "cli", "命令行核心命令"),
    ("topic3", "文件系统 & 组织", "用户目录、路径、iCloud 同步陷阱、项目组织与命名规范", "files", "文件系统 & 组织"),
    ("topic4", "Homebrew 包管理器", "命令行「应用商店」：安装、brew install、国内网络与镜像", "package", "Homebrew"),
    ("topic5", "Claude Code 初识", "能真正操作电脑的 AI：权限、token、模型与订阅计费", "spark", "Claude Code 初识"),
    ("topic6", "Markdown", "用纯文本优雅记笔记，也是和 AI 对话的原生语言", "hash", "Markdown"),
    ("topic7", "LaTeX & Overleaf", "专业排版与数学公式、用模板做简历、Overleaf 上手", "doc", "LaTeX & Overleaf"),
    ("topic8", "VS Code & Python", "编辑器上手、code 命令联动、写下第一个 Python 程序", "code", "VS Code & Python"),
]
LESSON2 = [
    ("c01-overview", "课程总览：一个下午三个网站", "今天实战的完整故事线：从注册 GitHub 到发布教学站", "book", "课程总览"),
    ("c02-mac-setup", "Mac 安装与配置", "Homebrew → git/gh/node → Claude Code 代理配置 → 启动参数详解", "spark", "Mac 安装配置"),
    ("c03-windows-setup", "Windows 方案（WSL2）", "一条命令装 Ubuntu，之后与 Mac 殊途同归；专属注意事项", "windows", "Windows 方案"),
    ("c04-github-gh", "GitHub 与 gh 命令行", "账号、仓库、gh auth login 全流程、git 身份与隐私技巧", "github", "GitHub & gh"),
    ("c05-github-pages", "GitHub Pages 发布", "把文件夹变成网站：两种站点、两种开启方式、三个坑", "globe", "GitHub Pages"),
    ("c06-web-slides", "网页就是幻灯片", "为什么放弃 PPT、Slidev 路线、今天踩过的四个坑与质量纪律", "slides", "网页幻灯片"),
    ("c07-prompt-skills", "向 AI 提问的艺术", "从真实对话提炼的 9 个技巧，每条附当时的原话", "chat", "提问的艺术"),
    ("c08-best-practices", "实战案例与最佳实践", "联网调研：官方建议、真实案例、常见坑（来源可查）", "star", "案例与最佳实践"),
    ("c09-prompt-patterns", "分任务型 Prompt 经验", "编程 / 写作 / 研究 / 幻灯片 / 自动化，各任务型的提问模式", "list", "任务型 Prompt"),
    ("c10-cheatsheet", "命令速查表", "今天出现过的每一条命令，逐条人话解释", "cli", "命令速查表"),
    ("c11-prompts", "Prompt 模板库", "实战验证过的提示词模板，Markdown 原文可下载", "download", "Prompt 模板"),
]
ALL = LESSON1 + LESSON2
GROUPS = [("第一课 · 电脑基本功", LESSON1), ("第二课 · Claude Code 实战", LESSON2)]

def md_to_html(md_path):
    out = subprocess.run(["pandoc", md_path, "-f", "gfm", "-t", "html"],
                         capture_output=True, text=True, check=True)
    return out.stdout

def extract_toc(frag_html):
    items = []
    for m in re.finditer(r'<h([23]) id="([^"]+)">(.*?)</h[23]>', frag_html, re.S):
        lvl, hid, title = m.group(1), m.group(2), re.sub(r"<[^>]+>", "", m.group(3)).strip()
        items.append((lvl, hid, title))
    return items

def sidebar(active):
    groups_html = ""
    idx = 0
    for label, items in GROUPS:
        rows = ""
        for (tid, _t, _s, _ic, short) in items:
            idx += 1
            rows += (f'<a class="s-item{" active" if f"{tid}.html" == active else ""}" '
                     f'href="{tid}.html" data-name="{short}">'
                     f'<span class="s-num">{idx:02d}</span><span class="s-txt">{short}</span></a>')
        groups_html += f'<div class="s-group"><div class="s-label">{label}</div>{rows}</div>'
    home = (f'<a class="s-item{" active" if active == "index.html" else ""}" href="index.html">'
            f'<span class="s-ico">{icon("book")}</span><span class="s-txt">总览</span></a>')
    return f'''<aside class="sidebar" id="sidebar">
  <a class="s-brand" href="index.html"><span class="s-logo">{icon("logo")}</span><span class="s-name">和 AI 一起用电脑</span></a>
  <div class="s-search"><span class="s-search-ico">{icon("search")}</span><input id="navFilter" type="text" placeholder="筛选章节…" autocomplete="off"></div>
  <nav class="s-scroll">
    <div class="s-group">{home}</div>
    <div id="topicGroup">{groups_html}</div>
    <div class="s-empty" id="navEmpty" hidden>没有匹配的章节</div>
  </nav>
  <div class="s-foot">2026-07-13 实战课 · 综合笔记</div>
</aside>'''

def shell(title, active, body, extra_scripts=""):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="progress" id="progress"></div>
<div class="backdrop" id="backdrop"></div>
{sidebar(active)}
<div class="content">
  <div class="mtop">
    <button class="burger" id="burger" aria-label="菜单">{icon("menu")}</button>
    <a class="m-brand" href="index.html">和 AI 一起用电脑</a>
  </div>
  <div class="page">
{body}
  </div>
</div>
<script src="assets/nav.js"></script>
{extra_scripts}
</body>
</html>'''

def build_index():
    cards = ""
    for gi, (label, items) in enumerate(GROUPS, 1):
        rows = ""
        offset = 0 if gi == 1 else len(LESSON1)
        for i, (tid, ttl, sub, ic, short) in enumerate(items, 1):
            rows += f'''<a class="tl-item" href="{tid}.html">
  <span class="tl-ico">{icon(ic)}</span>
  <span class="tl-body"><span class="tl-kicker">{offset + i:02d}</span><h3>{ttl}</h3><p>{sub}</p></span>
  <span class="tl-arrow">{icon("arrow")}</span>
</a>'''
        cards += f'<div class="sec-head"><h2>{label}</h2><span class="cnt">{len(items)} 篇</span></div><div class="topic-list">{rows}</div>'

    body = f'''
<section class="hero">
  <div class="eyebrow">CLAUDE CODE · 实战课综合笔记 · 2026-07</div>
  <h1>和 AI 一起<br>用电脑</h1>
  <p class="lede">从命令行零基础，到用 Claude Code 建站、发布幻灯片、完成真实工作。全部内容来自两堂真实课程：第一课打基本功，第二课完整实战——一个下午，从注册 GitHub 到上线三个网站。</p>
  <div class="hero-links">
    <a class="qbtn primary" href="c01-overview.html">从总览开始 →</a>
    <a class="qbtn" href="c11-prompts.html">直接看 Prompt 模板</a>
  </div>
  <div class="stats">
    <div class="stat"><b>{len(ALL)}</b><span class="s-lab">章节</span></div>
    <div class="stat"><b>5</b><span class="s-lab">Prompt 模板</span></div>
    <div class="stat"><b>3</b><span class="s-lab">实战网站</span></div>
  </div>
</section>
{cards}
'''
    return shell("和 AI 一起用电脑 · 实战课综合笔记", "index.html", body)

def build_topic(pos, tid, ttl, sub, ic, frag):
    toc_items = extract_toc(frag)
    toc_html = ""
    if len(toc_items) >= 2:
        links = "\n".join(
            f'<a class="{"lvl3" if lvl == "3" else "lvl2"}" href="#{hid}">{html.escape(t)}</a>'
            for lvl, hid, t in toc_items)
        toc_html = f'<aside class="toc"><div class="t-title">本页目录</div>{links}</aside>'

    if pos == 0:
        prev_html = f'<a href="index.html"><span class="lab">← 上一篇</span><span class="ttl">返回总览</span></a>'
    else:
        p = ALL[pos - 1]
        prev_html = f'<a href="{p[0]}.html"><span class="lab">← 上一篇</span><span class="ttl">{p[1]}</span></a>'
    if pos == len(ALL) - 1:
        next_html = f'<a class="next" href="index.html"><span class="lab">下一篇 →</span><span class="ttl">返回总览</span></a>'
    else:
        n = ALL[pos + 1]
        next_html = f'<a class="next" href="{n[0]}.html"><span class="lab">下一篇 →</span><span class="ttl">{n[1]}</span></a>'

    lesson = "第一课" if pos < len(LESSON1) else "第二课"
    body = f'''
<div class="doc-head">
  <div class="crumb">{lesson} · {pos + 1:02d} / {len(ALL):02d}</div>
  <h1>{ttl}</h1>
  <p class="sub">{sub}</p>
</div>

<div class="doc-layout">
  <article class="article md">
{frag}
  </article>
  {toc_html}
</div>

<nav class="pager">
  {prev_html}
  {next_html}
</nav>
'''
    return shell(f"{ttl} · 和 AI 一起用电脑", f"{tid}.html", body, '<script src="assets/toc.js"></script>')

def build():
    pages = {"index.html": build_index()}
    ready = 0
    for pos, (tid, ttl, sub, ic, short) in enumerate(ALL):
        mdp = os.path.join(BASE, "content", f"{tid}.md")
        if os.path.exists(mdp):
            frag = md_to_html(mdp); ready += 1
        else:
            frag = "<p>（本节内容整理中）</p>"
        pages[f"{tid}.html"] = build_topic(pos, tid, ttl, sub, ic, frag)
    for name, content in pages.items():
        with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(f"chapters ready: {ready}/{len(ALL)} · pages written: {len(pages)}")

if __name__ == "__main__":
    build()
