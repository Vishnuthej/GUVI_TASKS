"""4. write a program that takes a string and returns the number of unique characters in it?

STEPS:
1) Get the input from the user and convert into any case 
since the python is a case sensitive language
2)convert the string to set as it removes the repetitions of the chars
3)Find the length of the set and print it for the unique characters in it"""


#Getting the input and converting all the chars to lower case
string = input("Please enter a string: ").lower()

print (string)

string_to_set = set(string) #conversion of string to set

print (string_to_set)

unique_letters = len(string_to_set) # finding length of the set for unique letters count since the set removes duplicates


#printing the count of unique letters
print ("The number of unque characters in the given string are :",unique_letters)