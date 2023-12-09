with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

matches = []
for i, card in enumerate(lines):
    split_card = card.split(": ")[1].split(" | ")
    winners = {int(n) for n in split_card[0].split()}
    ours = {int(n) for n in split_card[1].split()}
    matches.append(len(winners & ours))

copies = [1] * len(lines)
for i, num_matches in enumerate(matches):
    for j in range(i + 1, i + num_matches + 1):
        copies[j] += copies[i]
print(sum(copies))
