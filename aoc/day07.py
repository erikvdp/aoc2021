from typing import List
import numpy as np


def parse_input(lines) -> List[int]:
    return list(int(x) for x in lines[0].split(","))


def calculate_cheapest_outcome(positions: List[int]) -> int:
    median = np.median(positions)
    return sum(abs(x - median) for x in positions)


def calculate_cheapest_outcome_2(positions: List[int]) -> int:
    start_point = np.median(positions)

    def _calculate_outcome(point):
        outcome = 0
        for x in positions:
            n = abs(x - point)
            outcome += (n * (n + 1)) / 2  # triangular number
        return outcome

    baseline = _calculate_outcome(start_point)
    baseline_1 = _calculate_outcome(start_point + -1)
    baseline_2 = _calculate_outcome(start_point + 1)

    while not (baseline < baseline_1 and baseline < baseline_2):
        if baseline_1 < baseline_2:
            start_point -= 1
        else:
            start_point += 1
        baseline = _calculate_outcome(start_point)
        baseline_1 = _calculate_outcome(start_point + -1)
        baseline_2 = _calculate_outcome(start_point + 1)
        print(start_point)
    return baseline
