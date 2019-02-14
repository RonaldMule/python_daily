'''import string

import math
import re

print(string.ascii_lowercase)
print(math.pi)
print(math.e)
print(re.IGNORECASE)

a = 3
a = 2
b = "jane"
b="bob"
my_list = [1,2,3]
my_list[0] = 5
print(my_list)

class MyClass(object):
    pass
my_object = MyClass()
my_object.some_propety = 42

#more about inputs
height = int(input("Enter the box height: "))
width = int(input("Enter the box width: "))
print("The area of the box is %d" %(width*height))
words_to_convert = (input("Enter the words bayibe: ")) 
print(words_to_convert.capitalize())

def capitalize(word):
    word = input
'''
'''animals = ['cat', 'dog', 'fish', 'bison']
# a list of integers
numbers = [1,7, 34, 20, 12]
# an empty list
my_list = []

print(animals[0])
print(numbers[1])
#print(animals[6])

print(animals[-1])
print(numbers[-2])

print(animals[1:3])

print(animals[1:-1])


print(sorted(numbers))
print(list(reversed(numbers)))

total =0
number=0
while total <200:
    number += 1
    total += number**2
print("Total: %d" % total)    
print("last number :%d" %number) 

GUESSES_ALLOWED = 10
SECRET_WORD = "my self"

guesses_left = GUESSES_ALLOWED
guessed_word = None

while guessed_word !=SECRET_WORD and guesses_left:
    guessed_word = input("Guess a word")

    if guessed_word == SECRET_WORD:
        print("idiot")
    else:
        guesses_left -=1
        print("asshole")   

numbers = [1,2,3,4,5]
for i, num in enumerate(numbers):
    if num == 2:
        del numbers[i]
print(numbers) 
'''

'''x = range(1,10 + 1)
print (sum(x))
#for number in range(1,10):
    #print (sum(number))
total = 0
for i in range(1,10 +1):
    total += i
print(total)    

num = int(input("Please enter an integer: "))
num_fac = 1
for i in range(1, num +1):
    num_fac *=i
print("%d! = %d" %(num, num_fac)) 

'''
def myfunction(idiot):
    print(idiot.capitalize())

benx = input("Enter a word to capitalaixe ")
myfunction(benx)


# your code goes here
flat_list = []
def nearlyFlatten(new_list):
	for sublist in new_list:
		for item in sublist:
			flat_list.append(item)
		
	return sorted(flat_list, key=lambda x: x[0] )
	
my_list = [[[1,2,3],[9,10]],[[4,5],[6,7,8]]]

print (nearlyFlatten(my_list))
	

	
        







