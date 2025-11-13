# LaTeX Templates for Mathematical Notes

Simple LaTeX templates designed for mathematical notes.

> Tested on Overleaf with TeX Live 2022/2023/2024.

## How to use it?

1. Clone or download the repo, or you can just download the relevant file(s),  such as [note-setup.tex](./note/note-setup.tex)

2. input setup file to the preamble of your document.
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

Styles:

- `note-setup` = `note-setup-box`
- `note-setup-simple`
- `note-setup-box` (tcolorbox)
- `note-setup-leftsidebox` (tcolorbox)
- `note-setup-borderless` (tcolorbox)
- `note-setup-dark` (tcolorbox)
- `note-setup-mdframed` (mdframed, legacy)

**note-setup-simple**

<img src="assets/note-setup-simple-demo.png" alt="note-setup-simple-demo"/>

**note-setup-box**

<img src="assets/note-setup-box-demo.png" alt="note-setup-box-demo"/>

**note-setup-leftsidebox**

<img src="assets/note-setup-leftsidebox-demo.png" alt="note-setup-leftsidebox-demo"/>

**note-setup-borderless**

<img src="assets/note-setup-borderless-demo.png" alt="note-setup-borderless-demo"/>

**note-setup-dark**

<img src="assets/note-setup-dark-demo.png" alt="note-setup-dark-demo"/>

Environments:

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


Usage:
```latex
\documentclass{article}
\input{/path/to/note-setup}

...
```

Add cover page (`\makecover`)

<img src="assets/note-cover-demo.png" alt="note-cover-demo"/>


## Beamer

Styles:

- `beamer-setup`
- `beamer-setup-plain`
- `beamer-setup-console` (inspired by [kmbeamer](https://github.com/kmaed/kmbeamer))

**beamer-setup**

<p align="center">
    <img src="assets/beamer-setup-demo.png" alt="beamer-setup-demo"/>
</p>

**beamer-setup-plain**

<p align="center">
    <img src="assets/beamer-setup-plain-demo.png" alt="beamer-setup-plain-demo"/>
</p>

**beamer-setup-console**

<p align="center">
    <img src="assets/beamer-setup-console-demo.png" alt="beamer-setup-console-demo"/>
</p>

Usage:
```latex
\documentclass[compress,aspectratio=169]{beamer}
\input{/path/to/beamer-setup}

...
```
