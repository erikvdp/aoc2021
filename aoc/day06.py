from typing import Counter, List


def parse_input(lines) -> List[int]:
    return list(int(x) for x in lines[0].split(","))


def simulate_days(state: List[int], days=0):
    for i in range(days):
        # decrement all items from the list by one
        state = [x - 1 for x in state]
        # if any of the items are zero, reset them to 6
        for j, el in enumerate(state):
            if el < 0:
                state[j] = 6
                state.append(8)
        print(f"Day: {days} {len(state)}")
    return len(state)


def simulate_days_2(state: List[int], days=0):
    c = Counter(state)
    data = [c[i] for i in range(9)][:]
    for _ in range(days):
        data.append(data.pop(0))
        data[6] += data[-1]
    return sum(data)
