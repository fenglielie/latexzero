# LaTeX Templates for Mathematical Notes

Simple LaTeX templates designed for mathematical notes.

> Tested on Overleaf with TeX Live 2022/2023/2024.

## Note

Styles:

- `note-setup` = `note-setup-box`
- `note-setup-simple`
- `note-setup-box` (tcolorbox)
- `note-setup-leftsidebox` (tcolorbox)
- `note-setup-borderless` (tcolorbox)
- `note-setup-mdframed` (mdframed, legacy)

**note-setup-simple**

<img src="assets/note-setup-simple-demo.png" alt="note-setup-simple-demo"/>

**note-setup-box**

<img src="assets/note-setup-box-demo.png" alt="note-setup-box-demo"/>

**note-setup-leftsidebox**

<img src="assets/note-setup-leftsidebox-demo.png" alt="note-setup-leftsidebox-demo"/>

**note-setup-borderless**

<img src="assets/note-setup-borderless-demo.png" alt="note-setup-borderless-demo"/>


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

**beamer-setup**

<p align="center">
    <img src="assets/beamer-setup-demo.png" alt="beamer-setup-demo" width="80%"/>
</p>

**beamer-setup-plain**

<p align="center">
    <img src="assets/beamer-setup-plain-demo.png" alt="beamer-setup-plain-demo" width="80%"/>
</p>


Usage:
```latex
\documentclass[compress,aspectratio=169]{beamer}
\input{/path/to/beamer-setup}

...
```
