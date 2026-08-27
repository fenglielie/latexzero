# note-setup 配置说明

本文说明默认的 [`note-setup.tex`](../note/note-setup.tex)。其他 setup 文件保留相同的宏包、命令和定理环境，只改变呈现方式：`attached` 使用附着式定理标题，`leftbar` 使用彩色左边线，`shaded` 隐藏边框，`plain` 不依赖tcolorbox；实验性的 `dark` setup 则采用深色配色。

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

先导入 `tcolorbox`，再导入 `keytheorems`。默认 setup 使用 keytheorems
原生的 tcolorbox 接口，而不是在定理环境定义完成后再从外部包装盒子。
```latex
\usepackage[most]{tcolorbox}
\usepackage{keytheorems}
\usepackage{pifont}
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
- `tcolorbox-no-titlebar`：应用 tcolorbox 参数，同时将定理标题保留在
  盒子正文中

公共盒子几何样式只定义一次。有编号环境使用直角，无编号环境使用圆角变体。
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


具体包括：

- 采用 `plain` 样式，定义 `theorem` / `theorem*`、`proposition` / `proposition*`、`corollary` / `corollary*`、`lemma` / `lemma*`、`claim` / `claim*` 环境
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
- 采用 `definition` 样式，定义 `definition` / `definition*`、`example` / `example*`、`problem` / `problem*` 环境
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
- 采用标准 `remark` 字体规范（标题斜体、正文正体），不使用盒子
```latex
\newkeytheorem{remark}[style=remark, name=Remark, numbered=true, parent=section]
\newkeytheorem{remark*}[style=remark, name=Remark, numbered=false]
```
- 定义一个位于左侧页边的零宽度手写标记，再使用 `\newkeytheoremstyle` 设置橙色粗体标题、正体正文和同色结束标记
```latex
\newcommand{\notehandmark}{\llap{\raisebox{0.05ex}{\large\ding{45}}\hspace{0.6em}}}
\newkeytheoremstyle{notestyle}{headfont=\color{orange!80!black}\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\color{orange!80!black}\diamond}}
```
- 采用 `notestyle` 定义 `note` / `note*`；左侧标记不占水平空间，因此正文宽度和缩进保持不变
```latex
\newkeytheorem{note}[style=notestyle, name={\notehandmark Note}, numbered=true, parent=section]
\newkeytheorem{note*}[style=notestyle, name={\notehandmark Note}, numbered=false]
```
- `plain` setup 与宏包的 `style=plain` 选项保留相同的执笔手和结束符，
  但不为其添加颜色，以维持极简风格。
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

盒子配置直接写在各个 `\newkeytheorem` 声明中，使环境定义、编号规则和
视觉样式集中在同一处。主要参数是边框颜色 `colframe` 和背景颜色
`colback`；`enhanced` 开启增强功能，`breakable` 允许跨页，
`boxrule=1pt` 将边框宽度设为 1pt。

`leftbar` 和 `shaded` setup 保留相同的环境声明，只替换公共盒子几何
样式；`attached` setup 则使用 keytheorems 的 `tcolorbox` 键，将定理
标题作为盒子标题。

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

## 自定义封面页

自定义封面页，参考 [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook) ：
```latex
%% cover
\usepackage{titling}
\newcommand{\extrainfo}{}
\renewcommand{\extrainfo}[1]{\renewcommand{\extrainfocontent}{#1}}
\newcommand{\extrainfocontent}{}
\newcommand{\makecover}[1]{%
    \begingroup
    \hypersetup{pageanchor=false}%
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
    \endgroup
}
% USAGE
% \extrainfo{xxx}
% \makecover{/path/to/cover.png}
```

这里没有选择覆盖 `\maketitle`，而是定义了一个新的 `\makecover` 命令，并将封面图路径作为其必需参数。

原始封面图采用 `1280 × 1024` 的宽高比。其他尺寸也可以编译，但图片的
宽高比会改变其占用的垂直空间，可能需要相应调整版面。

## 旧版 `cbox` 兼容

模板不再默认定义自定义 `cbox` 环境。仍在使用该环境的文档，可以把以下片段直接添加到主文件导言区：放在载入 setup 或 `latexzero-note` 之后、`\begin{document}` 之前即可。

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
