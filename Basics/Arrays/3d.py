a = [
    [
        [1, 2, 4],
        [4, 5, 6]
    ],
    [
        [1, 2, 4],
        [4, 5, 6]
    ]
]


for _ in range(len(a)):
    for __ in range(len(a[_])):
        for ___ in range(len(a[__])):
            print(a[_][__][___])