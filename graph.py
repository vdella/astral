import string
from dataclasses import dataclass


@dataclass
class Graph:
    nodes: dict


def __read(file: str) -> tuple:
    """Reads a :param file: and :returns: how many vertices will be used along with their edges."""
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]  # Clears end spaces.

    size = int(lines[1])  # Hardwired as the actual vertices count we'll be using.
    relations = lines[3:]  # The edges begin at the third position in the list.
    return size, relations


def nodes_according_to(size):
    """:returns: a dictionary of dicts using lowercase ascii chars according to :param size:"""
    chars = string.ascii_lowercase
    nodes = dict()

    for i in range(size):
        nodes[chars[i]] = dict()

    return nodes


def build_from(file: str) -> Graph:
    size, lines = __read(file)
    nodes = nodes_according_to(size)

    for line in lines:
        src, weight, dst = line.split()

        # As we'll be dealing with a non-directed graph, we must ensure that all extremities receive proper attention.
        nodes[src][dst] = nodes[dst][src] = int(weight)

    return Graph(nodes)
