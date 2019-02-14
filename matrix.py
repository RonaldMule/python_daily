#implementation of the matrix adt using a 2-d array
from array import Array2D
class Matrix:
    #creates a matrix of size numRows x numCols  initialized to 0
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    #Returns the number of rows in the matrix
    def numRows(self):
        return self._theGrid.numRows()
    #Returns the number of columns in the matrix
    def numCols(self):
        return self._theGrid.numCols()
    #Returns the value of element(i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]
    #Sets the value of the element (i,j) to the value s:[]
    def __Setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar

    #scales the matrix by given scalar
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range (self.numCols()):
                self [r,c] *=scalar

    #creates and return a new matrix that is the transpose of the matrix
    def transponse(self):
        pass
    #creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation" 
                #Create the new matrix
        newMatrix = Matrix(self.numRows(), self.numCols()) 
        #Adding the corresponding elements in the two matrices

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] + rhsMatrix[r, c]
        return newMatrix
    #create and returns a new matrix that results from matrix subtraction
    def __sub__(self, matSub):
        assert matSub.numRows() == self.numRows() and \
            matSub.numCols() == self.numCols(), \
                "Matrix size is not copatiable for subtration"
                # crate a new matrix for subtraction
        newMatrix = Matrix(self.numRows(), self.numCols())
        #subtating the corresponding elements in the matrice
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[ r,c] = self[r,c] - matSub[r,c]
        return  newMatrix   
    def __mutiply__(self, matmult):
        assert matmult.numRows() == self.numRows() and  \
            matmult.numCols() == self.numRows(), \
                "Matrix size is not compatible for multiplication"
                #create a new matrix for multiplication
        newMatrix = Matrix(self.numRows(), self.numCols())

        #multipliying the corresponding elements in a matrice
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] * matmult[r,c]  
        return newMatrix                                 