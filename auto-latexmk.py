import os
import subprocess
import logging
import argparse
import shutil

LATEX_COMMAND = "-xelatex"

SKIP_DIRS = ["chapters", ".git"]

success_count = 0
failure_count = 0
failed_files = []


def compile_tex_file(tex_file, subdir):
    global success_count, failure_count, failed_files
    logging.info(f"Compiling {tex_file} in {subdir}")

    try:
        result = subprocess.run(
            ["latexmk", LATEX_COMMAND, tex_file], cwd=subdir, capture_output=True
        )

        if result.returncode == 0:
            logging.info(f"Successfully compiled {tex_file} in {subdir}")
            print("[✓] " + tex_file)
            success_count += 1
        else:
            logging.error(f"Failed to compile {tex_file} in {subdir}")
            print("[x] " + tex_file)
            failed_files.append(tex_file)
            failure_count += 1
            logging.debug(result.stderr.decode("utf-8"))

    except Exception as e:
        logging.error(f"Error during compilation of {tex_file}: {e}")
        failed_files.append(tex_file)
        failure_count += 1


def find_tex_files_in_directory(directory):
    return [f for f in os.listdir(directory) if f.endswith(".tex")]


def should_skip_directory(subdir):
    for skip_dir in SKIP_DIRS:
        if skip_dir in subdir.split(os.sep):
            logging.debug(f"Skipping directory {subdir} (contains '{skip_dir}').")
            return True
    return False


def process_directory(subdir):
    tex_files = find_tex_files_in_directory(subdir)

    if len(tex_files) > 0:
        if len(tex_files) == 1:
            # only one .tex
            compile_tex_file(tex_files[0], subdir)
        else:
            # many .tex, find main*.tex
            main_file = next((f for f in tex_files if "main" in f), None)
            if main_file:
                compile_tex_file(main_file, subdir)
            else:
                logging.warning(
                    f"Multiple .tex files found in {subdir}, but no 'main.tex' found."
                )
    else:
        logging.debug(f"No .tex files found in {subdir}.")


def clean_aux_directory(subdir):
    aux_dir = os.path.join(subdir, ".aux")

    if os.path.exists(aux_dir) and os.path.isdir(aux_dir):
        logging.info(f"Cleaning .aux directory in {subdir}")
        try:
            shutil.rmtree(aux_dir)
            logging.info(f"Successfully cleaned .aux directory in {subdir}.")
        except Exception as e:
            logging.error(f"Failed to clean .aux directory in {subdir}: {e}")
    else:
        logging.debug(f"No .aux directory found in {subdir}.")


def main(root_dir, clean_mode, log_level):
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s]{%(levelname)s} %(message)s",
        handlers=[logging.StreamHandler()],  # -> console
    )

    for subdir, _, _ in os.walk(root_dir):
        if should_skip_directory(subdir):
            continue

        if clean_mode:
            clean_aux_directory(subdir)
        else:
            process_directory(subdir)

    if not clean_mode:
        print(f"Succeed: {success_count}   Failed: {failure_count}")
        if failed_files:
            print("Failed Files:")
            for failed_file in failed_files:
                print(f"[x] {failed_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compile or clean .tex files in the given directory."
    )
    parser.add_argument(
        "root_dir", type=str, help="The root directory to search for .tex files."
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean the .aux directories instead of compiling .tex files.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Set the logging level (default: WARNING).",
    )

    args = parser.parse_args()
    log_level = getattr(logging, args.log_level)

    main(args.root_dir, args.clean, log_level)
