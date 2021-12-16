from contextlib import suppress

def isLowest(plan, x, y):
	val = plan[x][y]

	n = list()

	if y > 0:
		n.append(plan[x][y-1])
	if x > 0:
		n.append(plan[x-1][y])
	if x < len(plan) - 1:
		n.append(plan[x+1][y])
	if y < len(plan[x]) - 1:
		n.append(plan[x][y+1])

	# print("Val: {}, neigh: {}".format(val, n))
	if val in n:
		# print("Return false, val in n")
		return False
	if val < min(n):
		# print("Val min, return true")
		return True
	else:
		return False


# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()

plan = [[0 for i in range(len(lines))] for j in range(len(lines[0].strip()))]

for y, line in enumerate(lines):
	for x, d in enumerate(line.strip()):
		plan[x][y] = int(d)

risk = 0
for i in range(len(plan)):
	for j in range(len(plan[i])):
		# print("Considering {}".format(plan[i][j]))
		if isLowest(plan, i, j):
			risk += 1 + plan[i][j]
			# print("Found a low point {}".format(plan[i][j]))
print(risk)