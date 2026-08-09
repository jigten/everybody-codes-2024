# Same answer as p1

input = open(0).read()
nails = [int(r) for r in input.split("\n") if r]
nails.sort(reverse=True)

n, res = len(nails), 0

for i in range(n - 1):
    res += nails[i] - nails[n - 1]

print(f"Answer: {res}")
