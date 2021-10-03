# refer: https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1


def detect(q):
    length = len(q)
    for index in range(length):
        q[index] = q[index][0] - q[index][1]

    now = 0
    tank = 0
    start = 0
    rem = 0

    for index in range(length):
        now = tank + q[index]

        if now > -1:
            tank = now
        else:
            tank = 0
            start += 1
            rem += now
    return start if (tank + rem) >= 0 else -1


print(
    detect(
        eval(
            "[[98, 18], [82, 72], [10, 76], [68, 28], [98, 57], [87, 54], [7, 66], [20, 84], [29, 25], [33, 72], [4, 30], [71, 20], [9, 69], [41, 16], [97, 50], [19, 24], [47, 46], [22, 52], [80, 56], [65, 89], [42, 29], [94, 51], [35, 1], [25, 65], [88, 15], [44, 57], [28, 92], [60, 66], [33, 37], [38, 52], [76, 29], [75, 8]]"
        )
    )
)
