# TODO 0 pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>


import json
from queue import PriorityQueue
from collections import defaultdict

import adthelpers


class Graph:
    def __init__(self) -> None:
        # self.edges: dict[int, list[tuple[float, int]]] = {}
        self.edges: dict[int, list[tuple[float, int]]] = defaultdict(list)

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        # přidání hrany do datové struktury grafu
        self.edges[src].append((weight, dst))
        self.edges[dst].append((weight, src))


def load_graph(filename: str) -> Graph:

    with open(filename, 'r') as f:
        json_data = json.load(f)

    # vytvořit graf podle dat ze souboru
    graph = Graph()
    for edge in json_data['links']:
        graph.add_edge(src=edge['source'], dst=edge['target'], weight=edge['weight'])

    return graph


def spanning_tree(graph: Graph) -> None:
    closed: set[int] = set()
    sp_tree: list[tuple[int, int]] = []
    queue: PriorityQueue = PriorityQueue()

    painter = adthelpers.painter.Painter(
        graph,
        visible=queue,
        closed=closed,
        color_edges=sp_tree,
    )
    painter.draw_graph()

    # TODO 3 Implementujte Prim-Jarníkův algoritmus pro nalezení minimální kostry


def main() -> None:
    graph = load_graph("10-spanning-tree/data/graph_grid_s3_3.json")

    painter = adthelpers.painter.Painter(
        graph,
        # colors=("red", "blue", "yellow", "grey") # pokud by byl problém s barvami je možné změnit
    )
    painter.draw_graph()

    # debug to see progress...
    spanning_tree(graph)

    # don't close before user acknowledges diagrams
    input("Press enter to exit program...")


if __name__ == "__main__":
    main()
