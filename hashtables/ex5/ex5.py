# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    path_for_files = {}
    result = []

    for file in files:
        filename = file.split('/')[-1]
        if filename in path_for_files:
            path_for_files[filename].append(file)
        else:
            path_for_files[filename] = [file]

    for query in queries:
        if query in path_for_files:
            result.extend(path_for_files[query])

    return result


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
