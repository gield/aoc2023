from typing import Optional


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def get_num(line: str, i: int) -> Optional[int]:
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    if line[i].isnumeric():
        return int(l[i])
    for j in range(3, 6):
        if line[i:i + j] in d:
            return d[line[i:i + j]]
    return None


s = 0
for l in lines:
    for i in range(len(l)):
        if (x := get_num(l, i)):
            s += 10 * x
            break
    for i in range(len(l) - 1, -1, -1):
        if (x := get_num(l, i)):
            s += x
            break
print(s)
