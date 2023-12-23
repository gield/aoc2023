with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

num_rows, num_cols = len(lines), len(lines[0])
grid = [[c for c in l] for l in lines]

for col in range(num_cols):
    for row in range(num_rows):
        if grid[row][col] in "#O":
            continue
        for r in range(row + 1, num_rows):
            if grid[r][col] == "#":
                break
            if grid[r][col] == "O":
                grid[r][col] = "."
                grid[row][col] = "O"
                break
print(sum(num_rows - r for r, row in enumerate(grid) for m in row if m == "O"))
