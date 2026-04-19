## PDF Action

Use the `custom_pdf` tag to work with PDF files.

### Syntax

```
<custom_pdf>
path=<path_to_pdf>  operation=<operation>
</custom_pdf>
```

### Operations

- **extract_text** — Extracts all text from the PDF and returns it.
- **page_count** — Returns the total number of pages in the PDF.

### Examples

Count pages:
```
<custom_pdf>
path=./docs/report.pdf  operation=page_count
</custom_pdf>
```

Extract text:
```
<custom_pdf>
path=./docs/report.pdf  operation=extract_text 
</custom_pdf>
```

### Notes
- Do not attempt PDF operations on non-PDF files.