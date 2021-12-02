horiz = 0
depth = 0
aim = 0

with open("input.txt", 'r') as f:
	lines = f.readlines()

for line in lines:
	instr = line.split(' ')[0]
	dist = int(line.split(' ')[1])
	if instr == "forward":
		horiz += dist
		depth += aim*dist
	elif instr == "down":
		aim += dist
	elif instr == "up":
		aim -= dist

print("Final distance: {}, depth: {}, product: {}".format(horiz, depth, horiz*depth))