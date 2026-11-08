"""Monte Carlo simulation of sums from two dice."""

from __future__ import annotations

import random
from collections import Counter


def simulate_dice(
    rolls: int = 100_000, seed: int | None = None
) -> tuple[dict[int, int], dict[int, float]]:
    if isinstance(rolls, bool) or not isinstance(rolls, int) or rolls <= 0:
        raise ValueError("Кількість кидків має бути додатним цілим числом.")
    generator = random.Random(seed)
    counts = Counter(
        generator.randint(1, 6) + generator.randint(1, 6) for _ in range(rolls)
    )
    probabilities = {total: counts[total] / rolls for total in range(2, 13)}
    return dict(counts), probabilities


def analytical_probabilities() -> dict[int, float]:
    return {
        total: (6 - abs(7 - total)) / 36
        for total in range(2, 13)
    }


if __name__ == "__main__":
    _, simulated = simulate_dice(seed=42)
    analytical = analytical_probabilities()
    print("Сума | Монте-Карло | Аналітична")
    for total in range(2, 13):
        print(f"{total:>4} | {simulated[total]:>11.4%} | {analytical[total]:>10.4%}")
