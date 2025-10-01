from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def save_as_pdf(elements: List[str], size: int, output_path: Path):
    c = canvas.Canvas(str(output_path), pagesize=letter)
    x, y = 100, 700
    for i, element in enumerate(elements):
        c.drawString(x + (i % size) * 100, y - (i // size) * 100, element)
    c.save()


def save_as_image(elements: List[str], size: int, output_path: Path):
    img = Image.new("RGB", (800, 800), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for i, element in enumerate(elements):
        draw.text(
            (100 + (i % size) * 100, 100 + (i // size) * 100),
            element,
            fill="black",
            font=font,
        )
    img.save(output_path)
