def start(n, e):
	print("Modulus (n):\t{}".format(n))
	print("Exponent (e):\t{}".format(e))
	
	p, q = find_prime_factors(n)
	print("First prime (p):\t{}".format(p))
	print("Second prime (q):\t{}".format(q))
	
	phi = (p - 1) * (q - 1)
	d = pow(e, -1, phi)
	print("\nPrivate key (d):\t{}".format(d))
	
	return d


def find_prime_factors(n):
	print("\nFinding primes. This may take a while...")
	
	# TODO: Quadratic sieve
	
	return 0, 0


if __name__ == '__main__':
	modulus = int(input("Enter modulus (decimal):\n"))
	exponent = int(input("Enter exponent (decimal):\n"))
	start(modulus, exponent)
