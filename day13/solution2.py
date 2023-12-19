from typing import Optional


with open("input.txt", "r") as f:
    patterns = [p.split("\n") for p in f.read().strip().split("\n\n")]


def find_mirror(pattern: list[str], ignore: Optional[int] = None) -> Optional[int]:
    # horizontal
    for m in range(1, len(pattern)):
        if 100 * m == ignore:
            continue
        d = min(len(pattern) - m, m - 0)
        up = pattern[m - d:m]
        down = pattern[m:m + d]
        if up == down[::-1]:
            return 100 * m

    # vertical
    pattern_t = ["".join(x) for x in zip(*pattern)]
    for m in range(1, len(pattern_t)):
        if m == ignore:
            continue
        d = min(len(pattern_t) - m, m - 0)
        left = pattern_t[m - d:m]
        right = pattern_t[m:m + d]
        if left == right[::-1]:
            return m

    # no mirror found
    return None


result = 0
for p, pattern in enumerate(patterns):
    original_mirror = find_mirror(pattern)
    for r in range(len(pattern)):
        for c in range(len(pattern[0])):
            if p == 0 and r == 14 and c == 5:
                pass
            pattern_copy = pattern.copy()
            if pattern[r][c] == "#":
                pattern_copy[r] = pattern[r][:c] + "." + pattern[r][c + 1:]
            if pattern[r][c] == ".":
                pattern_copy[r] = pattern[r][:c] + "#" + pattern[r][c + 1:]
            if (mirror := find_mirror(pattern_copy, ignore=original_mirror)):
                result += mirror
                break
        else:
            continue
        break
print(result)
