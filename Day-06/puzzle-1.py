with open("test-input", 'r') as f:
# with open("input", 'r') as f:
	lines = f.readlines()

fishes = list(map(int,lines[0].split(',')))
print(fishes)

for day in range(80):
	# print("Day {}".format(day+1))
	for i in range(len(fishes)):
		fishes[i] -= 1
		if fishes[i] < 0:
			fishes[i] = 6
			fishes.append(8)
	# print(fishes)
print("Fishes after 80 days: {}".format(len(fishes)))