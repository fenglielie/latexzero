# LaTeX Templates for Mathematical Notes

English | [简体中文](./README.zh-CN.md)

Simple LaTeX templates for mathematical notes and Beamer slides.

> Tested on Overleaf with TeX Live 2022, 2023, and 2024.

> Github page: https://fenglielie.github.io/latexzero/

## Overview

- Templates for mathematical notes and Beamer slides
- Multiple note and presentation styles with preview images
- Suitable for Overleaf and local TeX Live workflows

## Table of Contents

- [How to use it?](#how-to-use-it)
- [Note](#note)
- [Beamer](#beamer)
- [More](#more)

## How to use it?

1. Clone or download this repository, or simply download the file(s) you need, such as [note-setup.tex](./note/note-setup.tex).

2. Input the setup file in the preamble of your document.

Usage example:
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


## Note

### Available styles

All note styles share the same commands and environments, so you can switch between them directly by changing the setup file.

- `note-setup` = `note-setup-box`
- `note-setup-simple`
- `note-setup-box` (tcolorbox)
- `note-setup-leftsidebox` (tcolorbox)
- `note-setup-borderless` (tcolorbox)
- `note-setup-dark` (tcolorbox, experimental; may have issues in practical use)
- `note-setup-mdframed` (mdframed, legacy)

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

### Supported environments

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


### Usage
```latex
\documentclass{article}
\input{/path/to/note-setup}

...
```

### Cover page

To add a cover page, use `\makecover`.

![note-cover-demo](assets/note-cover-demo.png)


## Beamer

### Available styles

All Beamer styles share the same commands and structure, so you can switch between them directly by changing the setup file.

- `beamer-setup`
- `beamer-setup-plain`
- `beamer-setup-console` (inspired by [kmbeamer](https://github.com/kmaed/kmbeamer))

**beamer-setup**

![beamer-setup-demo](assets/beamer-setup-demo.png)

**beamer-setup-plain**

![beamer-setup-plain-demo](assets/beamer-setup-plain-demo.png)

**beamer-setup-console**

![beamer-setup-console-demo](assets/beamer-setup-console-demo.png)

### Usage
```latex
\documentclass[compress,aspectratio=169]{beamer}
\input{/path/to/beamer-setup}

...
```

## More

- The repository also includes a `lab-report` template under [`lab-report/`](./lab-report/).
- The repository also includes a usable VS Code LaTeX Workshop configuration in [`.vscode/settings.json`](./.vscode/settings.json).
