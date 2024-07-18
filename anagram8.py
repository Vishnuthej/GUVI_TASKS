"""8. Write a python program that takes a string and returns 'TRUE' if it is an ANAGRAM of another string, 
'FALSE' otherwise?

STEPS: 
1) Take input as 2 strings from the user
2) Convert them in to same case,remove spaces & get sorted to easily compare the characters in them
3) compare them if all characters are same print "TRUE" otherwise print "FALSE"
 """
#Taking Input from the user
String1 = input("Enter a string1:")
String2 = input("Enter a string2:")
#Changing the case & replacing the spaces with empty string
String1 = String1.replace(" ","").lower()
String2 = String2.replace(" ","").lower()

#print(String2)
#print(String1)
#Use sorted method to arrange them in alphabetical order for easy comparision of all characters
if sorted(String1)== sorted(String2):
    print ("TRUE")
else:
    print("FALSE")
