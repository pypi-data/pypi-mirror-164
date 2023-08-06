# "Matrix" the New Python Class by Hasitha Gallella;
print(''' Instructions by Hasitha Gallella;
>>> Create your empty (mxn) matrix using "Matrix(m,n)". You can edit it from "edit_mat" method using a multi line string.
>>> Or you can get external inputs by "get_mat" method , row by row.
>>> After entering one row use "Enter key" to begin a new row.
>>> Each eliment should separate with a "Space".
>>> After entering all the rows again press extra "Enter" to exit the "get_mat" method.
''')

class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    def get_matrix(self, n, m):
        matrix = [[0] * m for _ in range(n)]
        return matrix

    def print_mat(self):
        for row in self.matrix:
          print(' '.join(str(e) for e in row),end="\n")

    def get_mat(self):
        Row1 = list(map(int,input().split()))
        Columns= len(Row1)
        go = Columns
        matrix1=[Row1]
        while go != 0:
          r=list(map(int,input().split()))
          go = len(r)
          matrix1.append(r)
        matrix1.pop()
        self.matrix= matrix1

    def edit_mat(self,mat_string):
        strlist1 = mat_string.split('\n')# --> ['Line 1', 'Line 2', 'Line 3']
        strlist1.pop();strlist1.pop(0)
        matrix1=[]
        for row in strlist1:
          matrix1.append(list(map(int,row.split())))
        self.matrix= matrix1


    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)  

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)
    
    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def getElement(self, i, j):
        return self.matrix[i-1][j-1]
    
    def setElement(self, i, j, element):
        self.matrix[i-1][j-1] = element
    
    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def getTranspose(self):
        return self.get_readable_matrix_string(self.transpose(self.matrix))
    
    def doTranspose(self):
        self.matrix = self.transpose(self.matrix)

    def multiply(self, matrix):
        result = [[0 for j in range(len(matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += self.matrix[i][k] * matrix[k][j]
        return result

    def getMultiply(self, matrix):
        return self.get_readable_matrix_string(self.multiply(matrix))
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num*other for num in row] for row in self.matrix])
    

print('''>>>
# Let's practicaly use this new python class and it's unique functions and methods; 
>>>'''  )     

print("Let's creat a empty 2x3 matrix ")
m1 = Matrix(2, 3)
print("Let's print the empty matrix m1 ")
m1.print_mat()
print("Let's edit the empty m1 matrix as below and then again print the edeited m1")
m1.edit_mat('''
1 2 3
4 5 6
''')
m1.print_mat()
print("Let's get external input values to m1 ")
m1.get_mat()
print("Let's print the (2,2) element of m1")
print(m1.getElement(1,2))
print("Let's change the (2,2) element of m1 to (-10)")
m1.setElement(1,2,-10)
print("Now let's print the transpose of new m1 matrix")
print(m1.getTranspose())
print("let's again print the m1, It'll look like exact way of previous m1")
m1.print_mat()
print("let's permenatly change m1 into it's transpose matrix, Can't undo this action!!!")
m1.doTranspose()
m1.print_mat()
print("let's create a new empty 2x3 matrix")
m2 = Matrix(2,3)
m2.print_mat()
print("Let's get external input values to m2 ")
m2.get_mat()
print("Let's multiply m2 by m1")
print(m2.getMultiply(m1))
print("You can multiply this using '*' sign too ")
print(m2 * m1)
print("Let's see our m2 matrix again, it wasn't chage")
m2.print_mat()
print(":et's multiply this m1 by 2 (multiply with integers)")
print(m2 * 2)