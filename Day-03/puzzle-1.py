with open("input", 'r') as f:
	lines = f.readlines()

bits = [0]*len(lines[0].strip())
gammaBits = [0]*len(lines[0].strip())
epsilonBits = [0]*len(lines[0].strip())
total = len(lines)
for line in lines:
	for i in range(len(line.strip())):
		bits[i] += int(line.strip()[i])

for i in range(len(bits)):
	if bits[i] > total/2:
		gammaBits[i] = '1'
		epsilonBits[i] = '0'
	else:
		gammaBits[i] = '0'
		epsilonBits[i] = '1'

gammaBinary = ''.join(gammaBits)
espilonBinary = ''.join(epsilonBits)

print("Gamma: {}, epsilon: {}, product: {}".format(int(gammaBinary,2), int(espilonBinary,2), int(gammaBinary,2)*int(espilonBinary,2)))