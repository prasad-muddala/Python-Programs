method-1

from operator import mul
from functools import reduce#to know about reduce function go to readme and read about reduce and map functions
n=int(input())
list=[]
for i in range(1,n+1):
	list.append(i)
	k=reduce(mul,list[:])
print(k)

"""in the above program we imported "mul" which basically multiplies two values instead of importing it we can simply define a function
for "mul" as shown in the below program"""

method-2

#declare a function for finding the product
def fact(x,y):
	return x*y
n=int(input("enter a value:"))
f=reduce(fact,range(1,n+1))

print(f)

