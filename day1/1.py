import pdb

frequency = 0
with open('input.txt') as f:
	for line in f:
		if line[0] == '-':
			frequency = frequency - int(line[1:].rstrip())		
		elif line[0] == '+':
			frequency = frequency + int(line[1:].rstrip())		
print(frequency)
