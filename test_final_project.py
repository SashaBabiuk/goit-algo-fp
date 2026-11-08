import unittest

from task1_linked_list import (
    from_iterable,
    merge_sorted_lists,
    reverse_linked_list,
    sort_linked_list,
    to_list,
)
from task3_dijkstra import EXAMPLE_GRAPH, dijkstra, restore_path
from task5_tree_traversal import TreeNode, bfs, dfs, traversal_colors
from task6_food_optimization import ITEMS, dynamic_programming, greedy_algorithm
from task7_monte_carlo import analytical_probabilities, simulate_dice


class FinalProjectTests(unittest.TestCase):
    def test_linked_list_operations(self) -> None:
        head = from_iterable([4, 1, 3, 2])
        self.assertEqual(to_list(sort_linked_list(head)), [1, 2, 3, 4])
        self.assertEqual(to_list(reverse_linked_list(from_iterable([1, 2, 3]))), [3, 2, 1])
        self.assertEqual(
            to_list(merge_sorted_lists(from_iterable([1, 3]), from_iterable([2, 4]))),
            [1, 2, 3, 4],
        )

    def test_dijkstra(self) -> None:
        distances, previous = dijkstra(EXAMPLE_GRAPH, "A")
        self.assertEqual(distances["F"], 13)
        self.assertEqual(restore_path(previous, "F"), ["A", "C", "B", "D", "E", "F"])

    def test_iterative_traversals_and_colors(self) -> None:
        tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual([node.value for node in dfs(tree)], [1, 2, 4, 5, 3])
        self.assertEqual([node.value for node in bfs(tree)], [1, 2, 3, 4, 5])
        colors = traversal_colors(bfs(tree))
        self.assertEqual(len(colors), 5)
        self.assertTrue(all(color.startswith("#") and len(color) == 7 for color in colors.values()))

    def test_food_optimization(self) -> None:
        greedy, spent = greedy_algorithm(ITEMS, 100)
        selected, dynamic_spent, calories = dynamic_programming(ITEMS, 100)
        self.assertLessEqual(spent, 100)
        self.assertLessEqual(dynamic_spent, 100)
        self.assertGreaterEqual(calories, sum(ITEMS[item]["calories"] for item in greedy))
        self.assertEqual(set(selected), {"pizza", "pepsi", "cola", "potato"})
        self.assertEqual(calories, 970)

    def test_dice_simulation(self) -> None:
        counts, probabilities = simulate_dice(100_000, seed=42)
        self.assertEqual(sum(counts.values()), 100_000)
        self.assertAlmostEqual(sum(probabilities.values()), 1)
        for total, expected in analytical_probabilities().items():
            self.assertAlmostEqual(probabilities[total], expected, delta=0.01)


if __name__ == "__main__":
    unittest.main()
