from collections import defaultdict

input = [list(map(int, r.split())) for r in open(0).read().splitlines()]

grid = [list(map(int, col)) for col in zip(*input)]
rows, cols = len(input), len(input[0])

rnd = 0
seen = defaultdict(int)
res = 0

while True:
    curr_col = grid[rnd % cols]
    right_col = grid[(rnd + 1) % cols]

    clapper = curr_col.pop(0)
    n = len(right_col)
    r = clapper % (2 * n)

    if r == 0:
        r = 2 * n

    pos = r - 1 if r <= n else 2 * n - r + 1
    right_col.insert(pos, clapper)
    shout = int("".join(str(c[0]) for c in grid))
    res = max(res, shout)

    key = (rnd % cols, tuple(tuple(c) for c in grid))
    if key in seen:
        break

    seen[key] = rnd
    rnd += 1

print(f"Answer: {res}")
