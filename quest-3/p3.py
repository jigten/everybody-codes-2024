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
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

while changed:
    curr_change = False
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            curr = grid[r][c]

            if curr == 0:
                continue

            next_curr = curr + 1
            max_diff = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                max_diff = max(max_diff, abs(grid[nr][nc] - next_curr))

            if max_diff <= 1:
                res += 1
                grid[r][c] += 1
                curr_change = True

    changed = curr_change

print(f"Answer: {res}")
