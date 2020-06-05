def has_negatives(a):
    """
    YOUR CODE HERE
    """
    counts = {}
    result = []

    for num in a:
        if abs(num) not in counts:
            counts[abs(num)] = num
        else:
            if counts[abs(num)] + num == 0:
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
