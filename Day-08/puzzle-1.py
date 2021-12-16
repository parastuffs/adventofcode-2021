with open("input", 'r') as f:
# with open("test-input", 'r') as f:
	lines = f.readlines()

count = 0
for line in lines:
	outputs = line.split("|")[1].strip().split(' ')
	# print(outputs)
	for output in outputs:
		if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
			count += 1
			# print("incrementing because of {}".format(output))

print(count)