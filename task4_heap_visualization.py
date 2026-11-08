"""Binary min-heap visualization."""

from __future__ import annotations

import heapq
import uuid


class HeapNode:
    def __init__(self, value: int, color: str = "skyblue") -> None:
        self.value = value
        self.color = color
        self.id = str(uuid.uuid4())
        self.left: HeapNode | None = None
        self.right: HeapNode | None = None


def heap_to_tree(values: list[int]) -> HeapNode | None:
    if not values:
        return None
    heap = values[:]
    heapq.heapify(heap)
    nodes = [HeapNode(value) for value in heap]
    for index, node in enumerate(nodes):
        left, right = 2 * index + 1, 2 * index + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def visualize_heap(values: list[int]):
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
    except ImportError as error:
        raise RuntimeError(
            "Для візуалізації встановіть залежності з requirements.txt."
        ) from error
    root = heap_to_tree(values)
    if root is None:
        raise ValueError("Купа не може бути порожньою.")
    graph = nx.DiGraph()
    positions: dict[str, tuple[float, float]] = {}
    labels: dict[str, int] = {}
    colors: dict[str, str] = {}

    def add(node: HeapNode, x: float, y: float, spread: float) -> None:
        graph.add_node(node.id)
        positions[node.id] = (x, y)
        labels[node.id], colors[node.id] = node.value, node.color
        for child, offset in ((node.left, -spread), (node.right, spread)):
            if child is not None:
                graph.add_edge(node.id, child.id)
                add(child, x + offset, y - 1, spread / 2)

    add(root, 0, 0, 1)
    figure, axis = plt.subplots(figsize=(10, 6))
    nx.draw(graph, positions, labels=labels, node_color=list(colors.values()),
            node_size=2200, arrows=False, ax=axis)
    axis.set_title("Бінарна мін-купa")
    return figure, axis


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    visualize_heap([4, 1, 7, 3, 8, 2, 5])
    plt.show()
