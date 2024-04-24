matrix = [[1,2,3,], [4,5,6], [7,8,9]]
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("Transpose using for loop:",transposed)
     

# using single list comprehension
transposed1 = []
for i in range(len(matrix[0])):
    transposed_r = []
    transposed_r.append([row[i]for row in matrix])
    transposed_r.append(transposed_r)
print("transpose after single list comprehension:",transposed)
 

# using double list comprehension
transposed2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed after double list comprehension:",transposed2)