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

- `note-setup`：默认样式，采用彩色边框和浅色背景。
- `note-setup-attached`：由 `note-setup` 派生，采用附着式标题。
- `note-setup-leftbar`：采用彩色左边线和浅色背景。
- `note-setup-shaded`：采用无边框的浅色背景。
- `note-setup-plain`：采用标准定理样式，不依赖 tcolorbox。
- `note-setup-dark`：采用深色页面和定理框，属于实验性样式。

**note-setup**

![note-setup-demo](assets/note-setup-demo.png)

**note-setup-attached**

![note-setup-attached-demo](assets/note-setup-attached-demo.png)

**note-setup-leftbar**

![note-setup-leftbar-demo](assets/note-setup-leftbar-demo.png)

**note-setup-shaded**

![note-setup-shaded-demo](assets/note-setup-shaded-demo.png)

**note-setup-plain**

![note-setup-plain-demo](assets/note-setup-plain-demo.png)

**note-setup-dark**

![note-setup-dark-demo](assets/note-setup-dark-demo.png)

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

- `beamer-setup`：默认样式，采用顶部导航栏和圆角标题页。
- `beamer-setup-minimal`：移除导航栏，并采用更加简洁的标题页。
- `beamer-setup-console`：采用深色终端风格，灵感来自 [kmbeamer](https://github.com/kmaed/kmbeamer)。

**beamer-setup**

![beamer-setup-titlepage](assets/beamer-titlepage.png)

![beamer-setup-demo](assets/beamer-setup-demo.png)

**beamer-setup-minimal**

![beamer-setup-minimal-titlepage](assets/beamer-titlepage-minimal.png)

![beamer-setup-minimal-demo](assets/beamer-setup-minimal-demo.png)

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
