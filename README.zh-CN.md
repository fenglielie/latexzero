# 数学笔记 LaTeX 模板

[English](./README.md) | 简体中文

适用于数学笔记与 Beamer 的简洁 LaTeX 模板。

> **Note 模板兼容性更新：** Note 模板已由 `thmtools` 迁移至 `keytheorems`，
> 以规避 [thmtools issue #75](https://github.com/muzimuzhi/thmtools/issues/75)
> 所述的 TeX Live 2026 共享计数器兼容性问题。基于 `thmtools` 的旧版 Note
> 模板（包括 `mdframed` 样式）保留在
> [`legacy/thmtools` 分支](https://github.com/fenglielie/latexzero/tree/legacy/thmtools)，
> 可用于 TeX Live 2025 及更早版本。

## 概览

- 提供数学笔记与 Beamer 模板
- 包含多种笔记和演示风格，并附带预览图
- 适用于 Overleaf 和本地 TeX Live 工作流

## 目录

- [数学笔记 LaTeX 模板](#数学笔记-latex-模板)
  - [概览](#概览)
  - [目录](#目录)
  - [如何使用？](#如何使用)
  - [Note](#note)
    - [可用样式](#可用样式)
    - [支持的环境](#支持的环境)
    - [用法](#用法)
    - [封面页](#封面页)
  - [Beamer](#beamer)
    - [可用样式](#可用样式-1)
    - [用法](#用法-1)
  - [补充](#补充)

## 如何使用？

1. 克隆或下载本仓库，或者只下载你需要的文件，例如 [note-setup.tex](./note/note-setup.tex)。

2. 在文档导言区通过 `\input` 引入对应的设置文件。

使用示例：
```latex
\documentclass{article}
\input{./note-setup}

\title{Title}
\author{Author}
\date{\today}

\begin{document}

\maketitle

\end{document}
```

本地编译时，纯英文 note 和 Beamer 文档可使用 `pdflatex`、`xelatex` 或 `lualatex`；包含中文或 CJK 混排时，推荐使用 `xelatex` 或 `lualatex`。

> **新功能：** Note 模板既可通过各个独立的 setup 文件直接使用，也提供了统一的 [sty 宏包版本](./note-sty/README.md)，便于通过选项切换样式。

## Note

### 可用样式

这些 note 样式共享同一套命令和环境定义，因此只需替换对应的 setup 文件即可直接切换。

- `note-setup` = `note-setup-box`
- `note-setup-simple`
- `note-setup-box` (tcolorbox)
- `note-setup-leftsidebox` (tcolorbox)
- `note-setup-borderless` (tcolorbox)
- `note-setup-dark` (tcolorbox，实验性样式，实际使用时可能存在一些问题)
- `note-setup-box-attach`（由 `note-setup-box` 派生，采用附着式标题）

**note-setup-simple**

![note-setup-simple-demo](assets/note-setup-simple-demo.png)

**note-setup-box**

![note-setup-box-demo](assets/note-setup-box-demo.png)

**note-setup-leftsidebox**

![note-setup-leftsidebox-demo](assets/note-setup-leftsidebox-demo.png)

**note-setup-borderless**

![note-setup-borderless-demo](assets/note-setup-borderless-demo.png)

**note-setup-dark**

![note-setup-dark-demo](assets/note-setup-dark-demo.png)

**note-setup-box-attach**

![note-setup-box-attach-demo](assets/note-setup-box-attach-demo.png)

### 支持的环境

| Environment                   | Style           | Numbering Rule              |
| ----------------------------- | --------------- | --------------------------- |
| `theorem`, `theorem*`         | plain           | within section              |
| `proposition`, `proposition*` | plain           | shares counter with theorem |
| `corollary`, `corollary*`     | plain           | shares counter with theorem |
| `lemma`, `lemma*`             | plain           | shares counter with theorem |
| `claim`, `claim*`             | plain           | shares counter with theorem |
| `definition`, `definition*`   | definition      | within section              |
| `example`, `example*`         | definition      | within section              |
| `problem`, `problem*`         | definition      | within section              |
| `remark`, `remark*`           | remark          | within section              |
| `note`, `note*`               | remark          | within section              |
| `solution`, `solution*`       | (solutionstyle) | within section              |


### 用法
```latex
\documentclass{article}
\input{/path/to/note-setup}

...
```

### 封面页

如需添加封面页，可使用 `\makecover`。

![note-cover-demo](assets/note-cover-demo.png)


## Beamer

### 可用样式

这些 Beamer 样式共享同一套命令和结构，因此只需替换对应的 setup 文件即可直接切换。

- `beamer-setup`
- `beamer-setup-plain`（无导航栏，封面更简洁）
- `beamer-setup-console`（灵感来自 [kmbeamer](https://github.com/kmaed/kmbeamer)）

**beamer-setup**

![beamer-setup-titlepage](assets/beamer-titlepage.png)

![beamer-setup-demo](assets/beamer-setup-demo.png)

**beamer-setup-plain**

![beamer-setup-plain-titlepage](assets/beamer-titlepage-plain.png)

![beamer-setup-plain-demo](assets/beamer-setup-plain-demo.png)

**beamer-setup-console**

![beamer-setup-console-titlepage](assets/beamer-titlepage-console.png)

![beamer-setup-console-demo](assets/beamer-setup-console-demo.png)

### 用法
```latex
\documentclass[compress,aspectratio=169]{beamer}
% \definecolor{simplebeamercolor}{RGB}{200,50,50}% 在 \input 前定义以自定义主题色
\input{/path/to/beamer-setup}

...
```

## 补充

- 仓库中还提供了一个位于 [`lab-report/`](./lab-report/) 下的 `lab-report` 模板。
- 仓库中还附带了一份可用的 VS Code LaTeX Workshop 配置，见 [`.vscode/settings.json`](./.vscode/settings.json)。
