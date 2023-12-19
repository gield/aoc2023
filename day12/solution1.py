import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def dfs(springs: str, counts: list[int], i: int) -> int:
    if i == len(springs):  # last i
        spring_groups = re.findall(r"(#*)", springs)
        counts_state = [len(g) for g in spring_groups if len(g)]
        return int(counts == counts_state)
    if springs[i] == "?":
        return sum(
            dfs(springs[:i] + s + springs[i + 1:], counts, i + 1)
            for s in "#."
        )
    return dfs(springs, counts, i + 1)


all_springs = [line.split(" ")[0] for line in lines]
all_counts = [[int(c) for c in line.split(" ")[1].split(",")] for line in lines]
print(sum(
    dfs(springs, counts, 0)
    for springs, counts in zip(all_springs, all_counts)
))
