#input is used to take in input from user
score1 = input("Enter the score 1: ")
score2 = input("Enter score 2:")
totalString = score1+score2
messageString = "Total score is %s"
print(messageString % totalString)

totalInt = int(score1) + int(score2)
messageString ="Total score is %s"
print(messageString % totalInt)

a = [24, "as it is", "abc", 2+2j]
print(a[0])
print(a[2])
a.append(20)
print(a)

# A tuple is similar to the list
a = 24,  "as it is", "abc", 2+2j
#some times brackets are used to define tuples
print(a[0])
print(a[2])

myDict = {}
myDict[1] = "one"
myDict['a'] = "alphabet"
print(myDict)
print(myDict.items())
print(myDict.keys())
print(myDict.values())

x = int(input('Enter the number: \t'))
    if x%2==0:
        if x%3==0:
            print("Number is divisible by 2 and 3")
        else:
            print("Number is divisible by 2 only ") 
            print("x%3= ", x%3)
    elif x%3==0:
        print("Number is not divisible by 2 and 3")
    else:
        print("Number is not divisible by 2 and 3")
        print("x%2= ", x%2)
        print("x%3= ", x%3)
print("Thank you")        
                           