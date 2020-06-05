def intersection(arrays):
    """
    YOUR CODE HERE
    """
    counts = {}
    result = []

    for array in arrays:
        for item in array:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

    for k, v in counts.items():
        if v == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
