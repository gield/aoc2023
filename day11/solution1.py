with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_rows = [r for r in range(len(lines)) if set(lines[r]) == {"."}]
empty_cols = [c for c in range(len(lines[0])) if all(lines[r][c] == "." for r in range(len(lines)))]
for r in reversed(empty_rows):
    lines.insert(r, "." * len(lines[0]))
for c in reversed(empty_cols):
    for r in range(len(lines)):
        lines[r] = lines[r][:c] + "." + lines[r][c:]

galaxies = [(r, c) for r, row in enumerate(lines) for c, s in enumerate(row) if s == "#"]
total_distance = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1, g2 = galaxies[i], galaxies[j]
        total_distance += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
print(total_distance)
