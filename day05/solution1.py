with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

seeds = [int(s) for s in lines[0].split()[1:]]
maps: list[list[list[int]]] = []
map_i = -1
for line in lines[2:]:
    if line == "":
        continue
    if line.endswith(":"):
        map_i += 1
        continue
    if len(maps) == map_i:
        maps.append([])
    maps[map_i].append([int(i) for i in line.split()])

locations = []
for s in seeds:
    for m in maps:
        for dest_start, source_start, source_len in m:
            if s in range(source_start, source_start + source_len):
                s += dest_start - source_start
                break
    locations.append(s)
print(min(locations))
