input = [list(map(int, r.split())) for r in open(0).read().splitlines()]
grid = [list(map(int, col)) for col in zip(*input)]
rows, cols = len(input), len(input[0])

for rnd in range(10):
    curr_col = grid[rnd % cols]
    right_col = grid[(rnd + 1) % cols]

    clapper = curr_col.pop(0)
    n = len(right_col)
    r = clapper % (2 * n)

    pos = r - 1 if r <= n else 2 * n - r + 1
    right_col.insert(pos, clapper)
    print(f"Round {rnd + 1}: {"".join(str(c[0]) for c in grid)}")
