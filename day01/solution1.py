with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

s = 0
for l in lines:
    nums = [int(c) for c in l if c.isnumeric()]
    s += 10 * nums[0] + nums[-1]
print(s)
