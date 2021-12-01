
with open("input-1.txt", 'r') as f:
	lines = f.readlines()

# lines = ["199",
# 		"200",
# 		"208",
# 		"210",
# 		"200",
# 		"207",
# 		"240",
# 		"269",
# 		"260",
# 		"263"]

window = list(map(int, lines[0:3])) # Don't forget that the last index is not counted, it's [0, 3[
prevDepth = sum(window)
inc = 0
winCnt = 1
for i in range(1,len(lines)-2):
	window = list(map(int, lines[i:i+3]))
	winCnt += 1
	depth = sum(window)
	if depth > prevDepth:
		inc += 1
	prevDepth = depth

print(inc)
