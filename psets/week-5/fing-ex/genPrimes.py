def isPrime(n):
	for i in range(n - 1, 1, -1):
		if n%i == 0:
			return False
	return True

def genPrimes():
	prime = 2
	while True:
		if isPrime(prime):
			yield prime
			prime += 1
		else:
			prime += 1

