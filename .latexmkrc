$pdf_mode = 1;

$out_dir = "./";
$aux_dir = "./.aux";

$common_opts = '-interaction=nonstopmode -file-line-error -auxdir=' . $aux_dir . ' -outdir=' . $out_dir;

$pdflatex = 'pdflatex ' . $common_opts . ' %O %S';
$xelatex = 'xelatex ' . $common_opts . ' %O %S';
$lualatex = 'lualatex ' . $common_opts . ' %O %S';
