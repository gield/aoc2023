from collections import defaultdict


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

num_rows, num_cols = len(lines), len(lines[0])
graph = defaultdict(set)
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == ".":
            continue
        if char == "S":
            start = (r, c)
            continue
        if char in "|LJ" and r - 1 >= 0 and lines[r - 1][c] in "S|7F":
            graph[(r, c)].add((r - 1, c))
            graph[(r - 1, c)].add((r, c))
        if char in "|7F" and r + 1 < num_rows and lines[r + 1][c] in "S|LJ":
            graph[(r, c)].add((r + 1, c))
            graph[(r + 1, c)].add((r, c))
        if char in "-J7" and c - 1 >= 0 and lines[r][c - 1] in "S-LF":
            graph[(r, c)].add((r, c - 1))
            graph[(r, c - 1)].add((r, c))
        if char in "-LF" and c + 1 < num_cols and lines[r][c + 1] in "S-J7":
            graph[(r, c)].add((r, c + 1))
            graph[(r, c + 1)].add((r, c))

path = [start]
while True:
    for node in graph[path[-1]]:
        if node not in path:
            path.append(node)
            break
    else:
        break
print(len(path) // 2)
