import re
import ast
from urllib.parse import urlparse, unquote

def get_fields(card: dict) -> dict:

    """ Extract fields from card"""

    fields = {}

    for f in card.get("fields", []):
        field_id = (f.get("field") or {}).get("id")

        fields[field_id] = f.get("value")

    return fields

def safe_filename(name: str, default: str = "pipefy_brief") -> str:
    if not name:
        return default

    # Remove illegal characters
    name = re.sub(r'[<>:"/\\|?*]', "_", name)

    name = name.strip().rstrip(".")

    return name[:150] or default

# Normalise arrays and dictionaries into strings 
def format_value(raw):
    if raw is None:
        return ""

    # Lists (arrays)
    if isinstance(raw, (list, tuple, set)):
        items = []
        for x in raw:
            if x in (None, "", []):
                continue
            items.append(format_value(x).strip())
        return ", ".join([i for i in items if i])

    # Dictionaries
    if isinstance(raw, dict):
        for k in ("name", "title", "label", "value", "text"):
            if k in raw and raw[k] not in (None, "", []):
                return format_value(raw[k])
        # last resort
        return str(raw)
    
    s = str(raw).strip()
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                parsed = ast.literal_eval(s)
                if isinstance(parsed, list):
                    return ", ".join(str(x).strip() for x in parsed if str(x).strip())
            except Exception:
                pass
        return s

    return str(raw).strip()

def attachment_name(value):
    if not value:
        return ""

    if isinstance(value, list):
        return "\n".join(attachment_name(v) for v in value)

    if not isinstance(value, str):
        return str(value)

    try:
        path = urlparse(value).path
        filename = path.split("/")[-1]
        return unquote(filename)
    except Exception:
        return value

def bullet_format(pdf, text: str, w=0, line_h=7, bullet_indent=6, text_indent=12): # Need to look at what their agency font formatting will be for this
    # Make bullet points look like bullet points
    if not text:
        return

    # Normalise newlines
    lines = str(text).replace("\r\n", "\n").replace("\r", "\n").split("\n")

    for line in lines:
        line = line.rstrip()

        if line.strip().startswith("- "):
            bullet_text = line.strip()[2:].strip()  # remove "- "
            x0 = pdf.l_margin

            # Bullet
            pdf.set_x(x0 + bullet_indent)
            pdf.cell(0, line_h, "•", ln=0) # To be agency font bullet

            # Text (wrap)
            pdf.set_x(x0 + text_indent)
            pdf.multi_cell(w, line_h, bullet_text)

        else:
            
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(w, line_h, line)

def table_format(
    pdf,
    values,
    col_w,
    line_h=5,
    formatter=None,
    top_pad=0,
    bold_cols=(0, 2),
    font_regular=("source-sans-pro", "", 10),
    font_bold=("source-sans-pro-bold", "B", 10),
):
    # Help to wrap table text
    if formatter is None:
        formatter = lambda x: "" if x is None else str(x)

    texts = [formatter(v) for v in values]

    # calculate required row height
    max_lines = max(
        len(pdf.multi_cell(col_w, line_h, t, split_only=True))
        for t in texts
    )
    row_h = max_lines * line_h

    y = pdf.get_y()
    x0 = pdf.l_margin

    for i, text in enumerate(texts):
        x = x0 + i * col_w

        # Draw cell border
        pdf.rect(x, y, col_w, row_h)

        # Set font per column
        if i in bold_cols:
            pdf.set_font(*font_bold)
        else:
            pdf.set_font(*font_regular)

        # Write text
        pdf.set_xy(x, y + top_pad)
        pdf.multi_cell(col_w, line_h, text, align="L")

    pdf.set_y(y + row_h)



