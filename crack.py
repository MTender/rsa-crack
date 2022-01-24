import time
from math import gcd


# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
def factor(number):
	if number == 4:
		return 2
	elif number < 2:
		raise Exception("Modulus cannot be smaller than 2")
	
	x = 2
	cycle = 0
	while True:
		cycle += 1
		y = x
		for j in range(2 ** cycle):
			x = (x ** 2 + 1) % number
			fac = gcd(x - y, number)
			if fac > 1:
				return fac


def prime_check(number):
	if number % 2 == 0 or number % 3 == 0:
		return False
	for j in range(6, int(number ** 0.5) + 1, 6):
		if number % (j - 1) == 0 or number % (j + 1) == 0:
			return False
	return True


def start(n, e):
	print("Modulus (n):\t{}".format(n))
	print("Exponent (e):\t{}".format(e))
	
	p, q = find_prime_factors(n)
	print("First prime (p):\t{}".format(p))
	print("Second prime (q):\t{}".format(q))
	
	phi = (p - 1) * (q - 1)
	if phi == 0:
		raise Exception("Modulus cannot be prime".format(n))
	
	d = pow(e, -1, phi)
	print("\nPrivate key (d):\t{}".format(d))
	
	return d


def find_prime_factors(n):
	print("\nFinding primes. This may take a while...")
	
	p = factor(n)
	q = n // p
	if not prime_check(q):
		raise Exception("Modulus must be product of two primes".format(n))
	
	return p, q


def main():
	modulus = int(input("Enter modulus (decimal):\n"))
	exponent = input("Enter exponent (decimal, default 65537):\n")
	if exponent == "":
		exponent = 65537
	else:
		exponent = int(exponent)
		print()
	
	beginning = time.time()
	start(modulus, exponent)
	end = time.time()
	print("Time taken:\t{}s".format(round(end - beginning, 2)))


if __name__ == '__main__':
	main()
