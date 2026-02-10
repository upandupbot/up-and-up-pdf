from functions import get_fields, format_value, bullet_format, table_format
from pipefy_helpers import fetch_card
from fpdf import FPDF
from layout import sections
from pathlib import Path

def build_pdf(card_id: int) -> bytes:
    base = Path(__file__).resolve().parent

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_font("source-sans-pro", "", str(base / "source-sans-pro.regular.ttf"), uni=True)
    pdf.add_font("source-sans-pro-bold", "B", str(base / "source-sans-pro.bold.ttf"), uni=True)
    pdf.set_font("source-sans-pro", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

# ---------------------------------------------------------------------------------------------------
#                                       HEADER + LOGO
# ---------------------------------------------------------------------------------------------------

    logo_path = base / "up_slip_wide_spacing.png"
    usable_width = pdf.w - pdf.l_margin - pdf.r_margin
    # Header logo
    pdf.image(
        str(logo_path),
        x=pdf.l_margin,   # align with left margin
        y=10,             # distance from top
        w=usable_width    # width in mm (adjust if needed)
    )
    pdf.ln(20)  # push content down so it doesn't overlap

    card = fetch_card(card_id)
    fields = get_fields(card)

    filename = card.get("title") or f"Card {card_id}"


# ---------------------------------------------------------------------------------------------------
#                                       TOP OF TABLE
# ---------------------------------------------------------------------------------------------------
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_x(pdf.l_margin)
    
    pdf.set_font("source-sans-pro-bold", "B", 16)
    pdf.multi_cell(0, 10, filename, align="L")
    pdf.ln(8)

    pdf.set_font("source-sans-pro-bold", "B", 14)
    pdf.cell(0, 10, f"Brief Type: {fields.get('brief_type', 'N/A')}", ln=True, align="L")

    pdf.set_font("source-sans-pro", "", 10)

    usable_w = pdf.w - pdf.l_margin - pdf.r_margin
    col_w = usable_w / 4
    row_h = 8

    pdf.ln(2)

    top_rows = [
    ("Account Manager", fields.get("account_manager_1"), "Traffic Manager", fields.get("trafficker")),
    ("Client", fields.get("client_db_name"), "Product", fields.get("product")),
    ("Division", fields.get("division"), "Client Contact", fields.get("client_contact_name")),
    ("Job Deadline", fields.get("job_deadline"), "Campaign year", fields.get("campaign_year")),
    ("Go-Live Date", fields.get("go_live_date"), "Campaign Quarter", fields.get("quarter")),
]

    for row in top_rows:
    
        pdf.set_font("source-sans-pro-bold", "B", 10)
        table_format(
            pdf,
            row,
            col_w,
            line_h=row_h,
            formatter=format_value
        )

    pdf.ln(4)

# ---------------------------------------------------------------------------------------------------
#                                           MAIN BRIEF
# ---------------------------------------------------------------------------------------------------

    for section in sections:
        rendered_section = False

        for item in section["fields"]:
            raw_value = item["get"](fields)
            value = format_value(raw_value) # Normalise all values into strings

            if not value:
                continue

            if not rendered_section:
                pdf.set_font("source-sans-pro-bold", "B", 14)
                pdf.cell(0, 10, section["section"], ln=True, align="L")
                pdf.ln(2)
                rendered_section = True

            label = item["label"]

            pdf.set_font("source-sans-pro-bold", "B", 12)
            pdf.multi_cell(0, 7, f"{label}:")
            pdf.set_x(pdf.l_margin)
            pdf.set_font("source-sans-pro", "", 12)
            bullet_format(pdf, value, w=0, line_h=7)
            pdf.ln(2)

        if rendered_section:
            pdf.ln(3)

    out = pdf.output(dest="S")
    return out if isinstance(out, (bytes, bytearray)) else out.encode("latin-1")
