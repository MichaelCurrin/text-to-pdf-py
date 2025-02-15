# Notes

## Possible choices

For PDF generation, main options:

1. ReportLab: Industry standard, very stable, extensive features
   - Pros: Robust, well-maintained, great for complex layouts
   - Cons: Lower level API, steeper learning curve

2. WeasyPrint: HTML/CSS to PDF converter
   - Pros: Works with HTML/CSS, good for web-style documents
   - Cons: Requires external dependencies, can be tricky to install

3. pdfkit + wkhtmltopdf: HTML to PDF using wkhtmltopdf
   - Pros: Good HTML rendering, uses WebKit engine
   - Cons: Requires external wkhtmltopdf installation

For Markdown parsing:
1. markdown-it-py: Modern, feature-rich parser
   - Pros: Extensive plugin system, CommonMark compliant
   - Cons: Relatively newer

2. mistune: Fast and extensible
   - Pros: Pure Python, good performance
   - Cons: Less feature-rich than alternatives

3. Python-Markdown: Well-established
   - Pros: Stable, good extension ecosystem
   - Cons: Some CommonMark incompatibilities

## Recommended combination

WeasyPrint + markdown-it-py, because:
- WeasyPrint provides excellent HTML/CSS rendering
- markdown-it-py gives us a modern, compliant Markdown parser
- Both are actively maintained and have good security track records
