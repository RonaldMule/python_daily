from array import Array2D

#open the text file for reading
gradeFile = open(filename, "r")

numExams = int(gradeFile.readline())
numStudents = int(gradeFile.readline())

#create the 2-d array to store the grades
examGrades = Array2D(numStudents,numExams)

#extracting the grades from the remaining lines
i=0
for student in gradeFile:
    grades = student.split()
    for j in range(numExams):
        examGrades[i,j] = int(grades[j])
    i +=1

    gradeFile.close()
    #compute each students average exam grade
for i in range(numStudents) :
    #tarry the exam grades for the ith student
    total = 0
    for j in range(numExams):
        total += examGrades[i,j]

        #compute the average for each student
        examAvg = total /numExams
        print("%2d: %6.2f" %(i+1, examAvg))

