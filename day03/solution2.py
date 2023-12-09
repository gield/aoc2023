from collections import defaultdict
import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

gears: defaultdict[tuple[int, int], list[int]] = defaultdict(list)
for row_i, row in enumerate(lines):
    for m in re.finditer(r"(\d+)", row):
        neighbors = [
            (r, c)
            for c in range(m.start() - 1, m.end() + 1)
            for r in range(row_i - 1, row_i + 2)
            if 0 <= c < len(row) and 0 <= r < len(lines)
        ]
        for r, c in neighbors:
            if lines[r][c] == "*":
                gears[(r, c)].append(int(m[0]))
print(sum(g[0] * g[1] for g in gears.values() if len(g) == 2))
