#!/usr/bin/env bash

set -Eeuo pipefail

latex_engine="${1:-pdflatex}"

case "${latex_engine}" in
  pdflatex)
    latexmk_mode="-pdf"
    ;;
  xelatex)
    latexmk_mode="-pdfxe"
    ;;
  lualatex)
    latexmk_mode="-pdflua"
    ;;
  *)
    echo "Unsupported LaTeX engine: ${latex_engine}" >&2
    echo "Supported engines: pdflatex, xelatex, lualatex" >&2
    exit 2
    ;;
esac

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
build_root="${repo_root}/.aux/note-template-tests"
generated_dir="${build_root}/generated"
aux_root="${build_root}/aux"
artifact_dir="${repo_root}/artifacts/note"
note_package="${repo_root}/note-sty/latexzero-note.sty"
note_styles=(default attached leftbar shaded plain)

rm -rf -- "${build_root}" "${artifact_dir}"
mkdir -p "${generated_dir}" "${aux_root}" "${artifact_dir}"

mapfile -t note_setups < <(
  find "${repo_root}/note" -maxdepth 1 -type f \
    -name 'note-setup*.tex' -print | sort
)

if ((${#note_setups[@]} == 0)); then
  echo "No Note setup files found." >&2
  exit 1
fi

if [[ ! -f "${note_package}" ]]; then
  echo "Note package not found: ${note_package}" >&2
  exit 1
fi

export TEXINPUTS="${repo_root}/note-sty:${TEXINPUTS:-}"

build_tex() {
  local source_file="$1"
  local test_name
  local aux_dir

  test_name="$(basename "${source_file}" .tex)"
  aux_dir="${aux_root}/${test_name}"
  mkdir -p "${aux_dir}"

  echo "::group::Build ${test_name} with ${latex_engine}"
  latexmk -cd \
    "${latexmk_mode}" \
    -file-line-error \
    -halt-on-error \
    -interaction=nonstopmode \
    "-auxdir=${aux_dir}" \
    "-outdir=${generated_dir}" \
    "${source_file}"
  echo "::endgroup::"

  cp "${generated_dir}/${test_name}.pdf" \
    "${artifact_dir}/${test_name}.pdf"
}

generate_note_test() {
  local test_name="$1"
  local preamble="$2"
  local test_file

  test_file="${generated_dir}/${test_name}.tex"

  cat >"${test_file}" <<EOF
\documentclass{article}
${preamble}

\title{Note Template Test: ${test_name}}
\author{GitHub Actions}
\date{\today}

\begin{document}

\maketitle

\section{Numbered Environments}

\begin{theorem}[Optional title]\label{thm:first}
For every real number \(x\), \(x^2 \geq 0\).
\end{theorem}

\begin{proposition}
This proposition shares the theorem counter.
\end{proposition}

\begin{corollary}
The shared counter continues to increase.
\end{corollary}

\begin{lemma}
This is a lemma referring to Theorem~\ref{thm:first}.
\end{lemma}

\begin{claim}
This is a claim.
\end{claim}

\begin{definition}
A definition uses upright body text.
\end{definition}

\begin{example}
This is an example.
\end{example}

\begin{problem}
Compute \(1+1\).
\end{problem}

\begin{remark}
This is a remark.
\end{remark}

\begin{note}
This is a note.
\end{note}

\begin{solution}
The answer is \(2\).
\end{solution}

\section{Unnumbered Environments}

\begin{theorem*}Unnumbered theorem.\end{theorem*}
\begin{proposition*}Unnumbered proposition.\end{proposition*}
\begin{corollary*}Unnumbered corollary.\end{corollary*}
\begin{lemma*}Unnumbered lemma.\end{lemma*}
\begin{claim*}Unnumbered claim.\end{claim*}
\begin{definition*}Unnumbered definition.\end{definition*}
\begin{example*}Unnumbered example.\end{example*}
\begin{problem*}Unnumbered problem.\end{problem*}
\begin{remark*}Unnumbered remark.\end{remark*}
\begin{note*}Unnumbered note.\end{note*}
\begin{solution*}Unnumbered solution.\end{solution*}

\end{document}
EOF

  build_tex "${test_file}"
}

for setup_file in "${note_setups[@]}"; do
  setup_name="$(basename "${setup_file}" .tex)"
  generate_note_test \
    "test-${setup_name}" \
    "\\input{${setup_file}}"
done

for style in "${note_styles[@]}"; do
  generate_note_test \
    "test-latexzero-note-${style}" \
    "\\usepackage[style=${style}]{latexzero-note}"
done

{
  echo "Generated Note template PDFs"
  echo
  echo "LaTeX engine: ${latex_engine}"
  echo
  echo "Standalone setups: ${#note_setups[@]}"
  printf '  - %s\n' "${note_setups[@]##*/}"
  echo
  echo "Package styles: ${#note_styles[@]}"
  printf '  - %s\n' "${note_styles[@]}"
} >"${artifact_dir}/manifest.txt"

total_tests=$((${#note_setups[@]} + ${#note_styles[@]}))
echo "Built ${total_tests} Note template tests."
