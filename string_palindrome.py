"""compared to the number palindrome string palindrome is a lot easy"""
#code:

string=input()
reverse=string[::-1]     #[::-1] reverses the contents and is stored in the variable
if reverse==string:
	print(string,"is palindrome")
else:
	print(string,"is not palindrome")
