
with open("input-1.txt", 'r') as f:
	lines = f.readlines()

prevDepth = int(lines[0])
inc = 0
for line in lines:
	depth = int(line)
	if depth > prevDepth:
		inc += 1
	prevDepth = depth

print(inc)
