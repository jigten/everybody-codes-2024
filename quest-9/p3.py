import math

input = open(0).read()

brightness = map(int, input.splitlines())
res = 0
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]


def construct(b):
    dp = [b + 1] * (b + 1)
    dp[0] = 0

    for i in range(b + 1):
        for s in stamps:
            if i - s >= 0:
                dp[i] = min(dp[i], dp[i - s] + 1)

    return dp


for b in brightness:
    min_stamps = 10**9
    dp = construct(b)

    for y in range(max(0, (b + 1) // 2 - 50), b // 2 + 1):
        x = b - y
        x_cnt, y_cnt = dp[x], dp[y]

        min_stamps = min(min_stamps, x_cnt + y_cnt)

    res += min_stamps


print(f"Answer: {res}")
