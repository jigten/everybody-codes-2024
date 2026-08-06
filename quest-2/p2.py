input = open(0).read()
runes, words = input.split("\n\n")

runes = runes.split(":")[1].split(",")
reverse_runes = [r[::-1] for r in runes]
runes = {r for r in runes + reverse_runes}
sentences = words.split("\n")

res = 0


def count(w):
    n = len(w)
    pos = []
    for l in range(n):
        for r in range(l, n):
            if w[l : r + 1] in runes:
                pos.append((l, r + 1))

    stack = []
    for s, e in pos:
        ss, ee = s, e
        while stack and stack[-1][1] >= ss:
            ps, pe = stack.pop()
            ss = min(ss, ps)
            ee = max(ee, pe)

        stack.append((ss, ee))

    return sum(e - s for s, e in stack)


for words in sentences:
    for w in words.split():
        res += count(w)

print(f"Answer: {res}")
