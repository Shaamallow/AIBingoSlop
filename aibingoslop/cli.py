from pathlib import Path

import typer

from .bingo import generate_bingo_charts

app = typer.Typer()


@app.command()
def generate(
    input_file: Path = typer.Argument(..., help="Path to the input .txt file"),
    chart_type: str = typer.Argument(
        ..., help="Type of bingo chart: bullet, blitz, normal, 100dayslater"
    ),
    num_players: int = typer.Argument(..., help="Number of players"),
    output_dir: Path = typer.Argument(..., help="Path to the output directory"),
    output_format: str = typer.Option("pdf", help="Output format: pdf or img"),
):
    generate_bingo_charts(
        input_file, chart_type, num_players, output_dir, output_format
    )


if __name__ == "__main__":
    app()
