$pdf_mode = 5;

$bibtex_use = 1.5;

$out_dir = "./";
$aux_dir = "./.aux";

$common_opts = '-file-line-error -halt-on-error -interaction=nonstopmode -auxdir=' . $aux_dir . ' -outdir=' . $out_dir;

$pdflatex = 'pdflatex ' . $common_opts . ' -no-pdf %O %S';
$xelatex = 'xelatex ' . $common_opts . ' %O %S';
$lualatex = 'lualatex ' . $common_opts . ' %O %S';

$xdvipdfmx = "xdvipdfmx -q -E -o %D %O %S";
