"""2. Write another python function to read from a text file. The function will take the name of 
the text file and display the content of the file into the console.
STEPS: 
1) Define a function to read the file and its content
  a)  open the file in read mode
  b)get the content with read()
  c)handle the unexxpected errors during the above steps"""

def read_from_file(filename):
    try:
        with open(filename, 'r')as file:
         content = file.read()
         print(f"Content of the file '{filename}':{content}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
    except Exception as e:
        print(f"An error occured: {e}")

filename = "file_21-09-2024_18-56-03.txt"
read_from_file(filename)







