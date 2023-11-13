"""Classes for Nodes, Edges, and Graphs."""

from __future__ import annotations
from typing import List, Union

SupportedValueType = Union[float, int, str, bool, None]


class Node:
    def __init__(self, value: SupportedValueType = None, visited: bool = False):
        """Initialize a node with a value and an empty list of edges."""
        self.value: SupportedValueType = value
        self.visited: bool = visited
        self.edges: List[Edge] = []

    def add_edge(self, node: Node) -> None:
        """Add node to self.edges."""
        self.edges.append(node)

    def remove_edge(self, node: Node) -> None:
        """Remove first occurrence of node from self.edges.
        Raises ValueError if node is not found."""
        self.edges.remove(node)


class Edge:
    def __init__(self, node1: Node, node2: Node, value: SupportedValueType = None):
        """Initialize an edge with node1, and node2, and an optional value."""
        self.node1: Node = node1
        self.node2: Node = node2
        self.value: SupportedValueType = value


class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []

    def add_node(self, node: Node):
        """Add node to self.nodes."""
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2 to self.edges."""
        self.edges.append(Edge(node1, node2))

    def remove_node(self, node):
        """Remove first occurrence of node from self.nodes."""
        self.nodes.remove(node)

    def remove_edge(self, node1, node2):
        """Remove first occurrence of edge between node1 and node2 from self.edges."""
        self.edges.remove(Edge(node1, node2))
