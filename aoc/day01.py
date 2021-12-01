def count_increases(input_list):
    """
    Counts the number of times the input list increases
    """
    count = 0
    for i in range(len(input_list) - 1):
        if input_list[i] < input_list[i + 1]:
            count += 1
    return count


def sliding_window_count_increases(input_list, window_size):
    """
    Counts the number of times the input list increases
    """
    sliding_window_list = []
    for i in range(len(input_list) + 1 - window_size):
        sliding_window_list.append(sum(input_list[i : i + window_size]))
    return count_increases(sliding_window_list)
