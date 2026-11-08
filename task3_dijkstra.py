"""Dijkstra shortest paths using a binary heap."""

from __future__ import annotations

import heapq
from collections.abc import Mapping

Graph = Mapping[str, Mapping[str, float]]


def dijkstra(graph: Graph, start: str) -> tuple[dict[str, float], dict[str, str | None]]:
    if start not in graph:
        raise KeyError(f"Початкова вершина {start!r} відсутня в графі.")
    distances = {vertex: float("inf") for vertex in graph}
    previous: dict[str, str | None] = {vertex: None for vertex in graph}
    distances[start] = 0
    heap: list[tuple[float, str]] = [(0, start)]

    while heap:
        distance, vertex = heapq.heappop(heap)
        if distance != distances[vertex]:
            continue
        for neighbour, weight in graph[vertex].items():
            if weight < 0:
                raise ValueError("Алгоритм Дейкстри не підтримує від'ємні ваги.")
            if neighbour not in distances:
                raise KeyError(f"Вершина {neighbour!r} відсутня в графі.")
            candidate = distance + weight
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                previous[neighbour] = vertex
                heapq.heappush(heap, (candidate, neighbour))
    return distances, previous


def restore_path(previous: Mapping[str, str | None], target: str) -> list[str]:
    path: list[str] = []
    current: str | None = target
    while current is not None:
        path.append(current)
        current = previous.get(current)
    if not path or path[-1] not in previous:
        return []
    return path[::-1]


EXAMPLE_GRAPH: dict[str, dict[str, float]] = {
    "A": {"B": 4, "C": 2},
    "B": {"C": 1, "D": 5},
    "C": {"B": 1, "D": 8, "E": 10},
    "D": {"E": 2, "F": 6},
    "E": {"F": 3},
    "F": {},
}


if __name__ == "__main__":
    distances, previous = dijkstra(EXAMPLE_GRAPH, "A")
    print("Відстані:", distances)
    print("Шлях до F:", restore_path(previous, "F"))
