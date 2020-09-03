rows=int(input("Enter number of rows "))
cols=int(input("Enter number of Coloumns "))
matrix=[]
for i  in range(rows):
    element=[] 
    for j in range(cols):
        element.append(i*j)
    matrix.append(element)
print(matrix)