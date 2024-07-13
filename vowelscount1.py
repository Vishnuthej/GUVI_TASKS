"""1. Write a python program to calculate the total nomber of vowels and count
of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited

1) Getting the repetions of each letter in the given string
2)creating a vowels dictionary with zero count
3)comparing both the dicionaries to pick out the vowels and their counts
   3.1)make sure the both dictioanries in same case
    3.2)using for loop print the vowels and count """

def vowelscount1 ():
    string = "Guvi Geeks Network Private Limited" #given string

    
    count= {} # empty dictionary
    print (type(count))
# picking each letter from the given string and the count of the repetition 
    for letters in string:
        keys = count.keys()
        if letters in keys:
            count [letters] = count [letters]+1
        else:
            count[letters] =1 
    print (count) # printing all the letters and their count in string in a dictionary form
#----------------------------------------
#converting the count dictionary in to lower case 
    lower_keys_count = {key.lower(): value for key, value in count.items()}

    #creating a dictionary of vowels with empty count of each vowel
    vowels_count ={'a':0,'e':0,'i':0,'o':0,'u':0}

    #comparing the obtained dictionary with vowels dict for the count of each vowel
    for vowel in vowels_count:
        if vowel in lower_keys_count:#picking each vowel from vowels_count & compare with lower_keys_count
            vowels_count[vowel] =lower_keys_count[vowel] #updating the count in vowels dict
            
    
    """this for loop goes through the above updated vowels dict and
      will print only the count is >0"""
    
    for vowel,count in vowels_count.items():
        if count>0:
            print(f"{vowel}:{count}")#a type of print statement
                  

#calling the function     
vowelscount1() 


