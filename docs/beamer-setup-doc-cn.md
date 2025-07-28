# beamer-setup 配置说明

## Beamer 样式配置

设置主题，包括导航栏样式，数学字体，主题颜色
```latex
\usetheme{default}
\useoutertheme[subsection=false]{miniframes}
\usefonttheme[onlymath]{serif}
\definecolor{simplebeamercolor}{RGB}{57,89,199}
\usecolortheme[named=simplebeamercolor]{structure}
```

设置标题页样式：圆角，加阴影
```latex
\setbeamertemplate{title page}[default][colsep=-4bp,rounded=true,shadow=true]
```

设置目录样式：section和subsection均开启编号，subsection加上缩进
```latex
\setbeamertemplate{section in toc}[sections numbered]
\setbeamertemplate{subsection in toc}[subsections numbered]
\addtobeamertemplate{subsection in toc}{\hspace{2em}}{}
```

设置无序列表和有序列表的样式
```latex
\setbeamertemplate{itemize items}[circle]
\setbeamertemplate{enumerate items}[default]
```

设置caption样式：开启编号
```latex
\setbeamertemplate{caption}[numbered]
```

设置底部样式：仅显示页码，移除导航按钮
```latex
\setbeamertemplate{footline}[frame number]{}
\setbeamertemplate{navigation symbols}{}
```

设置帧标题样式：在帧标题下面添加一条横线
```latex
\setbeamertemplate{frametitle}{\vspace*{0.5em}\insertframetitle\par\vskip-6pt\hrulefill\vspace{-0.1em}}
```

设置标题样式
```latex
\setbeamercolor{title}{use=structure,fg=white,bg=structure.fg}
```

设置顶部导航栏中的section样式
```latex
\setbeamercolor{section in head/foot}{fg=white,bg=structure.fg}
```

设置各个元素的颜色样式
```latex
\setbeamercolor{block body}{bg=structure!10}
\setbeamercolor{block title}{bg=structure!20}
\setbeamercolor{block body alerted}{bg=alerted text.fg!10}
\setbeamercolor{block title alerted}{bg=alerted text.fg!20}
\setbeamercolor{block body example}{bg=green!10}
\setbeamercolor{block title example}{bg=green!20}
```

## 其它配置

导入常用的基础宏包
```latex
% fonts
\usepackage[T1]{fontenc}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{bm}

% math
\usepackage{amsmath,amsthm,amsfonts,amssymb}

\usepackage{extarrows}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{multicol}
```

导入盒子宏包，并为`\tcbhighmath`命令设置预设样式
```latex
\usepackage[most]{tcolorbox}
\tcbset{
    highlight math style={enhanced, colframe=blue!40,colback=yellow!20,arc=4pt,boxrule=1pt}
}
```

导入超链接支持的宏包
```latex
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,linkcolor=cyan,urlcolor=blue
}
```

插入图片以及子图的相关宏包，对图片文件夹路径进行配置
```latex
\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}{./graphics/}{./picture/}{./pictures/}
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
    frame=single,
    framesep=1em,
}
\lstset{style=simpleStyle}
