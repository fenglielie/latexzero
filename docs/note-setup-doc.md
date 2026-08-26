# note-setup Documentation

This document explains the default [`note-setup.tex`](../note/note-setup.tex). The other setup files keep the same packages, commands, and theorem environments, but change their presentation: `attached` uses attached theorem titles, `leftbar` uses a colored left border, `shaded` removes visible borders, and `plain` does not depend on tcolorbox. The experimental `dark` setup uses a dark color scheme.

## Basic Configuration

Import commonly used base packages.
```latex
\usepackage{amsmath,amsthm,amssymb}
\usepackage{mathtools}
\usepackage{mathrsfs}
\usepackage{bm}
\usepackage{extarrows}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{float}
\usepackage{indentfirst}
\usepackage{booktabs,multirow}
\usepackage[shortlabels,inline]{enumitem}
\usepackage{appendix}
```

Import color-related packages.
```latex
\usepackage[dvipsnames]{xcolor}
```

Import packages for images and subfigures, and configure image search paths.
```latex
\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}
    {./graphics/}{./picture/}{./pictures/}
}
\usepackage{subcaption}
```

Import the package for algorithm environments.
```latex
\usepackage[ruled,linesnumbered,noline]{algorithm2e}
```

Import the package for code blocks and configure its style.
```latex
\usepackage{listings}
\lstdefinestyle{simpleStyle}{
    basicstyle=\ttfamily\small,
    breaklines=true,
    keywordstyle=\color{blue},
    identifierstyle=\color{black},
    stringstyle=\color{violet},
    commentstyle=\color[RGB]{34,139,34},
    showstringspaces=false,
    numbers=left,
    numbersep=2em,
    numberstyle=\footnotesize,
    frame=single,
    framesep=1em,
}
\lstset{style=simpleStyle}
```

Import the hyperlink package.
```latex
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,linkcolor=,urlcolor=cyan
}
```


## Theorem Environments

Change the title of the `proof` environment to `Proof` and set it in bold upright text.
```latex
\renewcommand*{\proofname}{\normalfont\bfseries Proof}
```

Import `tcolorbox` before `keytheorems`. The default setup uses the native
keytheorems–tcolorbox integration instead of wrapping theorem environments after
they are defined.
```latex
\usepackage[most]{tcolorbox}
\usepackage{keytheorems}
\usepackage{pifont}
```

The `\newkeytheorem` options used here include:

- `style`: theorem style; built-in `amsthm` styles include
  - plain (default): upright heading, italic body
  - definition: upright heading and upright body
  - remark: italic heading and upright body
- `name`: the printed heading shown in the document body
- `numbered`: whether numbering is enabled
- `parent`, `sibling`: numbering rules, for example
  - `parent=section`: number within `section`
  - `sibling=theorem`: share the counter with `theorem`
- `tcolorbox-no-titlebar`: apply tcolorbox options while keeping the theorem
  heading in the box body

The shared box geometry is defined once. Numbered environments use sharp
corners, while unnumbered environments use the rounded variant.
```latex
\tcbset{
    theorem box/.style={
            enhanced,
            breakable,
            sharp corners,
            boxrule=1pt,
        },
    theorem box rounded/.style={
            theorem box,
            rounded corners,
        }
}
```


Specifically:

- Use the `plain` style to define `theorem` / `theorem*`, `proposition` / `proposition*`, `corollary` / `corollary*`, `lemma` / `lemma*`, and `claim` / `claim*`
```latex
%% define environments

\newkeytheorem{theorem}[style=plain, name=Theorem, numbered=true, parent=section,
    tcolorbox-no-titlebar={theorem box, colframe=RoyalPurple, colback=RoyalPurple!8}]
\newkeytheorem{theorem*}[style=plain, name=Theorem, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=RoyalPurple, colback=RoyalPurple!8}]

\newkeytheorem{proposition}[style=plain, name=Proposition, numbered=true, sibling=theorem,
    tcolorbox-no-titlebar={theorem box, colframe=RoyalPurple, colback=RoyalPurple!8}]
\newkeytheorem{proposition*}[style=plain, name=Proposition, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=RoyalPurple, colback=RoyalPurple!8}]

\newkeytheorem{corollary}[style=plain, name=Corollary, numbered=true, sibling=theorem,
    tcolorbox-no-titlebar={theorem box, colframe=NavyBlue, colback=SkyBlue!8}]
\newkeytheorem{corollary*}[style=plain, name=Corollary, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=NavyBlue, colback=SkyBlue!8}]

\newkeytheorem{lemma}[style=plain, name=Lemma, numbered=true, sibling=theorem,
    tcolorbox-no-titlebar={theorem box, colframe=NavyBlue, colback=SkyBlue!8}]
\newkeytheorem{lemma*}[style=plain, name=Lemma, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=NavyBlue, colback=SkyBlue!8}]

\newkeytheorem{claim}[style=plain, name=Claim, numbered=true, sibling=theorem,
    tcolorbox-no-titlebar={theorem box, colframe=NavyBlue, colback=SkyBlue!8}]
\newkeytheorem{claim*}[style=plain, name=Claim, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=NavyBlue, colback=SkyBlue!8}]
```
- Use the `definition` style to define `definition` / `definition*`, `example` / `example*`, and `problem` / `problem*`
```latex
\newkeytheorem{definition}[style=definition, name=Definition, numbered=true, parent=section,
    tcolorbox-no-titlebar={theorem box, colframe=ForestGreen, colback=ForestGreen!5}]
\newkeytheorem{definition*}[style=definition, name=Definition, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=ForestGreen, colback=ForestGreen!5}]

\newkeytheorem{example}[style=definition, name=Example, numbered=true, parent=section,
    tcolorbox-no-titlebar={theorem box, colframe=RawSienna, colback=RawSienna!5}]
\newkeytheorem{example*}[style=definition, name=Example, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=RawSienna, colback=RawSienna!5}]

\newkeytheorem{problem}[style=definition, name=Problem, numbered=true, parent=section,
    tcolorbox-no-titlebar={theorem box, colframe=WildStrawberry!30, colback=WildStrawberry!5}]
\newkeytheorem{problem*}[style=definition, name=Problem, numbered=false,
    tcolorbox-no-titlebar={theorem box rounded, colframe=WildStrawberry!30, colback=WildStrawberry!5}]
```
- Use the standard `remark` typography: an italic heading and upright body, without a box
```latex
\newkeytheorem{remark}[style=remark, name=Remark, numbered=true, parent=section]
\newkeytheorem{remark*}[style=remark, name=Remark, numbered=false]
```
- Define a zero-width handwritten marker in the left margin, then use `\newkeytheoremstyle` for a bold orange heading, upright body, and matching end marker
```latex
\newcommand{\notehandmark}{\llap{\raisebox{0.05ex}{\large\ding{45}}\hspace{0.6em}}}
\newkeytheoremstyle{notestyle}{headfont=\color{orange!80!black}\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\color{orange!80!black}\diamond}}
```
- Use the custom `notestyle` to define `note` / `note*`; the marker uses no horizontal space, so the body keeps the normal text width and indentation
```latex
\newkeytheorem{note}[style=notestyle, name={\notehandmark Note}, numbered=true, parent=section]
\newkeytheorem{note*}[style=notestyle, name={\notehandmark Note}, numbered=false]
```
- The `plain` setup and `style=plain` package option keep the same marker and
  end symbol but omit their color to preserve the minimal style.
- Use `\newkeytheoremstyle` to define a new `solutionstyle`, similar to `proof`, but with the heading changed to `Solution`
```latex
\newkeytheoremstyle{solutionstyle}{headfont=\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\square}}
```
- Use the custom `solutionstyle` to define `solution` / `solution*`
```latex
\newkeytheorem{solution}[style=solutionstyle, name=Solution, numbered=true, parent=section]
\newkeytheorem{solution*}[style=solutionstyle, name=Solution, numbered=false]
```

## Theorem Styling

The box configuration is attached directly to each `\newkeytheorem`
declaration. This keeps the theorem definition, numbering, and visual style in
one place. The main tcolorbox parameters are `colframe` for the frame color and
`colback` for the background color. `enhanced` enables advanced box features,
`breakable` permits page breaks, and `boxrule=1pt` sets the frame width.

The `leftbar` and `shaded` setup files reuse the same environment declarations
with different shared box geometry. The `attached` setup instead uses the
keytheorems `tcolorbox` key so the theorem heading becomes the box title.

The colors are as follows:

|          Environment          |    Frame Color    | Background Color |
| :---------------------------: | :---------------: | :--------------: |
|   `theorem`, `proposition`    |    RoyalPurple    |  RoyalPurple!8   |
| `corollary`, `lemma`, `claim` |     NavyBlue      |    SkyBlue!8     |
|         `definition`          |    ForestGreen    |  ForestGreen!5   |
|           `example`           |     RawSienna     |   RawSienna!5    |
|           `problem`           | WildStrawberry!30 | WildStrawberry!5 |

Notes:

- The standard colors provided by `xcolor` are used here. `xxx!n` means mixing color `xxx` with white at a ratio of `n%`.
- To avoid too many colors, environments with similar semantics share the same box colors.

## Custom Cover Page

Define a custom cover page, inspired by [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook):
```latex
%% cover
\usepackage{titling}
\newcommand{\extrainfo}{}
\renewcommand{\extrainfo}[1]{\renewcommand{\extrainfocontent}{#1}}
\newcommand{\extrainfocontent}{}
\newcommand{\makecover}[1]{%
    \begin{titlepage}
        \newgeometry{margin=0in}
        \parindent=0pt
        \includegraphics[width=\linewidth]{#1} % size = 1280*1024
        \vfill
        \begin{center}
            \parbox{0.618\textwidth}{%
                \raggedleft{\bfseries \Huge \thetitle} \\[0.6pt]
                \rule{0.618\textwidth}{4pt} \\
            }
        \end{center}
        \vfill
        \begin{center}
            \parbox{0.618\textwidth}{%
                \raggedleft\Large
                \begin{tabular}{r}
                    \theauthor \\
                    \thedate   \\
                \end{tabular}%
            }
        \end{center}
        \vfill
        \begin{center}
            \parbox[t]{0.7\textwidth}{\centering \itshape \extrainfocontent}
        \end{center}
        \vfill
    \end{titlepage}
    \restoregeometry
    \thispagestyle{empty}
}
% USAGE
% \extrainfo{xxx}
% \makecover{/path/to/cover.png}
```

Instead of overriding `\maketitle`, this defines a new `\makecover` command that takes the cover image path as a required argument.

The original cover image uses a `1280 × 1024` aspect ratio. Other image sizes
also compile, but their aspect ratio changes the vertical space occupied by the
image and may require layout adjustments.

## Legacy `cbox` Compatibility

The templates no longer define the custom `cbox` environment. Documents that
still use it can add the following snippet directly to the main document
preamble, after loading a setup file or the `latexzero-note` package and before
`\begin{document}`.

```latex
\usepackage[most]{tcolorbox}

\newtcolorbox{cbox}[1][]{%
    enhanced,
    breakable,
    sharp corners,
    leftrule=2pt, rightrule=0pt, toprule=0pt, bottomrule=0pt,
    colframe=SkyBlue,
    colback=SkyBlue!8,
    #1
}
```
