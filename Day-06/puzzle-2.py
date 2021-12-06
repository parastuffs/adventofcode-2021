from alive_progress import alive_bar

# with open("test-input", 'r') as f:
with open("input", 'r') as f:
	lines = f.readlines()

fishes = [0 for x in range(9)]
for val in list(map(int,lines[0].split(','))):
	fishes[val] += 1
print("Init: {}".format(fishes))

for day in range(256):
	save = 0
	for i in range((len(fishes)-1), -1, -1):
		prevSave = save
		save = fishes[i]
		fishes[i] = prevSave
	fishes[8] += save
	fishes[6] += save
	# print("Day {}: {}".format(day+1, fishes))



	# for day in range(256):
	# 	bar()
	# 	# print("Day {}".format(day+1))
	# 	for i in range(len(fishes)):
	# 		fishes[i] -= 1
	# 		if fishes[i] < 0:
	# 			fishes[i] = 6
	# 			fishes.append(8)
		# print(fishes)
print("Fishes after 256 days: {}".format(sum(fishes)))