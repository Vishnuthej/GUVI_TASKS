"""4.Write a python function to vaidate the Regular Expression for the following:
a) Email address
b) Mobile numbers of bangladesh
c) Telephone numbers of USA
d) 16 character Alpha-Numeric password composed of alphabets of upper case,
lower case, special characters, numbers"""
import re
#a) Function to validate the email address
def email_address(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Za-z]{2,7}$'
    
    # pass the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return("Valid Email")
    else:
        return("Invalid Email")
    

#b) Function to validate the mobile numbers of Bangladesh +880 XXNN-NNNNNN.
def mblnumber_Bangladesh(mobile_no):
    regex_2 = r'[+0-9]+[A-Z0-9]{4}+-[0-9]{6}'
    if (re.fullmatch(regex_2,mobile_no)):
        return("Valid Bangladesh phone number")
    else:
        return("Invalid Bangladesh phone number") 


#c)Function to validate the telephone numbers of USA (555) 555-1234
def USA_telephone(US_num):
    regex = r'^\([0-9]{3}\)[ ][0-9]{3}-[0-9]{2,4}$'
    
    # pass the string into the fullmatch() method
    if(re.fullmatch(regex, US_num)):
        return("Valid USA number")
    else:
        return("Not a USA number")

#d)Function to validate the password which is a 16 characters and alphanumeric + special chars
def Password(pswd):
    regex = r'^[A-Za-z0-9._%/&#+@!,^$*+-]{16}$'
            #r'^[A-Za-z0-9._%/&#+*$@!,^]{16}$'
   
    if (re.fullmatch(regex, pswd)):
        return "Valid Password"
    else:
        return "Invalid Password"


if __name__ == '__main__':
#call for the email validation function 
    email = "ankitrai326@gmail.com"
    print(email_address(email))

#call for the Bangladesh mobile number validation function
    mobile_no = "+880 1X89-987654"
    print(mblnumber_Bangladesh(mobile_no))

 #call for the USA Telephone number validation function
    US_num = "(555) 555-1244"    
    print(USA_telephone(US_num))

    pswd = "4056%%%%qw$_123V"
    print (Password(pswd))





  

