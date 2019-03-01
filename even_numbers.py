#to print all the prime numbers in a particular range using map 
#let sequence be represented as the 's'

n=int(input("enter a value  for the range:"))
s=range((n+1)/2)
def even(x,y):
	return x+y
p=map(even,s,s)
print(p)

"""i wrote this code using map() function so that you will be more familiar with the map function
i want you to try with using "divison by 2" that is the basic logic behind the even numbers """
