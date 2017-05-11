def binary_numbers(n):
	if n == 1:
		return ['0', '1']
	binary_old = binary_numbers(n-1)
	binary_new = []
	for number in binary_old:
		binary_new.append(number + '0')
	for number in binary_old:
		binary_new.append(number + '1')
	return binary_new

print('Enter n, the number of bits in the binary number')
n = int(input())
print('Binary sequence of n bits written in L-R manner is')
print('\n'.join(binary_numbers(n)))
