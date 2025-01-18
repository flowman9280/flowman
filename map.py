map = [
    [3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3],
    [3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3],
    [3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3],
    [3, 0, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 0, 3],
    [3, 0, 0, 0, 3, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 3, 0, 0, 3, 0, 3, 3, 0, 0, 0, 3],
    [3, 0, 3, 0, 3, 3, 0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 0, 3, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 3, 8, 8, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 3, 3, 0, 0, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 8, 8, 8, 8, 3, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 8, 8, 8, 8, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 8, 8, 8, 8, 3, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 3, 3, 0, 0, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 3, 0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 3, 0, 3, 3, 0, 3, 0, 3],
    [3, 0, 0, 0, 3, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 3, 0, 0, 3, 0, 3, 3, 0, 0, 0, 3],
    [3, 0, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 0, 3],
    [3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3],
    [3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3],
    [3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
]