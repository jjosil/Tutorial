for num in range(1, 101):
	if num % 5 == 0 and num % 3 == 0:
		print(num, ':', 'Fizz buzz')
	elif num % 5 == 0:
		print(num, ':', 'Fizz')
	elif num % 3 == 0:
		print(num, ':', 'buzz')
	else:
		print(num, ':', 'none')