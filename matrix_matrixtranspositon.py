#matrix of order 4*4 will be listed as follows

matrix=[[10,2,3,4],[10,3,4,5],[30,4,5,6],[40,5,6,7]]
print(matrix)
#transpose of the matrix
print('------------------')

transpose=[]
for i in range(4):
	transpose.append([row[i] for row in matrix])

print(transpose)

"""the logic is simple list of list is simply a matrix and
for transposing the matrix we are first appending the every first element of the
sublist of "matrix" into the transpose list 1st sublist and then second elements into 2nd sublist and so on"""
