# same as p1 answer

input = open(0).read()
grid = [list(row) for row in input.split("\n") if row]
rows, cols = len(grid), len(grid[0])

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == ".":
            grid[r][c] = 0
        elif grid[r][c] == "#":
            grid[r][c] = 1
            res += 1

changed = True
while changed:
    curr_change = False
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            curr = grid[r][c]

            if curr == 0:
                continue

            l_val = grid[r][c - 1]
            r_val = grid[r][c + 1]
            u_val = grid[r - 1][c]
            d_val = grid[r + 1][c]

            next_curr = curr + 1
            max_diff = max(
                abs(l_val - next_curr),
                abs(r_val - next_curr),
                abs(d_val - next_curr),
                abs(u_val - next_curr),
            )

            if max_diff <= 1:
                res += 1
                grid[r][c] += 1
                curr_change = True

    changed = curr_change

print(f"Answer: {res}")
