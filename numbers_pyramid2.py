""" 2. Create a pyramid of numbers from 1 to 20 using FOR loop? """

def numbers_pyramid2():

#intialises the values for rows & numbers
    rows=8
    num=1

    #generating required no.of rows iterating with i
    for i in range(1,rows+1, +1):
        for j in range (rows, i, -1): #creating spaces before the numbers in each row
            print(" ",end= " ")

        for k in range (1, i, +1): #printing and incrementing the numbers to form a pyramid
            if (num > 20):
                break
            print(num, end=" ")
            num +=1


        print() 
    

numbers_pyramid2() 

             

# if I take rows as 6 its printing only till 15 why? the same logic worked in java for the values rows =6