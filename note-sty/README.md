# 📦 latexzero-note

## 🚀 Usage

Download [`latexzero-note.sty`](./latexzero-note.sty) to the same directory as
your document and select a style with the `style` option. See
[`main.tex`](./main.tex) for a complete example.

```latex
\documentclass{article}
\usepackage[style=attached]{latexzero-note}

\begin{document}

...

\end{document}
```

## 🎨 Available styles

- `default`: colored borders and lightly tinted
  backgrounds; used when the `style` option is omitted.
- `attached`: derived from `default`, with
  attached title labels.
- `leftbar`: colored left bars and lightly
  tinted backgrounds.
- `shaded`: borderless boxes with lightly
  tinted backgrounds.
- `plain`: the standard theorem layout without
  a dependency on tcolorbox.
