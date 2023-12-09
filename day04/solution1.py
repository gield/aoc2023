with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total_num = 0
for i, card in enumerate(lines):
    split_card = card.split(": ")[1].split(" | ")
    winners = {int(n) for n in split_card[0].split()}
    ours = {int(n) for n in split_card[1].split()}
    if num_matches := len(winners & ours):
        total_num += 2 ** (num_matches - 1)
print(total_num)
