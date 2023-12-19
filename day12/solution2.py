with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def dfs(springs: str, counts: list[int], i: int, g: int, group_length: int,
        memo: dict[tuple[int, int, int], int]) -> int:
    k = (i, g, group_length)
    if k in memo:
        return memo[k]

    if i == len(springs):  # last i in springs
        if g == len(counts) - 1 and group_length == counts[g]:
            return 1  # currently in last group + it's finished
        if g == len(counts) and group_length == 0:
            return 1  # all groups finished + currently not in group
        return 0

    memo[k] = 0
    # next i is ? or .
    if springs[i] in "?.":
        if group_length > 0 and g < len(counts) and counts[g] == group_length:
            # currently in a group that is ending -> go to next i and next group
            memo[k] += dfs(springs, counts, i + 1, g + 1, 0, memo)
        elif group_length == 0:
            # currently not in a group -> go to next i
            memo[k] += dfs(springs, counts, i + 1, g, 0, memo)
    # next i is ? or #
    if springs[i] in "?#":
        # fill in #, stay in group, and go to next i
        memo[k] += dfs(springs, counts, i + 1, g, group_length + 1, memo)
    return memo[k]


all_springs = [line.split(" ")[0] for line in lines]
all_counts = [[int(c) for c in line.split(" ")[1].split(",")] for line in lines]
print(sum(
    dfs("?".join(5 * [springs]), 5 * counts, 0, 0, 0, {})
    for springs, counts in zip(all_springs, all_counts)
))
