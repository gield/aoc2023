with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

product = 1
for time, distance in zip(times, distances):
    product *= sum(t * (time - t) > distance for t in range(time + 1))
print(product)
