"""
Text to PDF application.
"""
import argparse
import sys
from pathlib import Path
from typing import Optional

from markdown_it import MarkdownIt
from weasyprint import HTML  # type: ignore
from weasyprint.text.fonts import FontConfiguration  # type: ignore


def read_input(input_path: Optional[str] = None) -> str:
    """Read content from file or stdin."""
    if input_path:
        resolved_path = Path(input_path).resolve()
        assert resolved_path.exists(), f"Unable to read from path: {resolved_path}"
        return resolved_path.read_text()

    return sys.stdin.read()


def md_to_html(content: str) -> str:
    """Convert markdown content to HTML."""
    md = MarkdownIt()
    html_content = md.render(content)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: system-ui, -apple-system, sans-serif;
                line-height: 1.5;
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
            }}
            pre {{
                background: #f5f5f5;
                padding: 1rem;
                border-radius: 4px;
                overflow-x: auto;
            }}
            code {{
                font-family: ui-monospace, monospace;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """


def generate_pdf(content: str, output_path: str, from_md: bool = False) -> None:
    """Generate PDF from content."""
    if from_md:
        content = md_to_html(content)

    font_config = FontConfiguration()

    HTML(string=content).write_pdf(
        output_path,
        font_config=font_config,
        # Enable PDF forms and links
        presentational_hints=True,
    )


def main() -> None:
    """Main command-line entry-point."""
    parser = argparse.ArgumentParser(
        description="Convert text or Markdown files to a PDF file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --output output.pdf input.txt
  %(prog)s --output output.pdf input.txt --markdown
  echo "Hello World" | %(prog)s -o output.pdf
        """,
    )

    parser.add_argument(
        "-o", "--output", metavar="OUTPUT_PATH", help="Output PDF file path"
    )
    parser.add_argument(
        "input",
        metavar="INPUT_PATH",
        nargs="?",
        help="Input file (omit to read from stdin)",
    )
    parser.add_argument(
        "--markdown",
        "-m",
        action="store_true",
        help="Process input as Markdown and render it.",
    )

    args = parser.parse_args()

    try:
        content = read_input(args.input)
        generate_pdf(content, args.output, args.markdown)

        print(f"PDF generated successfully: {args.output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
