def is_prime(number):
	if number <= 1:
		return False
	for num in range(0,number + 1):  
	    for i in range(2, number):  
	        if (number % i) == 0: 
	            return False
	return True
	   


def prime_list(number = int(input("Please enter a positive integer: "))): 
		primes = [num for num in range(0,number) if is_prime(num)]
		return primes

print(prime_list())