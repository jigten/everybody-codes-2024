input = open(0).read()
nails = [int(r) for r in input.split("\n") if r]
n, res = len(nails), 0

# without sorting
# res = sum(nails) - (n * min(nails))

nails.sort(reverse=True)
for i in range(n - 1):
    res += nails[i] - nails[n - 1]

print(f"Answer: {res}")
