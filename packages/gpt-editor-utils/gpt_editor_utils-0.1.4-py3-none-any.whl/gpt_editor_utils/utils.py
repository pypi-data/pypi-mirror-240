import unicodedata
import re
import os
from pathlib import Path

from typing import Iterable


def find_files(
    dir_path: os.PathLike,
    glob_pattern: str | None = None,
    recursive: bool = False,
    regex_pattern: str | None = None,
) -> Iterable[Path]:
    dir_path = Path(dir_path)
    if glob_pattern is None:
        files = dir_path.iterdir()
    else:
        if recursive:
            files = dir_path.rglob(glob_pattern)
        else:
            files = dir_path.glob(glob_pattern)

    if regex_pattern is not None:
        files = filter(lambda f: re.search(regex_pattern, f.name), files)
    return files


# cSpell:disable
def pdf_to_text_pymupdf(p: os.PathLike) -> list[str]:
    import fitz

    doc = fitz.open(p)  # open document # type: ignore
    texts = [page.get_text() for page in doc]
    return texts


# cSpell:enable


def slugify(value, allow_unicode=False) -> str:
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


# Function to check if a string is plain text, including Unicode
def is_plain_text(string):
    try:
        # Attempt to encode the string in ASCII
        string.encode("ascii")
    except UnicodeEncodeError:
        # If it fails, it's not plain ASCII text, now let's check for printable unicode characters
        for char in string:
            if not (
                unicodedata.category(char).startswith("C")
                or unicodedata.category(char).startswith("Z")
            ):
                # If the character is not a control character or a separator, return False
                return False
    # If all characters passed the checks, it's plain text
    return True


# # Check if the example string is plain text
# is_plain_text(input_string)
#
# def contains_binary(string: str) -> bool:
#     return bool(re.search(r"\b[01]+\b", string))
#
