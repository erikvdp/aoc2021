from typing import List, Text
from collections import deque
import numpy as np

MATCHES = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}


def calculate_score(lines: List[Text]) -> int:
    char_to_score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    total_score = 0
    for line in lines:
        stack = deque()
        for char in line:
            if char in MATCHES.keys():
                stack.append(char)
            elif char in MATCHES.values():
                if MATCHES.get(stack.pop()) != char:
                    total_score += char_to_score.get(char, 0)
                    break
    return total_score


def calculate_score_2(lines: List[Text]) -> int:
    char_to_score = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    scores = []
    for line in lines:
        stack = deque()
        corrupted_line = False
        for char in line:
            if char in MATCHES.keys():
                stack.append(char)
            elif char in MATCHES.values():
                if MATCHES.get(stack.pop()) != char:
                    corrupted_line = True
                    break  # corrupted line
        if not corrupted_line:
            # check if there is something on the stack -> incomplete line
            score = 0
            while stack:
                char = stack.pop()
                score = (5 * score) + char_to_score.get(char, 0)
            scores.append(score)
    return np.median(scores)
