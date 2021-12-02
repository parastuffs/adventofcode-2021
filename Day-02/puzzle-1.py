horiz = 0
depth = 0

with open("input.txt", 'r') as f:
	lines = f.readlines()

for line in lines:
	instr = line.split(' ')[0]
	dist = int(line.split(' ')[1])
	if instr == "forward":
		horiz += dist
	elif instr == "down":
		depth += dist
	elif instr == "up":
		depth -= dist

print("Final distance: {}, depth: {}, product: {}".format(horiz, depth, horiz*depth))