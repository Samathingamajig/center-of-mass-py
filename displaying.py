from rich.console import Console
from rich.table import Column, Table

from shapes import calculateX, calculateY


def format_float(num: float):
    return str(float(f"{num:.5f}"))


def display(shapes):
    tableX = Table(
        Column("Shape #", justify="center"),
        Column("Type", justify="center"),
        Column("Add/Sub", justify="center"),
        Column("x", justify="center"),
        Column("Area", justify="center"),
        Column("x * Area", justify="center"),
        title="Calculations for x-bar",
        show_lines=True,
    )

    for i, shape in enumerate(shapes, start=1):
        tableX.add_row(
            str(i),
            type(shape).__name__,
            "Sub" if shape.mInverted == -1 else "Add",
            format_float(shape.x()),
            format_float(shape.area()),
            format_float(shape.x() * shape.area()),
        )

    tableX.add_row(
        "Total",
        "",
        "",
        "",
        format_float(sum(shape.area() for shape in shapes)),
        format_float(sum(shape.x() * shape.area() for shape in shapes)),
    )

    tableY = Table(
        Column("Shape #", justify="center"),
        Column("Type", justify="center"),
        Column("Add/Sub", justify="center"),
        Column("y", justify="center"),
        Column("Area", justify="center"),
        Column("y * Area", justify="center"),
        title="Calculations for y-bar",
        show_lines=True,
    )

    for i, shape in enumerate(shapes, start=1):
        tableY.add_row(
            str(i),
            type(shape).__name__,
            "Sub" if shape.mInverted == -1 else "Add",
            format_float(shape.y()),
            format_float(shape.area()),
            format_float(shape.y() * shape.area()),
        )

    tableY.add_row(
        "Total",
        "",
        "",
        "",
        format_float(sum(shape.area() for shape in shapes)),
        format_float(sum(shape.y() * shape.area() for shape in shapes)),
    )

    console = Console()
    console.print(tableX)
    console.print(f"x-bar = {calculateX()}")
    console.print(f"x-bar = {calculateX():.3f}")
    console.print(f"x-bar = {calculateX():.2f}")
    console.print(f"x-bar = {calculateX():.1f}")
    console.print(tableY)
    console.print(f"y-bar = {calculateY()}")
    console.print(f"y-bar = {calculateY():.3f}")
    console.print(f"y-bar = {calculateY():.2f}")
    console.print(f"y-bar = {calculateY():.1f}")