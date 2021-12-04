with open("input", 'r') as f:
	lines = f.readlines()

# lines = ["00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010"]

bits = [0]*len(lines[0].strip())
gammaBits = [0]*len(lines[0].strip())
epsilonBits = [0]*len(lines[0].strip())
total = len(lines)
for line in lines:
	for i in range(len(line.strip())):
		bits[i] += int(line.strip()[i])

for i in range(len(bits)):
	if bits[i] >= total/2:
		gammaBits[i] = '1'
		epsilonBits[i] = '0'
	else:
		gammaBits[i] = '0'
		epsilonBits[i] = '1'

print("Gamma: {}, Espilon: {}".format(gammaBits, epsilonBits))

found = False
pos = 0
selection = list()
pool = lines[:]
while not found:
	print("Position: {}".format(pos))
	selection = list()
	total = 0
	for value in pool:
		total += int(value[pos])
	if total >= len(pool) / 2:
		majority = '1'
	else:
		majority = '0'

	for value in pool:
		if value[pos] == majority:
			selection.append(value)
	pool = selection[:]
	print(pool)
	if len(pool) == 1:
		oxy = pool[0]
		found = True
	else:
		pos += 1


found = False
pos = 0
selection = list()
pool = lines[:]
while not found:
	print("Position: {}".format(pos))
	selection = list()
	total = 0
	for value in pool:
		total += int(value[pos])
	if total < len(pool) / 2:
		minority = '1'
	else:
		minority = '0'

	for value in pool:
		if value[pos] == minority:
			selection.append(value)
	pool = selection[:]
	print(pool)
	if len(pool) == 1:
		co = pool[0]
		found = True
	else:
		pos += 1

oxy = ''.join(list(map(str, oxy)))
co = ''.join(list(map(str, co)))
print(int(oxy,2)*int(co,2))