with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

num_rows, num_cols = len(lines), len(lines[0])
grid = [[c for c in l] for l in lines]

memo = {}
cycle = 0
while cycle < 1_000_000_000:
    # do 1 cycle
    for _ in range(4):  # 4 directions
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
        grid = [list(x)[::-1] for x in zip(*grid)]  # rotate
    cycle += 1

    k = tuple(tuple(row) for row in grid)
    if k not in memo:
        memo[k] = cycle
    else:
        loop_length = cycle - memo[k]
        num_loops_to_skip = (1_000_000_000 - cycle) // loop_length
        cycle += num_loops_to_skip * loop_length

print(sum(num_rows - r for r, row in enumerate(grid) for m in row if m == "O"))
