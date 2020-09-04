def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    result = [];
    thingy = {};

    for a in arrays:
        for i in a:
            if i in thingy:
                thingy[i] = thingy[i] + 1;
            else:
                thingy[i] = 1;
    
    for b in thingy:
        if thingy[b] == len(arrays):
            result.append(b);

    return result;


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
