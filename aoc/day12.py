from typing import Dict, List, Text
from collections import Counter


def parse_input(lines) -> Dict[Text, List[Text]]:
    graph = dict()
    for line in lines:
        start, stop = line.split("-")
        if start in graph:
            graph[start].append(stop)
        else:
            graph[start] = [stop]
        if stop in graph:
            graph[stop].append(start)
        else:
            graph[stop] = [start]
    return graph


def calculate_paths_1(graph) -> int:

    total_paths = 0

    def _walk(node, path):
        path.append(node)
        for new_node in graph[node]:
            nonlocal total_paths
            if new_node == "end":
                total_paths += 1
            elif new_node not in path or new_node.isupper():
                _walk(new_node, path[:])

    _walk("start", [])

    return total_paths


def calculate_paths_2(graph) -> int:

    total_paths = 0
    paths = []

    def _walk(node, path):
        path.append(node)
        for new_node in graph[node]:
            nonlocal total_paths
            nonlocal paths
            if new_node == "end":
                total_paths += 1
                paths.append(path)
            elif new_node != "start":
                if new_node.isupper():
                    _walk(new_node, path[:])
                # check if there is only one small cave that has been visited twice
                else:
                    small_caves = list(x for x in path[:] if x.islower()) + [new_node]
                    small_caves_by_freq = Counter(Counter(small_caves).values())
                    if (
                        small_caves_by_freq.get(2) in (None, 1)
                        and max(small_caves_by_freq) <= 2
                    ):
                        _walk(new_node, path[:])

    _walk("start", [])

    return total_paths
