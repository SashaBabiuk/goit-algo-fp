"""Greedy and dynamic-programming food selection."""

from __future__ import annotations

from collections.abc import Mapping

Food = Mapping[str, Mapping[str, int]]


def greedy_algorithm(items: Food, budget: int) -> tuple[list[str], int]:
    if budget < 0:
        raise ValueError("Бюджет не може бути від'ємним.")
    selected: list[str] = []
    spent = 0
    for name, data in sorted(
        items.items(), key=lambda pair: pair[1]["calories"] / pair[1]["cost"], reverse=True
    ):
        if spent + data["cost"] <= budget:
            selected.append(name)
            spent += data["cost"]
    return selected, spent


def dynamic_programming(items: Food, budget: int) -> tuple[list[str], int, int]:
    if budget < 0:
        raise ValueError("Бюджет не може бути від'ємним.")
    names = list(items)
    best = [0] * (budget + 1)
    choices: list[list[str]] = [[] for _ in range(budget + 1)]
    for name in names:
        cost, calories = items[name]["cost"], items[name]["calories"]
        for current in range(budget, cost - 1, -1):
            candidate = best[current - cost] + calories
            if candidate > best[current]:
                best[current] = candidate
                choices[current] = choices[current - cost] + [name]
    selected = choices[budget]
    return selected, sum(items[name]["cost"] for name in selected), best[budget]


ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


if __name__ == "__main__":
    print("Жадібний:", greedy_algorithm(ITEMS, 100))
    print("Динамічне програмування:", dynamic_programming(ITEMS, 100))
