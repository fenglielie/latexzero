# LaTeX Templates for Mathematical Notes

A simple LaTeX template designed for mathematical notes.

Includes:

- Essential packages for mathematical symbols
- Packages for handling images and list environments
- Configuration for mathematical theorem environments
- Configuration for algorithm and code environments

Excludes:

- Bibliography configuration
- Chinese language support


Usage:

```latex
\documentclass{article}
\newcommand{\noteusemdframed}{true}
\input{/path/to/note-setup}

...
```

```latex
\documentclass[compress,aspectratio=43]{beamer}
\input{/path/to/beamer-setup}

...
```
