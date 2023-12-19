with open("input.txt", "r") as f:
    patterns = [p.split("\n") for p in f.read().strip().split("\n\n")]

result = 0
for pattern in patterns:
    # horizontal
    for m in range(1, len(pattern)):
        d = min(len(pattern) - m, m - 0)
        up = pattern[m - d:m]
        down = pattern[m:m + d]
        if up == down[::-1]:
            result += 100 * m
            break

    # vertical
    pattern_t = ["".join(x) for x in zip(*pattern)]
    for m in range(1, len(pattern_t)):
        d = min(len(pattern_t) - m, m - 0)
        left = pattern_t[m - d:m]
        right = pattern_t[m:m + d]
        if left == right[::-1]:
            result += m
            break
print(result)
