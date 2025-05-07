# LaTeX Templates for Mathematical Notes

Simple LaTeX templates designed for mathematical notes.

## Note

Styles:

- `note-setup` = `note-setup-box`
- `note-setup-simple`
- `note-setup-box` (tcolorbox)
- `note-setup-leftsidebox` (tcolorbox)
- `note-setup-mframed` (mframed, legacy)

**note-setup-simple**

<img src="./note/image/note-setup-simple-demo.png" alt="note-setup-simple-demo"/>

**note-setup-box**

<img src="./note/image/note-setup-box-demo.png" alt="note-setup-box-demo"/>

**note-setup-leftsidebox**

<img src="./note/image/note-setup-leftsidebox-demo.png" alt="note-setup-leftsidebox-demo"/>


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


## Beamer

<p align="center">
    <img src="./beamer/image/beamer-demo-1.png" alt="beamer-demo-1" width="80%"/>
</p>

<p align="center">
    <img src="./beamer/image/beamer-demo-2.png" alt="beamer-demo-2" width="80%"/>
</p>

<p align="center">
    <img src="./beamer/image/beamer-demo-3.png" alt="beamer-demo-3" width="80%"/>
</p>

<p align="center">
    <img src="./beamer/image/beamer-demo-4.png" alt="beamer-demo-4" width="80%"/>
</p>


Usage:
```latex
\documentclass[compress,aspectratio=43]{beamer}
\input{/path/to/beamer-setup}

...
```
