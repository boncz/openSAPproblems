def is_prime(number):
	if number <= 1:
		return False
	for x in range(2, number):
		if number % x == 0:
			return False
	return True

def prime_list(number = int(input("Please enter a positive integer: "))): 
		primes = [num for num in range(0, number + 1) if is_prime(num)]
		return primes

print(prime_list())