from collections import defaultdict
import math
import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total_num = 0
for _, game in enumerate(lines):
    sets = game.split(": ")[1].split("; ")
    min_num_colors: defaultdict[str, int] = defaultdict(int)
    for s in sets:
        num_colors = {c: int(n) for (n, c) in re.findall(r"(\d+) (\w+)", s)}
        for color, n in num_colors.items():
            min_num_colors[color] = max(min_num_colors[color], n)
    total_num += math.prod(min_num_colors.values())
print(total_num)
