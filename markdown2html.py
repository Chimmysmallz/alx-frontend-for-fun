#!/usr/bin/python3

"""
This module converts a Markdown file to an HTML file.

Usage: python3 markdown2html.py <input-file> <output-file>

Arguments:
    input-file: The name of the Markdown file to be converted to HTML.
    output-file: The name of the output HTML file.
"""

import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Converts the given Markdown file to HTML and writes the output to the given output file.
    """
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()
        html = markdown.markdown(markdown_text)
        with open(output_file, 'w') as html_file:
            html_file.write(html)


if __name__ == "__main__":
    # Check that the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input-file> <output-file>", file=sys.stderr)
        sys.exit(1)

    # Get the input and output filenames
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    try:
        with open(input_file, 'r'):
            pass
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown to HTML and write to the output file
    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)
