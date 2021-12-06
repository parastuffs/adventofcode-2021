def parseCoord(line):
	x1 = int(line.split(',')[0])
	y1 = int(line.split(' ')[0].split(',')[1])
	x2 = int(line.split(' ')[2].split(',')[0])
	y2 = int(line.split(' ')[2].split(',')[1])
	return x1, y1, x2, y2

def printField(field):
	for l in field:
		print(l)


# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()

maxX = 0
maxY = 0
for line in lines:
	x1, y1, x2, y2 = parseCoord(line)
	maxX = max([maxX, x1, x2])
	maxY = max([maxY, x1, x2])
print(maxX, maxY)

field = [[0 for y in range(maxY+1)] for x in range(maxX+1)]

for line in lines:
	# print(line)
	x1, y1, x2, y2 = parseCoord(line)
	# print(x1, y1, x2, y2)
	if x1 == x2:
		for i in range(min([y1,y2]), max([y1,y2])+1):
			field[x1][i] += 1
	elif y1 == y2:
		for i in range(min([x1,x2]), max([x1,x2])+1):
			field[i][y1] += 1
	else:
		xVals = list()
		yVals = list()
		if x1 > x2:
			for i in range(x1, x2-1, -1):
				xVals.append(i)
		elif x1 < x2:
			for i in range(x1, x2+1):
				xVals.append(i)
		if y1 > y2:
			for i in range(y1, y2-1, -1):
				yVals.append(i)
		elif y1 < y2:
			for i in range(y1, y2+1):
				yVals.append(i)
		# print("Diagonal")
		# print(xVals, yVals)
		for i in range(len(xVals)):
			field[xVals[i]][yVals[i]] += 1
	# printField(field)

forbid = 0
for line in field:
	# print(line)
	for point in line:
		if point > 1:
			forbid += 1

print(forbid)
