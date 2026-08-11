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
build_root="${repo_root}/.aux/beamer-template-tests"
generated_dir="${build_root}/generated"
aux_root="${build_root}/aux"
artifact_dir="${repo_root}/artifacts/beamer"

rm -rf -- "${build_root}" "${artifact_dir}"
mkdir -p "${generated_dir}" "${aux_root}" "${artifact_dir}"

mapfile -t beamer_setups < <(
  find "${repo_root}/beamer" -maxdepth 1 -type f \
    -name 'beamer-setup*.tex' -print | sort
)

if ((${#beamer_setups[@]} == 0)); then
  echo "No Beamer setup files found." >&2
  exit 1
fi

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

generate_beamer_test() {
  local setup_file="$1"
  local setup_name
  local test_file

  setup_name="$(basename "${setup_file}" .tex)"
  test_file="${generated_dir}/test-${setup_name}.tex"

  cat >"${test_file}" <<EOF
\documentclass[compress,aspectratio=169]{beamer}
\input{${setup_file}}

\title{Beamer Template Test}
\subtitle{${setup_name}}
\author{GitHub Actions}
\institute{latexzero}
\date{\today}

\begin{document}

\begin{frame}[plain]
  \titlepage
\end{frame}

\section{Components}

\begin{frame}{Text and Lists}
  Ordinary text with \alert{an alert} and inline mathematics
  \(Ax=b\).

  \begin{itemize}
    \item First item
    \item Second item
  \end{itemize}
\end{frame}

\begin{frame}{Blocks}
  \begin{block}{Standard block}
    Block content.
  \end{block}

  \begin{alertblock}{Alert block}
    Alert content.
  \end{alertblock}

  \begin{exampleblock}{Example block}
    Example content.
  \end{exampleblock}
\end{frame}

\begin{frame}{Theorem and Columns}
  \begin{theorem}
    For every real number \(x\), \(x^2 \geq 0\).
  \end{theorem}

  \begin{columns}
    \begin{column}{0.48\textwidth}
      Left column.
    \end{column}
    \begin{column}{0.48\textwidth}
      Right column.
    \end{column}
  \end{columns}
\end{frame}

\end{document}
EOF

  build_tex "${test_file}"
}

for setup_file in "${beamer_setups[@]}"; do
  generate_beamer_test "${setup_file}"
done

{
  echo "Generated Beamer template PDFs"
  echo
  echo "LaTeX engine: ${latex_engine}"
  echo
  echo "Beamer: ${#beamer_setups[@]}"
  printf '  - %s\n' "${beamer_setups[@]##*/}"
} >"${artifact_dir}/manifest.txt"

echo "Built ${#beamer_setups[@]} Beamer templates."
