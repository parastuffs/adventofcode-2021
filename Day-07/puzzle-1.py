from statistics import median
# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()
positions = list(map(int, lines[0].split(',')))
med = median(positions)
fuel = 0
for pos in positions:
	fuel += abs(med - pos)
print(fuel)