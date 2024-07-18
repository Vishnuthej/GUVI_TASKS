"""3.Write a python program that takes a string and returns a new string with all the vowels removed?

STEPS:
1) Take the input string and convert to list since string is immutable
2) take the list of vowels to compare with original string
3) use for loop to compare the vowel list elements present in the given string if yes .remove(element)
4) print the string as it is after removing the vowels """

def remove_vowels():
    string =input("Please enter a string:")#string
    #convert to a list
    result = list(string)
#take a tuple of vowels which should be standard for comparision
    vowels=('a','e','i','o','u','A','E','I','O','U')
#convert to a list 
    vowellist = list(vowels)
#print(type(vowellist))
    print(vowellist)
    print(result)
#iterate over the vowels to check if it is present in given string
    for letter in vowellist:
        while letter in result:
            result.remove(letter)#if vowel present in given string remove it 
    
    print ("The given string without the vowels is: " + ''.join(result))

remove_vowels()#function call



