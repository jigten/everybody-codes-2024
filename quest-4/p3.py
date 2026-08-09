input = open(0).read()

nails = [int(r) for r in input.split("\n") if r]
nails.sort(reverse=True)

n, res = len(nails), 0

half = n // 2

for i in range(n):
    if i == half:
        continue

    res += abs(nails[i] - nails[half])

print(f"Answer: {res}")
