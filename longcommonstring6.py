"""6. Write a program that takes 2 strings and returns the longest common substring between them?

Steps:
1) Take the 2 strings & their lengths
2)Iterate through the substrings of the s1 
3)Pick a substring and check for it in s2
4) Find the longest one among the common strings in between s1 & s2 then print it """

#Function 
def longest_common_substring(s1, s2):
    longest = "" # An empty string
   
    #find the length of each string
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # Iterate through substrings of s1 with i & j indices
    for i in range(len_s1):
        for j in range(i + 1, len_s1 + 1):
            
            # Get the current substring
            substring = s1[i:j]
            
            # Check if the current substring is in s2
            if substring in s2:
               
                # Update the longest substring if the current one is longer than the previous
                if len(substring) > len(longest):
                    longest = substring
    return longest

#Input strings for the comparision
s1 = "vishnu thej Pavan venkata"
s2 = "venkatav pavan kumar  paravasthu"
print(s1,s2)
#Function call
result = longest_common_substring(s1, s2)
print("The longest common substring between 2 strings is:", result)
