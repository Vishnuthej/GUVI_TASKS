"""Using python's Object Oriented Programming Scheme (oops) kindly complete the foloowing tasks whihc is given as below
1) Create a pyhton class called circle with constructor which will take a list as an argument
 for the task. The list is [10, 501, 22, 37, 100, 999, 87, 351]

2) Create proper member variables inside the task if required and use them when necessary. 
For example for this task create a class private variables named pi = 3.141

3) From the given list create two class methods Area and Perimeter which will be going to
 calculate the Area and Perimeter. 
  
   STEPS: 
    1.Create a class and a private variable within the class
    2. Define a constructor method for instance variable 
    3. Define 2 methods for Perimeter & area
    4.Define 1 more method to iterate through the list of radii and to print perimeter & area 
     of the each radius. """


class Circle:
    _pi = 3.141
    def __init__(self,radii_list):
        self.radii = radii_list
        print("constructor")

    @classmethod
    def Calculate_Area(cls, radius):
        return cls._pi * radius * radius
        
   
    @classmethod
    def Calculate_Perimeter(cls, radius):
        return 2 * cls._pi * radius
    
    def area_and_perimeter(self):
        for radius in self.radii:
             area = Circle.Calculate_Area(radius)
             perimeter= Circle.Calculate_Perimeter(radius)
             print(f"Radius:{radius}")
             print(f"Perimeter:{perimeter:.2f}")
             print(f"Area:{area:.2f}")
             print('-'* 20)

 

if __name__ == "__main__":
    radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
    circle = Circle(radii_list)
    circle.area_and_perimeter()
    



 
        