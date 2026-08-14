input = open(0).read()

priests = int(input)

blocks, acolytes = 20240000, 1111

L, thickness = 1, 1
blocks_used = 1

while blocks_used <= blocks:
    L += 1
    thickness = (thickness * priests) % acolytes
    blocks_used += thickness * (2 * L - 1)

print(f"Answer: {(blocks_used - blocks) * (2 * L - 1)}")
