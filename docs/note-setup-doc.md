# note-setup Documentation

## Basic Configuration

Import commonly used base packages.
```latex
\usepackage{amsmath,amsthm,amsfonts,amssymb}
\usepackage{mathtools}
\usepackage{mathrsfs}
\usepackage{bm}
\usepackage{extarrows}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{float}
\usepackage{indentfirst}
\usepackage{anyfontsize}
\usepackage{booktabs,multirow,multicol}
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

Import `thmtools` and use `\declaretheorem` to define theorem-like environments more conveniently than `\newtheorem`.
```latex
\usepackage{thmtools}
```

The `\declaretheorem` options used here include:

- `style`: theorem style; built-in `amsthm` styles include
  - plain (default): upright heading, italic body
  - definition: upright heading and upright body
  - remark: italic heading and upright body
- `name`: the printed heading shown in the document body
- `numbered`: whether numbering is enabled
- `numberwithin`, `sibling`: numbering rules, for example
  - `numberwithin=section`: number within `section`
  - `sibling=theorem`: share the counter with `theorem`


Specifically:

- Use the `plain` style to define `theorem` / `theorem*`, `proposition` / `proposition*`, `corollary` / `corollary*`, `lemma` / `lemma*`, and `claim` / `claim*`
```latex
%% define environments

\declaretheorem[style=plain, name=Theorem, numbered=yes, numberwithin=section]{theorem}
\declaretheorem[style=plain, name=Theorem, numbered=no]{theorem*}

\declaretheorem[style=plain, name=Proposition, numbered=yes, sibling=theorem]{proposition}
\declaretheorem[style=plain, name=Proposition, numbered=no]{proposition*}

\declaretheorem[style=plain, name=Corollary, numbered=yes, sibling=theorem]{corollary}
\declaretheorem[style=plain, name=Corollary, numbered=no]{corollary*}

\declaretheorem[style=plain, name=Lemma, numbered=yes, sibling=theorem]{lemma}
\declaretheorem[style=plain, name=Lemma, numbered=no]{lemma*}

\declaretheorem[style=plain, name=Claim, numbered=yes, sibling=theorem]{claim}
\declaretheorem[style=plain, name=Claim, numbered=no]{claim*}
```
- Use the `definition` style to define `definition` / `definition*`, `example` / `example*`, and `problem` / `problem*`
```latex
\declaretheorem[style=definition, name=Definition, numbered=yes, numberwithin=section]{definition}
\declaretheorem[style=definition, name=Definition, numbered=no]{definition*}

\declaretheorem[style=definition, name=Example, numbered=yes, numberwithin=section]{example}
\declaretheorem[style=definition, name=Example, numbered=no]{example*}

\declaretheorem[style=definition, name=Problem, numbered=yes, numberwithin=section]{problem}
\declaretheorem[style=definition, name=Problem, numbered=no]{problem*}
```
- Use the `remark` style to define `remark` / `remark*`
```latex
\declaretheorem[style=remark, name=Remark, numbered=yes, numberwithin=section]{remark}
\declaretheorem[style=remark, name=Remark, numbered=no]{remark*}
```
- Use `\declaretheoremstyle` to define a new `notestyle`, similar to `remark`, but with the heading changed to `Note` and colored
```latex
\declaretheoremstyle[headfont=\color{orange!80}\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt]{notestyle}
```
- Use the custom `notestyle` to define `note` / `note*`
```latex
\declaretheorem[style=notestyle, name=Note, numbered=yes, numberwithin=section]{note}
\declaretheorem[style=notestyle, name=Note, numbered=no]{note*}
```
- Use `\declaretheoremstyle` to define a new `solutionstyle`, similar to `proof`, but with the heading changed to `Solution`
```latex
\declaretheoremstyle[headfont=\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\square}]{solutionstyle}
```
- Use the custom `solutionstyle` to define `solution` / `solution*`
```latex
\declaretheorem[style=solutionstyle, name=Solution, numbered=yes, numberwithin=section]{solution}
\declaretheorem[style=solutionstyle, name=Solution, numbered=no]{solution*}
```


## Theorem Styling

Import `tcolorbox` to style existing theorem environments with boxes.
```latex
\usepackage[most]{tcolorbox}
```

`tcolorbox` is very feature-rich, but only `\tcolorboxenvironment` is needed here.

First, wrap it into a `\newtcbenvironment` command:
```latex
\newcommand{\newtcbenvironment}[2]{
    \tcolorboxenvironment{#1}{#2, enhanced, breakable, sharp corners, boxrule=1pt}
    \tcolorboxenvironment{#1*}{#2, enhanced, breakable, rounded corners, boxrule=1pt}
}
```

This adds boxes to both `#1` and `#1*`. The shared options are:

- `#2`: options passed in during definition, mainly frame and background colors
- `enhanced`: enhanced styling
- `breakable`: allow page breaks
- `boxrule=1pt`: set frame width to 1pt

The differences are:

- `#1` uses sharp corners
- `#1*` uses rounded corners

> By adjusting the shared options inside `\newtcbenvironment`, you can also achieve other effects, such as left-border-only boxes or borderless boxes.

Next, apply boxes to the theorem environments above. The main parameters are the frame color `colframe` and background color `colback`.
```latex
%% define styles

\newtcbenvironment{theorem}{colframe=RoyalPurple, colback=RoyalPurple!8}
\newtcbenvironment{proposition}{colframe=RoyalPurple, colback=RoyalPurple!8}
\newtcbenvironment{corollary}{colframe=NavyBlue, colback=SkyBlue!8}
\newtcbenvironment{lemma}{colframe=NavyBlue, colback=SkyBlue!8}
\newtcbenvironment{claim}{colframe=NavyBlue, colback=SkyBlue!8}

\newtcbenvironment{definition}{colframe=ForestGreen, colback=ForestGreen!5}
\newtcbenvironment{example}{colframe=RawSienna, colback=RawSienna!5}
\newtcbenvironment{problem}{colframe=WildStrawberry!30, colback=WildStrawberry!5}
```

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

In addition, a simple untitled box `cbox` is defined:
```latex
%% cbox
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


## Custom Cover Page

Define a custom cover page, inspired by [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook) and several of its derived templates:
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

The recommended cover image size is `1280 × 1024`; especially for `jpg` images, using a different size will cause compilation errors.
