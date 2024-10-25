#!/usr/bin/env python3

import os
import subprocess
import logging
import argparse
import shutil
import time

SKIP_DIRS = ["chapters", "chapter", ".git", ".aux"]

success_count = 0
failure_count = 0
failed_msgs = []


def show_success(subdir, tex_file, latex_command, elapsed_time):
    global success_count

    msg = f"- [✓] {tex_file} in {subdir} ({latex_command}) ({elapsed_time:.2f}s)"
    print(msg)
    success_count += 1


def show_failure(subdir, tex_file, latex_command, elapsed_time):
    global failure_count, failed_msgs

    msg = f"- [x] {tex_file} in {subdir} ({latex_command}) ({elapsed_time:.2f}s)"
    print(msg)
    failed_msgs.append(msg)
    failure_count += 1


def compile_tex_file(tex_file, subdir, default_engine):
    tex_file_path = os.path.join(subdir, tex_file)

    engine = get_tex_engine(tex_file_path, default_engine)

    if engine == "pdflatex":
        latex_command = "-pdf"
    else:
        latex_command = f"-{engine}"

    logging.info(f"Compiling {tex_file} with {engine} in {subdir}")

    start_time = time.time()
    try:
        result = subprocess.run(
            ["latexmk", latex_command, tex_file],
            cwd=subdir,
            capture_output=True,
            timeout=120,
        )

        end_time = time.time()
        elapsed_time = end_time - start_time

        if result.returncode == 0:
            logging.info(f"Successfully compiled {tex_file} in {subdir}")
            show_success(subdir, tex_file, latex_command, elapsed_time)
        else:
            logging.error(f"Failed to compile {tex_file} in {subdir}")
            show_failure(subdir, tex_file, latex_command, elapsed_time)
            logging.debug(result.stderr.decode("utf-8"))

    except subprocess.TimeoutExpired:
        end_time = time.time()
        elapsed_time = end_time - start_time

        logging.error(f"Compilation of {tex_file} in {subdir} timed out.")
        show_failure(subdir, tex_file, latex_command, elapsed_time)
    except Exception as e:
        end_time = time.time()
        elapsed_time = end_time - start_time

        logging.error(f"Error during compilation of {tex_file} in {subdir}: {e}")
        show_failure(subdir, tex_file, latex_command, elapsed_time)


def is_main_tex_file(tex_file_path):
    """check \\documentclass in .tex file"""
    try:
        with open(tex_file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return "\\documentclass" in content
    except Exception as e:
        logging.error(f"Error reading {tex_file_path}: {e}")
        return False


def get_tex_engine(tex_file_path, default_engine):
    """detect latex engine in .tex file"""
    try:
        # check shebang
        with open(tex_file_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            if first_line.startswith("#!"):
                logging.debug(f"Found shebang in {tex_file_path}")
                if "xelatex" in first_line:
                    return "xelatex"
                elif "pdflatex" in first_line:
                    return "pdflatex"
                elif "lualatex" in first_line:
                    return "lualatex"

        # check ctex, use xelatex if found
        with open(tex_file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "\\begin{document}" in line:
                    break
                if "ctex" in line:
                    logging.debug(f"Found ctex in {line}")
                    return "xelatex"

    except Exception as e:
        logging.error(f"Error reading {tex_file_path}: {e}")
        return default_engine

    return default_engine


def process_directory(subdir, default_engine):
    tex_files = [f for f in os.listdir(subdir) if f.endswith(".tex")]

    if len(tex_files) > 0:
        for tex_file in tex_files:
            tex_file_path = os.path.join(subdir, tex_file)
            if is_main_tex_file(tex_file_path):
                compile_tex_file(tex_file, subdir, default_engine)
            else:
                logging.debug(f"Ignoring {tex_file} (not a main file)")
    else:
        logging.debug(f"No .tex files found in {subdir}")


def clean_aux_directory(subdir):
    aux_dir = os.path.join(subdir, ".aux")

    if os.path.exists(aux_dir) and os.path.isdir(aux_dir):
        logging.info(f"Cleaning .aux directory in {subdir}")
        try:
            shutil.rmtree(aux_dir)
            logging.info(f"Successfully cleaned .aux directory in {subdir}")
        except Exception as e:
            logging.error(f"Failed to clean .aux directory in {subdir}: {e}")
    else:
        logging.debug(f"No .aux directory found in {subdir}")


def main(root_dir, mode, default_engine, log_level):
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s]{%(levelname)s} %(message)s",
        handlers=[logging.StreamHandler()],  # -> console
    )

    for subdir, dirs, _ in os.walk(root_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]  # remove skipped dirs

        logging.debug(f"Processing directory: {subdir}")

        if mode in ["clean", "both"]:
            clean_aux_directory(subdir)

        if mode in ["compile", "both"]:
            process_directory(subdir, default_engine)

    if mode in ["compile", "both"]:
        print(f"Succeed: {success_count}   Failed: {failure_count}")
        if failed_msgs:
            print("Failed Files:")
            for failed_msg in failed_msgs:
                print(failed_msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compile or clean .tex files in the given directory."
    )
    parser.add_argument(
        "root_dir", type=str, help="The root directory to search for .tex files."
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["clean", "compile", "both"],
        default="both",
        help="Choose the operation mode: 'clean' to clean .aux files, 'compile' to compile .tex files, or 'both' to clean and compile (default: both).",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Set the logging level (default: WARNING).",
    )
    parser.add_argument(
        "--engine",
        type=str,
        choices=["xelatex", "pdflatex", "lualatex"],
        default="xelatex",
        help="Set the default LaTeX engine (default: xelatex).",
    )

    args = parser.parse_args()
    log_level = getattr(logging, args.log_level)

    main(args.root_dir, args.mode, args.engine, log_level)
