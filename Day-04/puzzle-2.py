class Grid:
    def __init__(self):
    	self.g = list()

    def isWinner(self):
    	for line in self.g:
    		if sum(line) == -5:
    			return True
    	for i in range(len(self.g)):
    		# print("Column: {}".format([self.g[j][i] for j in range(len(self.g))]))
    		col = sum([self.g[j][i] for j in range(len(self.g))])
    		# print("Column score: {}".format(col))
	    	if col == -5:
	    		return True
    	return False

    def score(self):
    	score = 0
    	for line in self.g:
    		for value in line:
    			if value > -1:
    				score += value
    	return score

# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()

numbers = list(map(int,lines[0].split(',')))

grids = list()
grid = Grid()
grids.append(grid)
for line in lines[2:]:
	if line != "\n":
		grid.g.append(list(map(int,line.split())))
	else:
		grid = Grid()
		grids.append(grid)


winnerCountdown = len(grids)
for number in numbers:
	# print("Checking number {}".format(number))
	gridToRemove = list()
	for grid in grids:
		for i in range(len(grid.g)):
			for j in range(len(grid.g[i])):
				if grid.g[i][j] == number:
					# print("Removing {}".format(number))
					grid.g[i][j] = -1
		if grid.isWinner():
			winnerCountdown -= 1
			# print("Found winner, countdown: {}".format(winnerCountdown))
			gridToRemove.append(grid)
			# grids.remove(grid)
			if winnerCountdown == 0:
				print("Final score: {}".format(grid.score()*number))
		# print("Following grid is not a winner")
		# print(grid.g)
	for grid in gridToRemove:
		grids.remove(grid)
