with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

oasis = [list(map(int, l.split())) for l in lines]
result = 0
for s in oasis:
    sequences = [s]
    while not all(i == 0 for i in s):
        s = [j - i for i, j in zip(s[:-1], s[1:])]
        sequences.append(s)

    sequences[-1].append(0)
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
    result += sequences[0][-1]
print(result)
