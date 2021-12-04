class Grid:
    def __init__(self):
    	self.g = list()

    def isWinner(self):
    	for line in self.g:
    		if sum(line) == -5:
    			return True
    	for i in range(len(self.g)):
	    	if sum([self.g[i][j] for j in range(len(self.g))]) == -5:
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


winnerFound = False
for number in numbers:
	print("Checking number {}".format(number))
	for grid in grids:
		for i in range(len(grid.g)):
			for j in range(len(grid.g[i])):
				if grid.g[i][j] == number:
					grid.g[i][j] = -1
		if grid.isWinner():
			winnerFound = True
			print(grid.score()*number)
			break
	if winnerFound:
		break
