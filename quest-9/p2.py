input = open(0).read()

brightness = map(int, input.splitlines())
res = 0


# Recursion limit (stack overflow)
# @lru_cache(None)
# def min_stamps(b):
#     if b <= 0:
#         return 0
#
#     res = 10**9
#     for s in [30, 25, 24, 20, 16, 15, 10, 5, 3, 1]:
#         res = min(res, min_stamps(b % s) + b // s)
#
#     return res

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

for b in brightness:
    dp = [b + 1] * (b + 1)
    dp[0] = 0

    for i in range(1, b + 1):
        dp[i] = min(dp[i - s] + 1 for s in stamps if i >= s)

    res += dp[b]

print(f"Answer: {res}")
