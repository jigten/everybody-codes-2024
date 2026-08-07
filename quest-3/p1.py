from collections import deque

input = open(0).read()
grid = [list(row) for row in input.split("\n") if row]
rows, cols = len(grid), len(grid[0])


q = deque()

# bfs solution
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == ".":
            grid[r][c] = 0
        elif grid[r][c] == "#":
            grid[r][c] = 1
            q.append((r, c))


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    cr, cc = q.popleft()
    max_diff = 0
    next_curr = grid[cr][cc] + 1

    for dr, dc in dirs:
        nr, nc = cr + dr, cc + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            max_diff = max(max_diff, abs(next_curr - grid[nr][nc]))

    if max_diff <= 1:
        grid[cr][cc] += 1
        q.append((cr, cc))


print(f"Answer {sum(sum(row) for row in grid)}")

# simulation solution
# res = 0
# for r in range(rows):
#     for c in range(cols):
#         if grid[r][c] == ".":
#             grid[r][c] = 0
#         elif grid[r][c] == "#":
#             grid[r][c] = 1
#             res += 1
#
# changed = True
# while changed:
#     curr_change = False
#     for r in range(1, rows - 1):
#         for c in range(1, cols - 1):
#             curr = grid[r][c]
#
#             if curr == 0:
#                 continue
#
#             l_val = grid[r][c - 1]
#             r_val = grid[r][c + 1]
#             u_val = grid[r - 1][c]
#             d_val = grid[r + 1][c]
#
#             next_curr = curr + 1
#             max_diff = max(
#                 abs(l_val - next_curr),
#                 abs(r_val - next_curr),
#                 abs(d_val - next_curr),
#                 abs(u_val - next_curr),
#             )
#
#             if max_diff <= 1:
#                 res += 1
#                 grid[r][c] += 1
#                 curr_change = True
#
#     changed = curr_change
#
# print(f"Answer: {res}")
