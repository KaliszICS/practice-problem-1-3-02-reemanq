''' 
    Lesson 3 - Using Strings 
    Author: Mr. Kalisz 
    Date Created: September 17th, 2024
    Date Last Modified: September 17th, 2024
'''

#Review

num = 5 #5
num = 3 + 8 #11
num = num  - 5 #6

print(num)

#print without new Line

print(4) #outputs the values in the brackets followed by a newline
print(45)

print("Hello There", end="")
print("Hello there again")

#Concatenation

word = "Hello"
word2 = "World"

print(word + word2) #By putting a + between two strings, they are put side by side
print(word + " " + word2) 

#Escape Character - "\"

#Changes the functionality of the character after it INSIDE a string

word = "\n" #newline character
print("Hello\nWorld")

word2 = "\t" #tab
print("Hello\tWorld")

print("\\") #escapes the escape character to make it a normal backslash

print("\"") #Escaoe the quotation mark so it does not end the string

print('"') #Can also use single/double quotes inside of the other
