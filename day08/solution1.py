import itertools


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

instructions = lines[0]
network = {l[:3]: (l[7:10], l[12:15]) for l in lines[2:]}

current_node = "AAA"
for i, instr in enumerate(itertools.cycle(instructions)):
    current_node = network[current_node][0 if instr == "L" else 1]
    if current_node == "ZZZ":
        print(i + 1)
        break
