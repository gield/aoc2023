import itertools
import math


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

instructions = lines[0]
network = {l[:3]: (l[7:10], l[12:15]) for l in lines[2:]}

a_nodes = [n for n in network if n[2] == "A"]
num_steps = []
for current_node in a_nodes:
    for i, instr in enumerate(itertools.cycle(instructions)):
        current_node = network[current_node][0 if instr == "L" else 1]
        if current_node[2] == "Z":
            num_steps.append(i + 1)
            break
print(math.lcm(*num_steps))
