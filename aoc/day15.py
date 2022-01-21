import heapq
import numpy as np


def _read_file_to_grid(lines) -> np.ndarray:
    data = list()
    for line in lines:
        row = list()
        for number in line:
            row.append(int(number))
        data.append(row)
    grid = np.array(data)
    # replicate the grid in a new array
    return grid


def _read_file_to_grid_2(lines) -> np.ndarray:
    data = list()
    for line in lines:
        row = list()
        for number in line:
            row.append(int(number))
        data.append(row)
    grid = np.array(data)
    # replicate the grid in a new array
    new_grid = np.zeros((grid.shape[0] * 5, grid.shape[1] * 5))
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            start_pos = (i, j)
            value = grid[start_pos]
            for k in range(i, new_grid.shape[0], grid.shape[0]):
                all_values = list()
                for l in range(j, new_grid.shape[0], grid.shape[0]):
                    all_values.append(value)
                    new_grid[k, l] = value
                    value = value + 1
                    if value == 10:
                        value = 1
                value = all_values[1]  # reset start value for next row
    return new_grid


def _transform_grid_to_graph(grid: np.ndarray) -> dict:
    graph = dict()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbors = dict()
            if i - 1 >= 0:
                neighbors[(i - 1, j)] = grid[i - 1, j]
            if i + 1 < grid.shape[0]:
                neighbors[(i + 1, j)] = grid[i + 1, j]
            if j - 1 >= 0:
                neighbors[(i, j - 1)] = grid[i, j - 1]
            if j + 1 < grid.shape[1]:
                neighbors[(i, j + 1)] = grid[i, j + 1]
            graph[(i, j)] = neighbors
    return graph


def parse_input(lines) -> dict:
    grid = _read_file_to_grid(lines)
    # transform grid to graph
    graph = _transform_grid_to_graph(grid)
    return graph


def parse_input_2(lines) -> dict:
    grid = _read_file_to_grid_2(lines)
    # transform grid to graph
    graph = _transform_grid_to_graph(grid)
    return graph


def calculate_min_cost_path(graph: dict) -> float:

    distances = dict()
    distances = {point: float("infinity") for point in graph.keys()}
    distances[0, 0] = 0

    pq = [(0, (0, 0))]  # priority queue of (distance, vertex) tuples
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # return bottom right distance
    return distances[max(graph.keys())]
