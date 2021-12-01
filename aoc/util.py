from typing import List


def read_file_as_list(filename) -> List[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()