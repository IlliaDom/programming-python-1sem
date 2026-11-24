
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Preformatted,
    HRFlowable
)

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "report_lab46.md"
OUTPUT_FILE = BASE_DIR / "report_lab46.pdf"

font_path = Path("C:/Windows/Fonts/arial.ttf")
bold_path = Path("C:/Windows/Fonts/arialbd.ttf")

pdfmetrics.registerFont(TTFont("Arial", str(font_path)))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(bold_path)))

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="MainTitle",
    fontName="Arial-Bold",
    fontSize=18,
    leading=23,
    alignment=TA_CENTER,
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name="Heading",
    fontName="Arial-Bold",
    fontSize=14,
    leading=18,
    spaceBefore=12,
    spaceAfter=7
))

styles.add(ParagraphStyle(
    name="SubHeading",
    fontName="Arial-Bold",
    fontSize=12,
    leading=16,
    spaceBefore=9,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name="BodyTextUA",
    fontName="Arial",
    fontSize=10.5,
    leading=15,
    alignment=4,
    spaceAfter=7
))

styles.add(ParagraphStyle(
    name="CodeText",
    fontName="Arial",
    fontSize=9,
    leading=13,
    leftIndent=8,
    spaceBefore=4,
    spaceAfter=8,
    backColor=colors.whitesmoke,
    borderPadding=7
))

story = []
lines = INPUT_FILE.read_text(encoding="utf-8").splitlines()

in_code = False
code_lines = []

def format_inline(text):
    text = escape(text)
    text = re.sub(
        r"\*\*(.*?)\*\*",
        r"<b>\1</b>",
        text
    )
    text = re.sub(
        r"`(.*?)`",
        r'<font name="Arial-Bold">\1</font>',
        text
    )
    return text

for line in lines:
    stripped = line.strip()

    if stripped.startswith("```"):
        if not in_code:
            in_code = True
            code_lines = []
        else:
            story.append(Preformatted(
                "\n".join(code_lines),
                styles["CodeText"]
            ))
            in_code = False
        continue

    if in_code:
        code_lines.append(line)
        continue

    if not stripped:
        story.append(Spacer(1, 3))
    elif stripped.startswith("# "):
        story.append(Paragraph(
            format_inline(stripped[2:]),
            styles["MainTitle"]
        ))
    elif stripped.startswith("## "):
        story.append(Paragraph(
            format_inline(stripped[3:]),
            styles["Heading"]
        ))
    elif stripped.startswith("**") and stripped.endswith("**"):
        story.append(Paragraph(
            format_inline(stripped),
            styles["BodyTextUA"]
        ))
    elif stripped.startswith("- "):
        story.append(Paragraph(
            "• " + format_inline(stripped[2:]),
            styles["BodyTextUA"]
        ))
    else:
        story.append(Paragraph(
            format_inline(stripped),
            styles["BodyTextUA"]
        ))

def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Arial", 9)
    canvas.drawCentredString(
        A4[0] / 2,
        1.1 * cm,
        str(document.page)
    )
    canvas.restoreState()

document = SimpleDocTemplate(
    str(OUTPUT_FILE),
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm
)

document.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
)

print("PDF успішно створено:", OUTPUT_FILE.name)
