# note-setup 配置说明

## 基本配置

导入常用的基础宏包
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

导入颜色支持的宏包
```latex
\usepackage[dvipsnames]{xcolor}
```

插入图片以及子图的相关宏包，对图片文件夹路径进行配置
```latex
\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}
    {./graphics/}{./picture/}{./pictures/}
}
\usepackage{subcaption}
```

导入算法环境的宏包
```latex
\usepackage[ruled,linesnumbered,noline]{algorithm2e}
```

导入代码环境的宏包并配置样式
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

导入超链接支持的宏包
```latex
\usepackage[colorlinks=true,linkcolor=cyan,urlcolor=magenta,citecolor=violet]{hyperref}
```


## 定理环境

修改 proof 环境的引导词为 Proof，样式为加粗无斜体
```latex
\renewcommand*{\proofname}{\normalfont\bfseries Proof}
```

导入 thmtools 宏包，使用 `\declaretheorem` 命令来定义各种定理环境（比`\newtheorem`命令更加方便）
```latex
\usepackage{thmtools}
```

使用的 `\declaretheorem` 命令参数包括：

- `style`: 定理环境样式，amsthm 内置的样式包括
  - plain（默认）：引导词是正体，内容是斜体
  - definition：引导词和内容都是正体
  - remark：引导词是斜体，内容是正体
- `name`：显示在正文中的引导词（不等于环境的名称）
- `numbered`：是否开启编号
- `numberwithin`、`sibling`：定义编号规则，例如
  - `numberwithin=section`：基于 section 编号
  - `sibling=theorem`：共享 `theorem` 环境的编号


具体包括：

- 采用 plain 样式，定义 `theorem`/`theorem*`、`proposition`/`proposition*`、`corollary`/`corollary*`、`lemma`/`lemma*`、`claim`/`claim*` 环境
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
- 采用 definition 样式，定义 `definition`/`definition*`、`example`/`example*`、`problem`/`problem*` 环境
```latex
\declaretheorem[style=definition, name=Definition, numbered=yes, numberwithin=section]{definition}
\declaretheorem[style=definition, name=Definition, numbered=no]{definition*}

\declaretheorem[style=definition, name=Example, numbered=yes, numberwithin=section]{example}
\declaretheorem[style=definition, name=Example, numbered=no]{example*}

\declaretheorem[style=definition, name=Problem, numbered=yes, numberwithin=section]{problem}
\declaretheorem[style=definition, name=Problem, numbered=no]{problem*}
```
- 采用 remark 样式，定义 `remark`/`remark*`、`note`/`note*` 环境
```latex
\declaretheorem[style=remark, name=Remark, numbered=yes, numberwithin=section]{remark}
\declaretheorem[style=remark, name=Remark, numbered=no]{remark*}

\declaretheorem[style=remark, name=Note, numbered=yes, numberwithin=section]{note}
\declaretheorem[style=remark, name=Note, numbered=no]{note*}
```
- 使用 `\declaretheoremstyle` 命令定义新的 solutionstyle 样式，类似 proof 环境，但是引导词变成 Solution
```latex
\declaretheoremstyle[headfont=\bfseries, bodyfont=\normalfont, spaceabove=3pt, spacebelow=3pt, qed=\ensuremath{\square}]{solutionstyle}
```
- 采用新定义的 solutionstyle 样式，定义 `solution`/`solition*` 环境
```latex
\declaretheorem[style=solutionstyle, name=Solution, numbered=yes, numberwithin=section]{solution}
\declaretheorem[style=solutionstyle, name=Solution, numbered=no]{solution*}
```


## 定理环境的美化

导入 tcolorbox 宏包以使用盒子美化现有的定理环境
```latex
\usepackage[most]{tcolorbox}
```

tcolorbox 宏包的功能非常复杂，这里只需要使用 `\tcolorboxenvironment` 命令。

首先封装一个 `\newtcbenvironment` 命令
```latex
\newcommand{\newtcbenvironment}[2]{
    \tcolorboxenvironment{#1}{#2, enhanced, breakable, sharp corners, boxrule=1pt}
    \tcolorboxenvironment{#1*}{#2, enhanced, breakable, rounded corners, boxrule=1pt}
}
```

它可以同时为 `#1` 以及 `#1*` 这两个环境加上盒子，公共参数：

- `#2`：在定义时传入的参数，这里主要是边框颜色和背景色
- `enhanced`：样式增强
- `breakable`：允许跨页
- `boxrule=1pt`：边框宽度为 1pt

还有不同的参数：

- `#1` 盒子使用直角边框（`sharp corners`）
- `#1*` 盒子使用圆角边框（`rounded corners`）

> 对 `\newtcbenvironment` 内部的公共参数部分进行调整，就可以实现所有盒子只保留左侧边框或者四周无边框等不同的效果。

下面就是为前面的各种定理环境加上盒子，参数是盒子的边框颜色 `colframe` 和背景色 `colback`
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

具体颜色如下表

|            环境名             |   盒子边框颜色    |    盒子背景色    |
| :---------------------------: | :---------------: | :--------------: |
|   `theorem`, `proposition`    |    RoyalPurple    |  RoyalPurple!8   |
| `corollary`, `lemma`, `claim` |     NavyBlue      |    SkyBlue!8     |
|         `definition`          |    ForestGreen    |  ForestGreen!5   |
|           `example`           |     RawSienna     |   RawSienna!5    |
|           `problem`           | WildStrawberry!30 | WildStrawberry!5 |

说明：

- 这里采用 `xcolor` 宏包所提供的标准颜色，`xxx!n`代表将颜色 `xxx` 以 `n%` 比例和白色混合得到的浅颜色。
- 为了避免颜色过多，对语义类似的环境合并采用相同的盒子颜色。
