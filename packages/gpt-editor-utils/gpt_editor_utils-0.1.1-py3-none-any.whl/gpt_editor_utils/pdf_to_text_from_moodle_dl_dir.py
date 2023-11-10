#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-11-09
Purpose: Convert PDFs in moodle-dl dir to text files in output dir. Old PDFs like `*_01.pdf` are ignored.
"""

import argparse
from pathlib import Path
from gpt_editor_utils.utils import (
    find_files,
    pdf_to_text_pymupdf,
    slugify,
    # contains_binary,
    is_plain_text,
)


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Convert PDFs in moodle-dl dir to text files in output dir. Old PDFs like `*_01.pdf` are ignored.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # input dir
    parser.add_argument(
        "input",
        metavar="input",
        type=Path,
        help="Input dir containing PDFs",
    )

    # output dir
    parser.add_argument(
        "output",
        metavar="output",
        type=Path,
        help="Output dir containing text files",
    )

    # output_filename_includes_path
    parser.add_argument(
        "-p",
        "--output-filename-includes-path",
        action="store_true",
        help="Output filename includes path",
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    pdf_glob_pattern = "*.pdf"
    moodle_pdf_re_pattern = r"(?<!_\d{2})\.pdf$"
    args.output.mkdir(parents=True, exist_ok=True)

    def process_pdf(p: Path):
        if p.stem == "HW3_Fall_2023_PRINT":
            print(f"Skipping {p}")
            return
        texts = pdf_to_text_pymupdf(p)
        if args.output_filename_includes_path:
            output_text_filename = slugify(str(p).removesuffix(".pdf")) + ".txt"
        else:
            output_text_filename = slugify(p.stem) + ".txt"
        output_text_path = args.output / output_text_filename
        with open(output_text_path, "w") as f:
            f.write("\n\n---\n\n".join(x for x in texts if is_plain_text(x)))

    for p in find_files(
        args.input,
        recursive=True,
        glob_pattern=pdf_glob_pattern,
        regex_pattern=moodle_pdf_re_pattern,
    ):
        if p.stem.endswith("_old") or p.stem.endswith("Instructions"):
            print(f"Skipping {p}")
            continue
        print(f"Processing {p}")
        process_pdf(p)


if __name__ == "__main__":
    main()
