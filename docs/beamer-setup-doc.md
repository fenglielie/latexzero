# beamer-setup Documentation

## Beamer Style Configuration

Set the theme, including the navigation bar style, math font, and theme color.
```latex
\usetheme{default}
\useoutertheme[subsection=false]{miniframes}
\usefonttheme[onlymath]{serif}
\definecolor{simplebeamercolor}{RGB}{57,89,199}
\usecolortheme[named=simplebeamercolor]{structure}
```

Set the title page style: rounded corners and shadow.
```latex
\setbeamertemplate{title page}[default][colsep=-4bp,rounded=true,shadow=true]
```

Set the table of contents style: show numbering for both `section` and `subsection`, and add indentation to `subsection`.
```latex
\setbeamertemplate{section in toc}[sections numbered]
\setbeamertemplate{subsection in toc}[subsections numbered]
\addtobeamertemplate{subsection in toc}{\hspace{2em}}{}
```

Set the styles for unordered and ordered lists.
```latex
\setbeamertemplate{itemize items}[circle]
\setbeamertemplate{enumerate items}[default]
```

Set the `caption` style to display numbering.
```latex
\setbeamertemplate{caption}[numbered]
```

Set the footer style: show only page numbers and remove navigation symbols.
```latex
\setbeamertemplate{footline}[frame number]{}
\setbeamertemplate{navigation symbols}{}
```

Set the frame title style by adding a horizontal rule below the frame title.
```latex
\setbeamertemplate{frametitle}{\vspace*{0.5em}\insertframetitle\par\vskip-6pt\hrulefill\vspace{-0.1em}}
```

Set the title style.
```latex
\setbeamercolor{title}{use=structure,fg=white,bg=structure.fg}
```

Set the `section` style in the top navigation bar.
```latex
\setbeamercolor{section in head/foot}{fg=white,bg=structure.fg}
```

Set color styles for the various elements.
```latex
\setbeamercolor{block body}{bg=structure!10}
\setbeamercolor{block title}{bg=structure!20}
\setbeamercolor{block body alerted}{bg=alerted text.fg!10}
\setbeamercolor{block title alerted}{bg=alerted text.fg!20}
\setbeamercolor{block body example}{bg=green!10}
\setbeamercolor{block title example}{bg=green!20}
```

## Other Configuration

Import commonly used base packages.
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

Import the box package and define a preset style for `\tcbhighmath`.
```latex
\usepackage[most]{tcolorbox}
\tcbset{
    highlight math style={enhanced, colframe=blue!40,colback=yellow!20,arc=4pt,boxrule=1pt}
}
```

Import the hyperlink package.
```latex
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,linkcolor=,urlcolor=cyan
}
```

Import packages for images and subfigures, and configure image search paths.
```latex
\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}{./graphics/}{./picture/}{./pictures/}
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
    frame=single,
    framesep=1em,
}
\lstset{style=simpleStyle}
```
