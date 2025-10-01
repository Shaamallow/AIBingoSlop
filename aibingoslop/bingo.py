import random
from pathlib import Path
from typing import List

from .utils import save_as_image, save_as_pdf

CHART_SIZES = {
    "bullet": 3,
    "blitz": 5,
    "normal": 7,
    "100dayslater": 9,
}


def read_elements(input_file: Path) -> List[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f if line.strip()]


def generate_bingo_charts(
    input_file: Path,
    chart_type: str,
    num_players: int,
    output_dir: Path,
    output_format: str,
):
    size = CHART_SIZES.get(chart_type.lower())
    if not size:
        raise ValueError(f"Invalid chart type: {chart_type}")

    elements = read_elements(input_file)
    required = size * size
    if len(elements) < required:
        raise ValueError(
            f"Not enough elements in the input file. Need at least {required}."
        )

    selected = random.sample(elements, required)
    shuffled = [random.sample(selected, required) for _ in range(num_players)]

    output_dir.mkdir(parents=True, exist_ok=True)
    for i, chart in enumerate(shuffled, 1):
        if output_format == "pdf":
            save_as_pdf(chart, size, output_dir / f"bingo_{i}.pdf")
        else:
            save_as_image(chart, size, output_dir / f"bingo_{i}.png")
