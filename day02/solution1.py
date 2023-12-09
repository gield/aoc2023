import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total_num = 0
limits = {"red": 12, "green": 13, "blue": 14}
for i, game in enumerate(lines):
    sets = game.split(": ")[1].split("; ")
    for s in sets:
        if any(int(n) > limits[c] for (n, c) in re.findall(r"(\d+) (\w+)", s)):
            break
    else:
        total_num += i + 1
print(total_num)
