with open("input.txt", "r") as f:
    lines = f.read().strip().split(",")


def h(s: str) -> int:
    value = 0
    for c in s:
        _, value = divmod((value + ord(c)) * 17, 256)
    return value


print(sum(h(s) for s in lines))
