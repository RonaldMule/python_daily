from studentfile import StudentFileReader

#name of the file to open
File_Name = "students.txt"

def main():
    #Extract the student records from the given text file
    reader = StudentFileReader(File_Name)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    #sort the list by id number. Each object is passed to lambda
    #expression which returns the idNum field of the object
    studentList.sort(key = lambda rec: rec.idNum)

    #print the student report
    printReport (studentList)

def printReport(theList):
    classNames = (None, "freshman", "sophomore", "junior", "senior")    

    #print the header
    print("List of students".center(50))
    print("")
    print("%-5s %-25s %-10s % -4s" %('ID','NAME', 'CLASS', 'GPA'))
    print("%5s %25s %10s %4s" %('-' *5, '-' *25,'-' *10, '-' *5))

    #print the body
    for record in theList:
        print("%5d %-25s %-10s %4.2f" %(record.idNum, record.lastName + ' '+ record.firstName, \
            classNames[record.classCode], record.gpa))
        #Add a footer 
        print("-"*50)
        print("Number of students:", len(theList))   

main()