"""Utility functions for traversing graphs."""

from .structs import Graph, Node, Edge


def breadth_first(start_node: Node):
    """An implementation of breadth-first traversal."""

    start_node.visited = True
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        for node in current_node.edges:
            if not node.visited:
                node.visited = True
                queue.append(node)


def depth_first(start_node: Node):
    """An implementation of depth-first traversal."""

    start_node.visited = True
    for node in start_node.edges:
        if not node.visited:
            depth_first(node)
