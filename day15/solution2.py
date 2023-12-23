with open("input.txt", "r") as f:
    lines = f.read().strip().split(",")


def h(s: str) -> int:
    value = 0
    for c in s:
        _, value = divmod((value + ord(c)) * 17, 256)
    return value


boxes = [{} for _ in range(256)]
for step in lines:
    if step.endswith("-"):
        label = step[:-1]
        box_i = h(label)
        if label in boxes[box_i]:
            del boxes[box_i][label]
    else:
        label, n = step.split("=")
        box_i = h(label)
        boxes[box_i][label] = int(n)

total_power = 0
for box_i in range(256):
    for slot_i, focal_length in enumerate(boxes[box_i].values()):
        total_power += (box_i + 1) * (slot_i + 1) * focal_length
print(total_power)
