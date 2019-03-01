Hi...
I'm prasad.
In this im giving you some python codes(programs) which are very basic and fundamentals to learn.

First thing first im assuming that you are familiar with python2/python3 basic syntax and how to run a python code in windows or linux 

Also im giving tutorials(description) regarding some important function you are going to use or see alot in the programs i gave

--------------------------------------------------------------------------------------------------------------------------------
Reduce():
---------
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working : 

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

---------------------------------------------------------------------------------------------------------------------------------------
map() :
-------
this function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
------
map(fun, iter)

Parameters :
----------
fun : It is a function to which map passes each element of given iterable.
-----
iter : It is a iterable which is to be mapped.
-----
NOTE : You can pass one or more iterable to the map() function.

--------------------------------------------------------------------------------------------------------------------------------------
