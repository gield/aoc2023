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
for seed_start, seed_len in zip(seeds[::2], seeds[1::2]):
    current_ranges = [(seed_start, seed_start + seed_len)]
    next_ranges = []
    # go through each map 1 by 1
    for m in maps:
        # go through the current seed ranges and split them accordingly
        while current_ranges:
            range_start, range_end = current_ranges.pop()
            for dest_start, source_start, source_len in m:
                source_end = source_start + source_len
                diff = dest_start - source_start
                if range_start >= source_end or range_end <= source_start:
                    # no overlap -> the current range stays the same
                    continue
                elif range_start >= source_start and range_end <= source_end:
                    # the current range completely falls in the map range
                    # map all seeds according to the map range
                    next_ranges.append((range_start + diff, range_end + diff))
                elif range_start < source_start:
                    # the seed range overlaps at the start of the map range
                    # the seed start until the map start -> process later
                    current_ranges.append((range_start, source_start))
                    # the map start until the seed end -> map accordingly
                    next_ranges.append((source_start + diff, range_end + diff))
                elif range_end > source_end:
                    # the seed range overlaps at the end of the map range
                    # the seed start until the map end -> map accordingly
                    next_ranges.append((range_start + diff, source_end + diff))
                    # the map end until the seed end -> process later
                    current_ranges.append((source_end, range_end))
                break
            else:
                # no overlap -> the seeds stay the same
                next_ranges.append((range_start, range_end))
        current_ranges, next_ranges = next_ranges, []
    locations += current_ranges
print(min(loc[0] for loc in locations))
