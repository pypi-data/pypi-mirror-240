#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-11-10
Purpose: ChatGPT HTML file to a list of GPTs
"""

import argparse
from pathlib import Path
from gpt_editor_utils.config import CHATGPT_BASE_URL


def extract_gpt_a_tags(html_content: str) -> list:
    from bs4 import BeautifulSoup
    import re

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract all 'a' tags with href matching the given regex
    regex = re.compile(r"^/g/g-[-\w\d]+$")
    matching_tags = soup.find_all("a", href=regex)

    return matching_tags


def extract_a_tag_data(a_tag) -> dict:
    """
    Extract structured data from an 'a' tag provided in the format specified in the user's request.
    The SVGs are ignored as per the instruction.
    """
    # from bs4 import BeautifulSoup
    #
    # # Parse the 'a' tag with BeautifulSoup
    # soup = BeautifulSoup(a_tag, "html.parser")

    # Extract the class from the 'a' tag
    # a_class = a_tag.get('class', [])

    # Extract the href from the 'a' tag
    href = a_tag.get("href")

    # Extract the img tag's src and alt attributes
    img = a_tag.find("img")
    img_src = img.get("src") if img else None
    img_alt = img.get("alt") if img else None

    # Extract the text content, ignoring any SVG elements
    text_div = a_tag.find(
        "div",
        class_="grow overflow-hidden text-ellipsis whitespace-nowrap text-sm text-token-text-primary",
    )
    text_content = text_div.get_text(strip=True) if text_div else None

    splitted = href.removeprefix("/g/").split("-", 2)

    # Structure the data in a dictionary
    data = {
        # 'class': a_class,
        # "href": href,
        "id": splitted[1],
        "slug": splitted[2],
        "handle": href,
        "url": f"{CHATGPT_BASE_URL}{href}",
        "img_src": img_src,
        # "img_alt": img_alt,
        # "text_content": text_content,
        "name": text_content,
    }

    return data


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="ChatGPT HTML file to a list of GPTs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # input Path
    parser.add_argument(
        "input",
        metavar="PATH",
        help="Input HTML file",
        type=Path,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    input_file = args.input

    # Read the HTML file
    html_content = input_file.read_text()

    # Extract all 'a' tags with href matching the given regex
    matching_tags = extract_gpt_a_tags(html_content)

    # Extract structured data from each 'a' tag
    data_list = []
    for a_tag in matching_tags:
        data = extract_a_tag_data(a_tag)
        if data["name"] is None:
            continue
        data_list.append(data)

    # print json
    import json

    print(json.dumps(data_list, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
