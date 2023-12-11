with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

print(sum(t * (time - t) > distance for t in range(time + 1)))
