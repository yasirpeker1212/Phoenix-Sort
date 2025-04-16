import bisect
import time


def phoenix_sort_optimized(data):
    result = []
    leftovers = data[:]
    history = []

    while leftovers:
        run = [leftovers[0]]
        next_leftovers = []

        for i in range(1, len(leftovers)):
            if leftovers[i] >= run[-1]:
                run.append(leftovers[i])
            else:
                next_leftovers.append(leftovers[i])

        result = merge_sorted(result, run)
        leftovers = smart_reinsert(next_leftovers, result)
        history.append(result[:])

    return result, history


def merge_sorted(list1, list2):
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def smart_reinsert(leftovers, sorted_part):
    """Use binary insertion to smartly reintegrate rejected items."""
    new_leftovers = []
    for item in leftovers:
        idx = bisect.bisect_right(sorted_part, item)
        sorted_part.insert(idx, item)
    return new_leftovers


if __name__ == '__main__':
    data = [5, 1, 4, 2, 6, 0, 7]
    start = time.time()
    sorted_data, steps = phoenix_sort_optimized(data)
    end = time.time()

    print("Original:", data)
    print("Sorted:", sorted_data)
    print(f"Phoenix Sort took {end - start:.6f} seconds")
