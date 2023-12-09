import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total_num = 0
for row_i, row in enumerate(lines):
    for m in re.finditer(r"(\d+)", row):
        neighbors = [
            (r, c)
            for c in range(m.start() - 1, m.end() + 1)
            for r in range(row_i - 1, row_i + 2)
            if 0 <= c < len(row) and 0 <= r < len(lines)
        ]
        if any(not lines[r][c].isnumeric() and lines[r][c] != "." for r, c in neighbors):
            total_num += int(m[0])
print(total_num)
