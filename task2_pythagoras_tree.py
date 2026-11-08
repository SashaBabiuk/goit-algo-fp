"""Recursive Pythagoras tree fractal visualization."""

from __future__ import annotations

import math
from collections.abc import Callable


def draw_pythagoras_tree(level: int, size: float = 1.0, angle: float = 0.0):
    """Draw and return a Pythagoras tree figure for the requested recursion level."""
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("Рівень рекурсії має бути невід'ємним цілим числом.")
    try:
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon
    except ImportError as error:
        raise RuntimeError(
            "Для візуалізації встановіть залежності з requirements.txt."
        ) from error

    figure, axis = plt.subplots(figsize=(10, 8))

    def square(x: float, y: float, side: float, direction: float, depth: int) -> None:
        dx = side * math.cos(direction)
        dy = side * math.sin(direction)
        corners = [(x, y), (x + dx, y + dy)]
        perpendicular = direction + math.pi / 2
        px, py = side * math.cos(perpendicular), side * math.sin(perpendicular)
        corners.extend([(x + dx + px, y + dy + py), (x + px, y + py)])
        axis.add_patch(Polygon(corners, closed=True, color=plt.cm.YlGn(depth / max(level, 1))))
        if depth == 0:
            return
        apex_x, apex_y = x + dx + px, y + dy + py
        child_side = side / math.sqrt(2)
        square(x + px, y + py, child_side, direction + math.pi / 4, depth - 1)
        square(apex_x, apex_y, child_side, direction - math.pi / 4, depth - 1)

    square(-size / 2, 0, size, angle, level)
    axis.set_aspect("equal")
    axis.autoscale_view()
    axis.axis("off")
    axis.set_title(f"Дерево Піфагора, рівень рекурсії: {level}")
    return figure, axis


if __name__ == "__main__":
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument("level", type=int, nargs="?", default=8)
    args = parser.parse_args()
    draw_pythagoras_tree(args.level)
    plt.show()
