import re
import os


def _get(tag_content: str, key: str) -> str | None:
    m = re.search(rf'{key}=([^\s"<][^\n<]*?)(?=\s+\w+=|\s*$)', tag_content, re.DOTALL)
    if not m:
        m = re.search(rf'{key}=(.*?)(?=\s+\w+=|\s*$)', tag_content, re.DOTALL)
    return m.group(1).strip() if m else None


def run(inner: str) -> str:
    path      = _get(inner, "path")
    operation = _get(inner, "operation") or "extract_text"

    if not path:
        return "ERROR - 'path' parameter is required."

    if not os.path.isfile(path):
        return f"ERROR - File not found: {path}"

    try:
        import pypdf

        reader = pypdf.PdfReader(path)

        if operation == "page_count":
            return f"Page count: {len(reader.pages)}"

        elif operation == "extract_text":
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            return text

        else:
            return f"ERROR - Unknown operation '{operation}'. Supported: extract_text, page_count"

    except ImportError:
        return "ERROR - pypdf is not installed. Run: pip install pypdf"
    except Exception as e:
        return f"ERROR - {e}"