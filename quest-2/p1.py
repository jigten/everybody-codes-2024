input = open(0).read()
runes, words = [l for l in input.split("\n") if l]

runes = runes.split(":")[1].split(",")
words = words.split()

res = 0

for w in words:
    for r in runes:
        if r in w:
            res += 1

print(f"Answer: {res}")
