from typing import Counter, List, Tuple, Text
import numpy as np
from collections import defaultdict

# digit to nr_segments
# 1 -> 2 segments
# 7 -> 3 segments
# 4 -> 4 segments

# 2 -> 5 segments
# 3 -> 5 segments
# 5 -> 5 segments

# 6 -> 6 segments
# 0 -> 6 segments
# 9 -> 6 segments

# 8 -> 7 segments


def parse_input(lines) -> List[Tuple[Text]]:
    formatted_input = []
    for line in lines:
        signal_patterns, output_values = list(x.strip() for x in line.split("|"))
        signal_patterns = list(x.strip() for x in signal_patterns.split(" "))
        output_values = list(x.strip() for x in output_values.split(" "))
        formatted_input.append((signal_patterns, output_values))
    return formatted_input


def calculate_easy_output_values(lines):
    easy_output_values = 0
    for _, output_values in lines:
        for output_value in output_values:
            if len(output_value) in [2, 3, 4, 7]:
                easy_output_values += 1
    return easy_output_values


def calculate_output_values(lines):
    total = 0
    for signal_patterns, output_values in lines:
        number_mapping = ["x"] * 10
        segment_mapping = ["x"] * 10
        n_segments_to_display = defaultdict(list)
        for pattern in signal_patterns:
            n_segments_to_display[len(pattern)].append("".join(sorted(pattern)))
        # easy segments
        number_mapping[1] = n_segments_to_display[2][0]
        number_mapping[7] = n_segments_to_display[3][0]
        number_mapping[4] = n_segments_to_display[4][0]
        number_mapping[8] = n_segments_to_display[7][0]

        # get segment_mapping at pos 0 (digit with lenght 3 - digit with length 2)
        segment_mapping[0] = list(
            set(n_segments_to_display[3][0]) - set(n_segments_to_display[2][0])
        )[0]
        segment_mapping[5] = list(
            (
                set(n_segments_to_display[6][1])
                .intersection(set(n_segments_to_display[6][0]))
                .intersection(set(n_segments_to_display[6][2]))
            ).intersection(n_segments_to_display[2][0])
        )[0]
        segment_mapping[2] = list(
            set(n_segments_to_display[2][0]) - set(segment_mapping[5])
        )[0]
        number_mapping[6] = list(
            x for x in n_segments_to_display[6] if segment_mapping[2] not in x
        )[0]
        number_mapping[2] = list(
            x for x in n_segments_to_display[5] if segment_mapping[5] not in x
        )[0]
        number_mapping[5] = list(
            x for x in n_segments_to_display[5] if (segment_mapping[2] not in x)
        )[0]
        number_mapping[3] = list(
            x
            for x in n_segments_to_display[5]
            if (x != number_mapping[5] and x != number_mapping[2])
        )[0]
        segment_mapping[4] = list(set(number_mapping[6]) - set(number_mapping[5]))[0]
        number_mapping[9] = list(
            x for x in n_segments_to_display[6] if segment_mapping[4] not in x
        )[0]
        number_mapping[0] = list(
            x
            for x in n_segments_to_display[6]
            if (x != number_mapping[9] and x != number_mapping[6])
        )[0]
        # decode output values
        number = ""
        for value in output_values:
            number += str(number_mapping.index("".join(sorted(value))))
        total += int(number)
    return total
