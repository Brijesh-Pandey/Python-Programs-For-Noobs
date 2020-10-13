# FizzBuzz: Return Fizz for multiples of 3 and Buzz for multiples of 2.
# Feel free to improve this algorithm ;)
def fizzBuzz(max=100):
	for n in range(1, max):
		print(n)
		if n % 3 == 0 and n % 2 == 0:
			print('FizzBuzz')
			continue
		elif n % 3 == 0:
			print('Fizz')
			continue
		elif n % 2 == 0:
			print('Buzz')

fizzBuzz()
