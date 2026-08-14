import math

input = open(0).read()

blocks = int(input)

# L completed Ls needs 1 + 3 + 5 + ... + (2L-1) = L² blocks, and its width is 2L - 1
# so we get the smallest possible L where L * L >= blocks
# that will be the max layer we can build with the given blocks using extra blocks for one more layer
L = math.isqrt(blocks - 1) + 1

print(f"{(L * L - blocks) * (2 * L - 1)}")
