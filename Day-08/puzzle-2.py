#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

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