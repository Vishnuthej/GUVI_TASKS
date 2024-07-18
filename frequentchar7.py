"""Write a program that takes a string and returns the most frequent character in it? 
STEPS: 
1) Take the input from the user
2) convert to the string to lower case to know the occurences of each char
3)find the maximum frequent char and print it """

def frequentchar():
    #Taking input string from the user and changing into lowercase
    string = input("Please enter the string:").lower()
    string = sorted(string) #it gives a sorted and conversion to a list sequence
    string_2 = {} #empty dictionary to make a count of characters
    #print (type(string_2))

#Iterating over the string to check each char present in dictionary 
    for char in string:
        if char in string_2:#if the char same from the dictionary increment the occurence value
            string_2[char]+= 1
        else:# if the char not there in dictionary keep the occurence as 1
            string_2 [char] =1 

# pickout the maximum occured key charecter value from the dictionary
    max_frequesnt_char = max(string_2, key=string_2.get)

    print (string_2)
    print(type(string_2))

    #Print the character whihc occurend for maximum no.of times  
    print("The most occured letter from the given input is: " + max_frequesnt_char) 

#Function call
frequentchar()
 