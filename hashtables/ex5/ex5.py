# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = [];

    for x in files:
        for y in queries:
            if y in x:
                result.append(x);

    return result;


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
