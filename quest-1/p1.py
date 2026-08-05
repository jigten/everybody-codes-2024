input = open(0).read()
res = 0

for c in input:
    if c == "B":
        res += 1
    elif c == "C":
        res += 3

print(f"Answer: {res}")
