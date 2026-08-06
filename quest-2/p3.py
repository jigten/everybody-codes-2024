input = open(0).read()

runes, words = input.split("\n\n")
runes = runes.split(":")[1].split(",")
reverse_runes = [r[::-1] for r in runes]
runes = {r for r in runes + reverse_runes}

words_grid = [list(w) for w in words.split("\n") if w]
rows, cols = len(words_grid), len(words_grid[0])

coords = set()
max_rune_len = len(max(runes, key=len))

for r in range(rows):
    for c in range(cols):
        for l in range(max_rune_len + 1):
            if "".join(words_grid[r][(c + i) % cols] for i in range(l)) in runes:
                coords.update((r, (c + i) % cols) for i in range(l))

for c in range(cols):
    for r in range(rows):
        for l in range(min(rows - r + 1, r + max_rune_len + 1)):
            if "".join(words_grid[(r + i)][c] for i in range(l)) in runes:
                coords.update((r + i, c) for i in range(l))

print(f"Answer: {len(coords)}")
