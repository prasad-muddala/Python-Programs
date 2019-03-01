# Python-Codes
some basic python programs
#writing a factorial code in python using some inbuilt functions
------------
from operator import mul
from functools import reduce
n=int(input())
list=[]
for i in range(1,n+1):
	list.append(i)
	k=reduce(mul,list[:])
print(k)
