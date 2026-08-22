# note-setup 配置说明

## 基本配置

导入常用基础宏包
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

导入颜色相关宏包
```latex
\usepackage[dvipsnames]{xcolor}
```

导入图片与子图相关宏包，并配置图片搜索路径
```latex
\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}
    {./graphics/}{./picture/}{./pictures/}
}
\usepackage{subcaption}
```

导入算法环境宏包
```latex
\usepackage[ruled,linesnumbered,noline]{algorithm2e}
```

导入代码环境宏包并配置样式
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

导入超链接宏包
```latex
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,linkcolor=,urlcolor=cyan
}
```


## 定理环境

将 `proof` 环境的标题改为 `Proof`，并设置为加粗正体
```latex
\renewcommand*{\proofname}{\normalfont\bfseries Proof}
```

导入 `keytheorems` 宏包，并使用 `\newkeytheorem` 命令通过键值接口定义各类定理环境
```latex
\usepackage{keytheorems}
```

这里使用的 `\newkeytheorem` 命令参数包括：

- `style`：定理环境样式，`amsthm` 内置的样式包括
  - plain（默认）：引导词是正体，内容是斜体
  - definition：引导词和内容都是正体
  - remark：引导词是斜体，内容是正体
- `name`：显示在正文中的引导词（不等于环境的名称）
- `numbered`：是否开启编号
- `parent`、`sibling`：定义编号规则，例如
  - `parent=section`：基于 `section` 编号
  - `sibling=theorem`：共享 `theorem` 环境的编号


具体包括：

- 采用 `plain` 样式，定义 `theorem` / `theorem*`、`proposition` / `proposition*`、`corollary` / `corollary*`、`lemma` / `lemma*`、`claim` / `claim*` 环境
```latex
%% define environments

\newkeytheorem{theorem}[style=plain, name=Theorem, numbered=true, parent=section]
\newkeytheorem{theorem*}[style=plain, name=Theorem, numbered=false]

\newkeytheorem{proposition}[style=plain, name=Proposition, numbered=true, sibling=theorem]
\newkeytheorem{proposition*}[style=plain, name=Proposition, numbered=false]

\newkeytheorem{corollary}[style=plain, name=Corollary, numbered=true, sibling=theorem]
\newkeytheorem{corollary*}[style=plain, name=Corollary, numbered=false]

\newkeytheorem{lemma}[style=plain, name=Lemma, numbered=true, sibling=theorem]
\newkeytheorem{lemma*}[style=plain, name=Lemma, numbered=false]

\newkeytheorem{claim}[style=plain, name=Claim, numbered=true, sibling=theorem]
\newkeytheorem{claim*}[style=plain, name=Claim, numbered=false]
```
- 采用 `definition` 样式，定义 `definition` / `definition*`、`example` / `example*`、`problem` / `problem*` 环境
```latex
\newkeytheorem{definition}[style=definition, name=Definition, numbered=true, parent=section]
\newkeytheorem{definition*}[style=definition, name=Definition, numbered=false]

\newkeytheorem{example}[style=definition, name=Example, numbered=true, parent=section]
\newkeytheorem{example*}[style=definition, name=Example, numbered=false]

\newkeytheorem{problem}[style=definition, name=Problem, numbered=true, parent=section]
\newkeytheorem{problem*}[style=definition, name=Problem, numbered=false]
```
- 采用 `remark` 样式，定义 `remark` / `remark*` 环境
```latex
\newkeytheorem{remark}[style=remark, name=Remark, numbered=true, parent=section]
\newkeytheorem{remark*}[style=remark, name=Remark, numbered=false]
```
- 使用 `\newkeytheoremstyle` 命令定义新的 `notestyle` 样式，类似 `remark` 环境，但引导词改为 `Note`，并带有颜色
```latex
\newkeytheoremstyle{notestyle}{headfont=\color{orange!80}\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt}
```
- 采用新定义的 `notestyle` 样式，定义 `note` / `note*` 环境
```latex
\newkeytheorem{note}[style=notestyle, name=Note, numbered=true, parent=section]
\newkeytheorem{note*}[style=notestyle, name=Note, numbered=false]
```
- 使用 `\newkeytheoremstyle` 命令定义新的 `solutionstyle` 样式，类似 `proof` 环境，但引导词改为 `Solution`
```latex
\newkeytheoremstyle{solutionstyle}{headfont=\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\square}}
```
- 采用新定义的 `solutionstyle` 样式，定义 `solution` / `solution*` 环境
```latex
\newkeytheorem{solution}[style=solutionstyle, name=Solution, numbered=true, parent=section]
\newkeytheorem{solution*}[style=solutionstyle, name=Solution, numbered=false]
```

## 定理环境的美化

导入 `tcolorbox` 宏包，用盒子样式美化现有的定理环境
```latex
\usepackage[most]{tcolorbox}
```

`tcolorbox` 宏包功能非常丰富，这里只用到 `\tcolorboxenvironment` 命令。

首先封装一个 `\newtcbenvironment` 命令：
```latex
\newcommand{\newtcbenvironment}[2]{
    \tcolorboxenvironment{#1}{#2, enhanced, breakable, sharp corners, boxrule=1pt}
    \tcolorboxenvironment{#1*}{#2, enhanced, breakable, rounded corners, boxrule=1pt}
}
```

它可以同时为 `#1` 和 `#1*` 这两个环境加上盒子，其中公共参数包括：

- `#2`：定义时传入的参数，这里主要是边框颜色和背景色
- `enhanced`：样式增强
- `breakable`：允许跨页
- `boxrule=1pt`：边框宽度为 1pt

此外还有以下区别：

- `#1` 盒子使用直角边框（`sharp corners`）
- `#1*` 盒子使用圆角边框（`rounded corners`）

> 调整 `\newtcbenvironment` 内部的公共参数后，可以进一步实现仅保留左侧边框、或四周无边框等不同效果。

下面为前面的各类定理环境加上盒子，主要参数是盒子的边框颜色 `colframe` 和背景色 `colback`。
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

具体颜色如下表：

|            环境名             |   盒子边框颜色    |    盒子背景色    |
| :---------------------------: | :---------------: | :--------------: |
|   `theorem`, `proposition`    |    RoyalPurple    |  RoyalPurple!8   |
| `corollary`, `lemma`, `claim` |     NavyBlue      |    SkyBlue!8     |
|         `definition`          |    ForestGreen    |  ForestGreen!5   |
|           `example`           |     RawSienna     |   RawSienna!5    |
|           `problem`           | WildStrawberry!30 | WildStrawberry!5 |

说明：

- 这里采用 `xcolor` 宏包提供的标准颜色，`xxx!n` 表示将颜色 `xxx` 按 `n%` 的比例与白色混合得到的浅色。
- 为了避免颜色过多，对语义类似的环境合并采用相同的盒子颜色。

此外，还添加了一个没有标题的简单盒子 `cbox`：
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


## 自定义封面页

自定义封面页，参考 [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook) ：
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

这里没有选择覆盖 `\maketitle`，而是定义了一个新的 `\makecover` 命令，并将封面图路径作为其必需参数。

封面图建议使用 `1280 × 1024` 的尺寸；尤其对于 `jpg` 格式的图片，尺寸不同会导致编译报错。
