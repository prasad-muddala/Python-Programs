"""if a string or a number is same as its reverse we call it as a palindrome"""

program-1:

#number palindrome

n=int(input("enter a value:"))
t=n
r=0
while n>0:
	l=n%10      #gives the remainder
	r=r*10+l
	n=n//10     #gives the integral value of the quotient
if r==t:
	print(t,"number  is palindrome")
else:
	print(t,"is not a palindrome")

"""logic is simple
we are reversing the value 
and storing the value in variable r 
and then comparing it with the original"""

