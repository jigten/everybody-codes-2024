from collections import defaultdict


def convert_to_flat(track):
    rows, cols = len(track), len(track[0])
    flat_track = []

    for c in range(1, cols):
        flat_track.append(track[0][c])

    for r in range(1, rows):
        flat_track.append(track[r][cols - 1])

    for c in range(cols - 2, -1, -1):
        flat_track.append(track[rows - 1][c])

    for r in range(rows - 2, 0, -1):
        flat_track.append(track[r][0])

    flat_track.append(track[0][0])

    return flat_track


# track = """
# S+===
# -   +
# =+=-+
# """

track = """
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
"""

track = [list(r) for r in track.splitlines() if r]
flat_track = convert_to_flat(track)


input = open(0).read().splitlines()
segments = defaultdict(list)

for seg in input:
    name, actions = seg.split(":")
    segments[name] = actions.split(",")

action_map = {"+": 1, "-": -1, "=": 0}
rankings = defaultdict(int)


for name, actions in segments.items():
    total, score = 0, 10
    step = 0

    for _ in range(10):
        for i in range(len(flat_track)):
            if flat_track[i] == "=" or flat_track[i] == "S":
                a = actions[step % len(actions)]
                score += action_map[a]
            else:
                score += action_map[flat_track[i]]

            if score < 0:
                score = 0
            total += score
            step += 1

    rankings[name] = total

print(
    f"Answer: {''.join([name for name, _ in sorted(rankings.items(), key=lambda x: x[1], reverse=True)])}"
)
