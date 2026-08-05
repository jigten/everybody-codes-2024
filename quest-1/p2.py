input = open(0).read()
pts_map = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

n = len(input)
res = 0

for i in range(0, n - 1, 2):
    x, y = input[i], input[i + 1]
    both = False if "x" in [x, y] else True

    res += pts_map[x]
    res += pts_map[y]

    if both:
        res += 2

print(f"Answer: {res}")
