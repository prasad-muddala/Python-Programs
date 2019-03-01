task: to print the prime numbers with in the range of user input 

def prime(m):
	for n in range(2,m+1):
		for x in range(2,n):
			if n%x == 0:
				print(n, 'is even')
				break
		else:
			print(n,"is a prime number")

val=int(input("enter the range to find the prime numbers:"))
prime(val)

