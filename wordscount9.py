"""9. Write a program that takes a string and returns the number of words in it?
STEPS:
1) Take the input string from the user
2) convert it into a list to divide the string in to pieces
3) Now find the length of the list for the count of words"""

def wordscount9(): 

    string_data= input("Please enter a string to know the no.of words in it:")

# converting the string into list
    words = string_data.split(" ")

    print(type(words))
    print ("The no.of words present in the string:",len(words))# Printing the no.of words present in given string


wordscount9()





