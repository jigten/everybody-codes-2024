# Same as Part 2

from collections import defaultdict

input = open(0).read()
adj = defaultdict(list)

paths = defaultdict(list)

for row in input.splitlines():
    node, children = row.split(":")

    for c in children.split(","):
        adj[node].append(c)


def dfs(node, path, path_len):
    if node == "@":
        paths[path_len].append(path)
        return

    for c in adj[node]:
        if c in path:
            continue
        dfs(c, path + c + ",", path_len + 1)


dfs("RR", "RR,", 1)

for path in paths.values():
    if len(path) == 1:
        print(f"Answer: {"".join(c[0] for c in path[0].split(",") if c)}")
