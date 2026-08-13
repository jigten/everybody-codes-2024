from collections import defaultdict

input = open(0).read().splitlines()
segments = defaultdict(list)

for seg in input:
    name, actions = seg.split(":")
    segments[name] = actions.split(",")

action_map = {"+": 1, "-": -1, "=": 0}
rankings = defaultdict(int)

for name, actions in segments.items():
    total, score = 0, 10

    for i in range(10):
        a = actions[i % len(actions)]
        score += action_map[a]
        if score < 0:
            score = 0
        total += score

    rankings[name] = total

print(
    f"Answer: {''.join([name for name, _ in sorted(rankings.items(), key=lambda x: x[1], reverse=True)])}"
)
