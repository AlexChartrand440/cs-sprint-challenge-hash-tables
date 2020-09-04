def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = [];

    for i in a:
        if i > 0 and (i * -1) in a and i not in result:
            result.append(i);

    return result;


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
