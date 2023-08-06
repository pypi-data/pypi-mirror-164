# "Matrix" the New Python Class by Hasitha Gallella;

class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    def get_matrix(self, n, m):
        matrix = [[0] * m for _ in range(n)]
        return matrix

    def print_mat(matrix):
        for row in matrix:
          print(' '.join(str(e) for e in row),end="\n")

    def input_mat(self):
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

    def str_mat(self,mat_string):
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
    
def add_numbers(a,b):
    return a+b

def sub_numbers(a,b):
    return a-b

def mul_numbers(a,b):
    return a*b

def div_numbers(a,b):
    return a/b