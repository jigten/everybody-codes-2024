input = open(0).read()

brightness = map(int, input.splitlines())
res = 0

for b in brightness:
    cb = b
    while cb > 0:
        for s in [10, 5, 3, 1]:
            res += cb // s
            cb %= s

print(f"Answer: {res}")
