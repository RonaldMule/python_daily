#implementation of the studentfileReader ADT using a text
#input source in which each field is stored on a separate line
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0        


class StudentFileReader:
    #create a new student reader instance.
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
    #open a connection to the input file
    def open(self):
        self._inputFile = open(self._inputSrc, "r")


    #close the connection to the input file
    def close(self):
        self._inputFile.close()
        self._inputFile = None
    def fetchRecord(self):
        #read the first line of the record
        line = self._inputFile.readline()
        if line =="":
            return None

        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()  
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())  
        student.gpa = float(self._inputFile.readline())
        return student
    
    #extract all student records and store them in a list
    # 
    def fetchAll(self):
        theRecords = list()   
        student = self.fetchRecord()

        while student != None:
            theRecords.append(student)
            student = self.fetchRecord() 
            return theRecords

    
#storage class used for an individual student
