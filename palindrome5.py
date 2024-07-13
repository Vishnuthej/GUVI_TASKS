"""Write a program that takes a string and returns TRUE if it s a palindrome, FALSE otherwise.

STEPS: 
1) Get the input string from the user and convert into lower case
2)Remove all the spaces from the string
3)Reverse the string with negative step and empty start and end limits
4)Compare the string before and reversed one print the appropriate result"""


#Taking the input string & converting to the lower case
string = input("Enter the string to check whether its a palindrome :" ).lower()

#removing the spaces
string = string.replace(" ","")

print (string)

#comparing the string and reversed string with negative step 1 
if string == string[::-1]:
    print ("TRUE")

else: 
    print ("FALSE")
