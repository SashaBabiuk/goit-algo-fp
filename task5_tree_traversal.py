"""Iterative DFS and BFS traversals with step colors."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def dfs(root: TreeNode | None) -> list[TreeNode]:
    if root is None:
        return []
    order: list[TreeNode] = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return order


def bfs(root: TreeNode | None) -> list[TreeNode]:
    if root is None:
        return []
    order: list[TreeNode] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return order


def traversal_colors(nodes: list[TreeNode]) -> dict[int, str]:
    total = max(len(nodes) - 1, 1)
    return {
        id(node): f"#{int(18 + 180 * index / total):02X}"
        f"{int(80 + 120 * index / total):02X}"
        f"{int(220 - 130 * index / total):02X}"
        for index, node in enumerate(nodes)
    }


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("DFS:", [node.value for node in dfs(tree)])
    print("BFS:", [node.value for node in bfs(tree)])
    print("Кольори DFS:", traversal_colors(dfs(tree)))
