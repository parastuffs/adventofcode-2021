from statistics import median

def fuelConsumption(med, positions):
	score = 0
	for pos in positions:
		n = (abs(pos - med)+1)
		score += n*abs(pos - med)/2
	return score


# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()
positions = list(map(int, lines[0].split(',')))
start = median(positions)

found = False
skew = 0
best = fuelConsumption(start, positions)

while not found:
	skew += 1
	upScore = fuelConsumption(start + skew, positions)
	downScore = fuelConsumption(start - skew, positions)
	if upScore > best and downScore > best:
		found = True
	best = min([best, upScore, downScore])
print(best)