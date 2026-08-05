input = open(0).read()
pts_map = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

n = len(input)
res = 0

for i in range(0, n - 2, 3):
    x, y, z = input[i], input[i + 1], input[i + 2]
    gp_cnt = 3 - [x, y, z].count("x")

    res += pts_map[x]
    res += pts_map[y]
    res += pts_map[z]

    if gp_cnt == 2:
        res += 2
    elif gp_cnt == 3:
        res += 6

print(f"Answer: {res}")
