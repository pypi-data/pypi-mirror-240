#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-11-11
Purpose: claude.ai html to chat list
"""

import argparse
from pathlib import Path
from gpt_editor_utils.config import CLAUDE_BASE_URL


def extract_gpt_a_tags(html_content: str) -> list:
    from bs4 import BeautifulSoup
    import re

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    uuid4_regex = (
        r"[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}"
    )

    # Extract all 'a' tags with href matching the given regex
    regex = re.compile(rf"^/chat/{uuid4_regex}$")
    matching_tags = soup.find_all("a", href=regex)

    return matching_tags


def extract_a_tag_data(a_tags) -> list[dict]:
    # from bs4 import BeautifulSoup
    #
    # soup = BeautifulSoup(a_tags, "html.parser")
    #
    # # Find all <a> tags
    # links = soup.find_all("a")
    #
    # # Extract the href attribute and text for each <a> tag
    # # extracted_data = [(link["href"], link.span.text.strip()) for link in links]

    d_l = []
    for link in a_tags:
        d = {}
        d["href"] = link["href"]
        d["title"] = link.span.text.strip()
        d["url"] = CLAUDE_BASE_URL + link["href"]
        d_l.append(d)

    # Now `extracted_data` contains tuples of (link, text) for each <a> tag
    return d_l


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="claude.ai html to chat list",
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

    # Read the HTML file
    html_content = Path(args.input).read_text()

    # Extract all 'a' tags with href matching the given regex
    matching_tags = extract_gpt_a_tags(html_content)

    # Extract structured data from each 'a' tag
    data_list = extract_a_tag_data(matching_tags)

    # print json
    import json

    print(json.dumps(data_list, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
