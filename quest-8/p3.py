priests = int(open(0).read())

acolytes, available = 10, 202400000

thickness, L = 1, 1
heights = [1]
best = 0

while True:
    L += 1
    thickness = (thickness * priests) % acolytes + acolytes
    heights = [thickness] + [h + thickness for h in heights] + [thickness]

    width = 2 * L - 1
    removed = sum((priests * width * h) % acolytes for h in heights[1:-1])
    needed = sum(heights) - removed

    if needed > available:
        break
    best = needed

print(needed - available)
