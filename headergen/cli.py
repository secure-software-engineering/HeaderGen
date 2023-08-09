import click
import uvicorn

from headergen import headergen
from headergen.server import app


@click.group()
def cli():
    """CLI tool"""
    pass


@cli.command()
@click.option(
    "-i", "--input", required=True, help="Path of the input Notebook/Python script"
)
@click.option("-o", "--output", default=".", help="Output path")
def generate(input, output):
    """Generate HeaderGen linted notebook"""
    analysis_meta = headergen.start_headergen(input, output, debug_mode=True)


@cli.command()
def server():
    """Start Server"""
    uvicorn.run(app, host="0.0.0.0", port=54068)
