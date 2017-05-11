def pingala_2_pow(n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return pingala_2_pow(n / 2) ** 2
	else: #if n % 2 == 1:
		return pingala_2_pow(n - 1) * 2

print('Enter n to get 2^n using pingala\'s algorithm')
n = int(input())
print('2^n using pingala\'s algorithm is: ' + str(pingala_2_pow(n)))
