
frequency = 0
frequencies = {}
frequencies[frequency] = 1
duplicate_found = False
with open('input.txt') as f:
	while not duplicate_found:
		for line in f:
			operator = line[0]
			value = int(line[1:].rstrip())
			if operator == '-':
				frequency = frequency - value
			elif operator == '+':
				frequency = frequency + value
			if frequency in frequencies.keys():
				print(f'Frequency {frequency} seen twice.')
				duplicate_found = True
				break
			else:
				frequencies[frequency] = 1
		f.seek(0)
# for key in sorted(frequencies.keys()):
#     print(f'{key}: {frequencies[key]}')
print (frequency)
