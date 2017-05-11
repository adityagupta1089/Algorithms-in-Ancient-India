print('Enter the line to generate Ghanapatha for:')
line = input()
words = line.split()
init_seq = [1, 2, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]
if len(words) < 3:
	print('String should be atleast 3 words long for Ghanapatha')
else:
	print()
	print('Ghanapatha for given text is:')
	print()
	for offset in range(-1, len(words) - 3):
		for word_index in init_seq:
			print(words[word_index + offset], end = ' ')
		print(';')
	print()
