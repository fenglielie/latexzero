#!/usr/bin/env python3
"""Build every PNG preview used by the repository README files.

Examples:
    python .github/scripts/build-assets.py
    python .github/scripts/build-assets.py --dpi 180

The script only needs Python's standard library, latexmk, and pdftocairo.
Intermediate TeX and PDF files are kept under .aux/readme-assets/.
"""

from __future__ import annotations

import argparse
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path


NOTE_STYLES = {
    "default": ("note-setup.tex", "note-setup-demo.png"),
    "attached": ("note-setup-attached.tex", "note-setup-attached-demo.png"),
    "leftbar": ("note-setup-leftbar.tex", "note-setup-leftbar-demo.png"),
    "shaded": ("note-setup-shaded.tex", "note-setup-shaded-demo.png"),
    "plain": ("note-setup-plain.tex", "note-setup-plain-demo.png"),
    "dark": ("note-setup-dark.tex", "note-setup-dark-demo.png"),
}

BEAMER_STYLES = {
    "default": (
        "beamer-setup.tex",
        "beamer-titlepage.png",
        "beamer-setup-demo.png",
    ),
    "minimal": (
        "beamer-setup-minimal.tex",
        "beamer-titlepage-minimal.png",
        "beamer-setup-minimal-demo.png",
    ),
    "console": (
        "beamer-setup-console.tex",
        "beamer-titlepage-console.png",
        "beamer-setup-console-demo.png",
    ),
}

LATEXMK_MODES = {
    "pdflatex": "-pdf",
    "xelatex": "-pdfxe",
    "lualatex": "-pdflua",
}

BEAMER_PREVIEW_FIRST_PAGE = 11
BEAMER_PREVIEW_PAGE_COUNT = 6
BEAMER_PREVIEW_COLUMNS = 2
BEAMER_SLIDE_WIDTH = "16cm"
BEAMER_PREVIEW_GAP = "1mm"

NOTE_SETUP_RE = re.compile(
    r"^\\input\{\.\./note-setup(?:-[^}]+)?\}\s*$", re.MULTILINE
)
BEAMER_SETUP_RE = re.compile(
    r"^\\input\{\.\./beamer-setup(?:-[^}]+)?\}\s*$", re.MULTILINE
)
NOTE_COVER_RE = re.compile(r"\\makecover\{\.\./cover/cover\.png\}")
BEAMER_BIB_RE = re.compile(r"\\addbibresource\{references\.bib\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile and render all PNG previews used by the README files."
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="PNG resolution passed to pdftocairo (default: 150).",
    )
    args = parser.parse_args()
    if args.dpi <= 0:
        parser.error("--dpi must be a positive integer")
    return args


def require_tool(name: str) -> str:
    executable = shutil.which(name)
    if executable is None:
        raise RuntimeError(f"Required executable not found on PATH: {name}")
    return executable


def run(command: list[str]) -> None:
    print("+", shlex.join(command), flush=True)
    subprocess.run(command, check=True)


def latex_path(path: Path) -> str:
    return path.resolve().as_posix()


def replace_once(
    source: str, pattern: re.Pattern[str], replacement: str, description: str
) -> str:
    rendered, replacements = pattern.subn(lambda _: replacement, source, count=1)
    if replacements != 1:
        raise RuntimeError(f"Expected exactly one {description}")
    return rendered


def write_source(path: Path, source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as generated_file:
        generated_file.write(source)


def compile_tex(
    *,
    tex_path: Path,
    pdf_dir: Path,
    aux_dir: Path,
    engine: str,
    latexmk: str,
) -> Path:
    pdf_dir.mkdir(parents=True, exist_ok=True)
    aux_dir.mkdir(parents=True, exist_ok=True)
    run(
        [
            latexmk,
            "-cd",
            "-silent",
            "-file-line-error",
            "-halt-on-error",
            "-interaction=nonstopmode",
            "-synctex=0",
            LATEXMK_MODES[engine],
            f"-auxdir={aux_dir.resolve()}",
            f"-outdir={pdf_dir.resolve()}",
            str(tex_path.resolve()),
        ]
    )
    pdf_path = pdf_dir / f"{tex_path.stem}.pdf"
    if not pdf_path.is_file():
        raise RuntimeError(f"latexmk did not produce the expected PDF: {pdf_path}")
    return pdf_path


def render_page(
    *, pdf_path: Path, page: int, image_path: Path, dpi: int, pdftocairo: str
) -> None:
    image_path.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            pdftocairo,
            "-png",
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-r",
            str(dpi),
            str(pdf_path.resolve()),
            str(image_path.with_suffix("").resolve()),
        ]
    )
    if not image_path.is_file():
        raise RuntimeError(
            f"pdftocairo did not produce the expected image: {image_path}"
        )


def build_note_onepage(
    *,
    style: str,
    engine: str,
    dpi: int,
    latexmk: str,
    pdftocairo: str,
    source: str,
    repo_root: Path,
    build_root: Path,
) -> None:
    setup_name, image_name = NOTE_STYLES[style]
    setup_path = repo_root / "note" / setup_name
    tex_path = build_root / "generated" / f"note-onepage-{style}.tex"
    rendered = replace_once(
        source,
        NOTE_SETUP_RE,
        rf"\input{{{latex_path(setup_path)}}}",
        "../note-setup*.tex input in note/demo/onepage-demo.tex",
    )
    write_source(tex_path, rendered)

    print(f"\n==> Building Note one-page style: {style}")
    pdf_path = compile_tex(
        tex_path=tex_path,
        pdf_dir=build_root / "pdf",
        aux_dir=build_root / "aux" / f"note-onepage-{style}",
        engine=engine,
        latexmk=latexmk,
    )
    image_path = repo_root / "assets" / image_name
    render_page(
        pdf_path=pdf_path,
        page=1,
        image_path=image_path,
        dpi=dpi,
        pdftocairo=pdftocairo,
    )
    print(f"    PNG: {image_path.relative_to(repo_root)}")


def build_note_cover(
    *,
    engine: str,
    dpi: int,
    latexmk: str,
    pdftocairo: str,
    source: str,
    repo_root: Path,
    build_root: Path,
) -> None:
    setup_path = repo_root / "note" / "note-setup-attached.tex"
    cover_path = repo_root / "note" / "cover" / "cover.png"
    tex_path = build_root / "generated" / "note-cover.tex"
    rendered = replace_once(
        source,
        NOTE_SETUP_RE,
        rf"\input{{{latex_path(setup_path)}}}",
        "../note-setup*.tex input in note/demo/main.tex",
    )
    rendered = replace_once(
        rendered,
        NOTE_COVER_RE,
        rf"\makecover{{{latex_path(cover_path)}}}",
        "../cover/cover.png reference in note/demo/main.tex",
    )
    write_source(tex_path, rendered)

    print("\n==> Building Note cover")
    pdf_path = compile_tex(
        tex_path=tex_path,
        pdf_dir=build_root / "pdf",
        aux_dir=build_root / "aux" / "note-cover",
        engine=engine,
        latexmk=latexmk,
    )
    image_path = repo_root / "assets" / "note-cover-demo.png"
    render_page(
        pdf_path=pdf_path,
        page=1,
        image_path=image_path,
        dpi=dpi,
        pdftocairo=pdftocairo,
    )
    print(f"    PNG: {image_path.relative_to(repo_root)}")


def generated_beamer_source(source: str, setup_path: Path, repo_root: Path) -> str:
    figures_path = latex_path(repo_root / "beamer" / "demo" / "figures") + "/"
    bibliography_path = repo_root / "beamer" / "demo" / "references.bib"
    rendered = replace_once(
        source,
        BEAMER_SETUP_RE,
        (
            rf"\input{{{latex_path(setup_path)}}}"
            "\n"
            rf"\graphicspath{{{{{figures_path}}}}}"
        ),
        "../beamer-setup*.tex input in beamer/demo/main.tex",
    )
    return replace_once(
        rendered,
        BEAMER_BIB_RE,
        rf"\addbibresource{{{latex_path(bibliography_path)}}}",
        "references.bib resource in beamer/demo/main.tex",
    )


def montage_source(pdf_path: Path) -> str:
    pages = range(
        BEAMER_PREVIEW_FIRST_PAGE,
        BEAMER_PREVIEW_FIRST_PAGE + BEAMER_PREVIEW_PAGE_COUNT,
    )
    images = [
        (
            rf"\includegraphics[page={page},width={BEAMER_SLIDE_WIDTH}]"
            rf"{{{latex_path(pdf_path)}}}"
        )
        for page in pages
    ]
    rows = [
        "\\hbox{%\n"
        + (f"\\hspace{{{BEAMER_PREVIEW_GAP}}}%\n").join(
            images[index : index + BEAMER_PREVIEW_COLUMNS]
        )
        + "%\n}"
        for index in range(0, len(images), BEAMER_PREVIEW_COLUMNS)
    ]
    return (
        "\\documentclass[border=0pt]{standalone}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{xcolor}\n"
        "\\definecolor{previewgap}{RGB}{210,210,210}\n"
        "\\pagecolor{previewgap}\n"
        "\\begin{document}\n"
        "\\vbox{\\offinterlineskip\n"
        + (f"%\n\\vskip{BEAMER_PREVIEW_GAP}%\n").join(rows)
        + "\n}\n"
        "\\end{document}\n"
    )


def build_beamer_style(
    *,
    style: str,
    engine: str,
    dpi: int,
    latexmk: str,
    pdftocairo: str,
    source: str,
    repo_root: Path,
    build_root: Path,
) -> None:
    setup_name, title_image_name, preview_image_name = BEAMER_STYLES[style]
    setup_path = repo_root / "beamer" / setup_name
    tex_path = build_root / "generated" / f"beamer-{style}.tex"
    write_source(tex_path, generated_beamer_source(source, setup_path, repo_root))

    print(f"\n==> Building Beamer style: {style}")
    pdf_path = compile_tex(
        tex_path=tex_path,
        pdf_dir=build_root / "pdf",
        aux_dir=build_root / "aux" / f"beamer-{style}",
        engine=engine,
        latexmk=latexmk,
    )

    title_image_path = repo_root / "assets" / title_image_name
    render_page(
        pdf_path=pdf_path,
        page=1,
        image_path=title_image_path,
        dpi=dpi,
        pdftocairo=pdftocairo,
    )

    montage_tex_path = build_root / "generated" / f"beamer-preview-{style}.tex"
    write_source(montage_tex_path, montage_source(pdf_path))
    montage_pdf_path = compile_tex(
        tex_path=montage_tex_path,
        pdf_dir=build_root / "pdf",
        aux_dir=build_root / "aux" / f"beamer-preview-{style}",
        engine=engine,
        latexmk=latexmk,
    )
    preview_image_path = repo_root / "assets" / preview_image_name
    render_page(
        pdf_path=montage_pdf_path,
        page=1,
        image_path=preview_image_path,
        dpi=dpi,
        pdftocairo=pdftocairo,
    )
    print(f"    PNG: {title_image_path.relative_to(repo_root)}")
    print(f"    PNG: {preview_image_path.relative_to(repo_root)}")


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    build_root = repo_root / ".aux" / "readme-assets"
    engine = "pdflatex"

    try:
        latexmk = require_tool("latexmk")
        pdftocairo = require_tool("pdftocairo")

        onepage_source = (
            repo_root / "note" / "demo" / "onepage-demo.tex"
        ).read_text(encoding="utf-8")
        for style in NOTE_STYLES:
            build_note_onepage(
                style=style,
                engine=engine,
                dpi=args.dpi,
                latexmk=latexmk,
                pdftocairo=pdftocairo,
                source=onepage_source,
                repo_root=repo_root,
                build_root=build_root,
            )

        note_source = (repo_root / "note" / "demo" / "main.tex").read_text(
            encoding="utf-8"
        )
        build_note_cover(
            engine=engine,
            dpi=args.dpi,
            latexmk=latexmk,
            pdftocairo=pdftocairo,
            source=note_source,
            repo_root=repo_root,
            build_root=build_root,
        )

        beamer_source = (repo_root / "beamer" / "demo" / "main.tex").read_text(
            encoding="utf-8"
        )
        for style in BEAMER_STYLES:
            build_beamer_style(
                style=style,
                engine=engine,
                dpi=args.dpi,
                latexmk=latexmk,
                pdftocairo=pdftocairo,
                source=beamer_source,
                repo_root=repo_root,
                build_root=build_root,
            )
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print("\nRefreshed all 13 README preview images.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
