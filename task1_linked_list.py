"""Singly linked-list operations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Node:
    value: int
    next: Node | None = None


def from_iterable(values: Iterable[int]) -> Node | None:
    head: Node | None = None
    tail: Node | None = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            assert tail is not None
            tail.next = node
        tail = node
    return head


def to_list(head: Node | None) -> list[int]:
    values: list[int] = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


def reverse_linked_list(head: Node | None) -> Node | None:
    previous: Node | None = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous, current = current, following
    return previous


def sort_linked_list(head: Node | None) -> Node | None:
    """Sort a linked list in-place with merge sort."""
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next
    right = slow.next
    slow.next = None
    return merge_sorted_lists(sort_linked_list(head), sort_linked_list(right))


def merge_sorted_lists(first: Node | None, second: Node | None) -> Node | None:
    dummy = Node(0)
    tail = dummy
    while first is not None and second is not None:
        if first.value <= second.value:
            tail.next, first = first, first.next
        else:
            tail.next, second = second, second.next
        tail = tail.next
    tail.next = first if first is not None else second
    return dummy.next


if __name__ == "__main__":
    values = from_iterable([4, 2, 1, 3])
    print("Відсортований список:", to_list(sort_linked_list(values)))
    print("Реверс:", to_list(reverse_linked_list(from_iterable([1, 2, 3]))))
