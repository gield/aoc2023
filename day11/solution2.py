with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_rows = [r for r in range(len(lines)) if set(lines[r]) == {"."}]
empty_cols = [c for c in range(len(lines[0])) if all(lines[r][c] == "." for r in range(len(lines)))]

galaxies = [(r, c) for r, row in enumerate(lines) for c, s in enumerate(row) if s == "#"]
total_distance = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1, g2 = galaxies[i], galaxies[j]
        total_distance += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
        for r in empty_rows:
            if g1[0] < r < g2[0] or g2[0] < r < g1[0]:
                total_distance += 999_999
        for c in empty_cols:
            if g1[1] < c < g2[1] or g2[1] < c < g1[1]:
                total_distance += 999_999
print(total_distance)
