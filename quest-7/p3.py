from collections import Counter, defaultdict

track_str = """
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
"""


def convert_to_flat(track):
    path = [(0, 0), (0, 1)]
    H, W = len(track), len(track[0])

    while True:
        r, c = path[-1]
        pr, pc = path[-2]

        nxt = next(
            (nr, nc)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if (nr := r + dr, nc := c + dc) != (pr, pc)
            and 0 <= nr < H
            and 0 <= nc < W
            and track[nr][nc] != " "
        )
        path.append(nxt)
        if nxt == (0, 0):
            break
    return "".join(track[r][c] for r, c in path[1:])


rows = [r for r in track_str.splitlines() if r]
width = max(len(r) for r in rows)
track = [list(r.ljust(width)) for r in rows]
flat_track = convert_to_flat(track)


input = open(0).read().splitlines()
enemy_plan = ""

for seg in input:
    name, actions = seg.split(":")
    enemy_plan = actions.split(",")

action_map = {"+": 1, "-": -1, "=": 0}


def calculate_score(actions):
    total, score = 0, 10
    step = 0

    for _ in range(2024):
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
    return total


enemy_score = calculate_score(enemy_plan)
res = 0
counts = Counter({"+": 5, "-": 3, "=": 3})


def generate_plans(prefix=()):
    if len(prefix) == 11:
        yield prefix
        return
    for sym in counts:
        if counts[sym]:
            counts[sym] -= 1
            yield from generate_plans(prefix + (sym,))
            counts[sym] += 1


for plan in generate_plans():
    if calculate_score(plan) > enemy_score:
        res += 1

print(f"Answer: {res}")
