#Implemetation off the array 2d dt using an array
class Array2D:
    #creates a 2-d array of size numRows x numcols
    def __init__(self, numRows, numCols):
        #creates a 1-D array to store an array referenc
        self._theRows = Array(numRows)
        #create a 1-D arrays for each of the 2-D arrays
        for i in range (numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)    
    #RETURNS THE NUMBER OF COLUMS IN THE 2-d ARRAY
    def numCols(self):
        return len(self._theRows[0])

    #clears the array by setting evert element to the default value
    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value) 
    #Gets the content of the element at position [1,j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple)==2, "Invalid number of array subscripts"   
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self.numRows() \
            and col >=0 and col < self.numCols(), \
                "Array subsript is out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]
    #sets the contents of the element at position[i,j to value]
    def __setitem__(self, ndxTuple,value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripte"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self.numRows()\
            and col >=0 and col < self.numCols(),\
                "array subscript is out of range"

        theidArray = self._theRows[row]
        theidArray [col] = value      
