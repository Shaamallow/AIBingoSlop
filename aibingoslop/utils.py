from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import black

# lightgrey
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle

# getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


def save_as_pdf(elements: List[str], size: int, output_path: Path):
    # Capitalize the first letter of each element
    elements = [elem[0].upper() + elem[1:] if elem else "" for elem in elements]

    # Create a PDF canvas
    c = canvas.Canvas(str(output_path), pagesize=letter)

    # Define styles
    # styles = getSampleStyleSheet()
    style = ParagraphStyle(
        name="BingoCell",
        fontName="Times-Roman",
        fontSize=12,
        alignment=TA_CENTER,
        leading=14,
    )

    # Create a table with grid lines
    cell_width = letter[0] / (size + 1)
    cell_height = letter[1] / (size + 1)
    data = [
        [Paragraph(elements[row * size + col], style) for col in range(size)]
        for row in range(size)
    ]

    table = Table(data, colWidths=[cell_width] * size, rowHeights=[cell_height] * size)
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 1, black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
                ("FONTSIZE", (0, 0), (-1, -1), 12),
            ]
        )
    )

    # Center the table on the page
    table.wrapOn(c, letter[0], letter[1])
    table.drawOn(c, inch, letter[1] - inch - table._height)  # type:ignore

    c.save()


def save_as_image(elements: List[str], size: int, output_path: Path):
    # Capitalize the first letter of each element
    elements = [elem[0].upper() + elem[1:] if elem else "" for elem in elements]

    # Calculate cell size and image dimensions
    cell_size = 100
    img_width = size * cell_size + 100
    img_height = size * cell_size + 100
    img = Image.new("RGB", (img_width, img_height), color="white")
    draw = ImageDraw.Draw(img)

    # Load Times New Roman font (fallback to default if not available)
    try:
        font = ImageFont.truetype("times.ttf", 14)
    except:
        font = ImageFont.load_default()

    # Draw grid and elements
    for i in range(size + 1):
        # Vertical lines
        draw.line(
            [(50 + i * cell_size, 50), (50 + i * cell_size, 50 + size * cell_size)],
            fill="black",
            width=1,
        )
        # Horizontal lines
        draw.line(
            [(50, 50 + i * cell_size), (50 + size * cell_size, 50 + i * cell_size)],
            fill="black",
            width=1,
        )

    for i, element in enumerate(elements):
        x = 50 + (i % size) * cell_size + cell_size // 2
        y = 50 + (i // size) * cell_size + cell_size // 2
        # Center text in the cell
        draw.text((x, y), element, fill="black", font=font, anchor="mm")

    img.save(output_path)
