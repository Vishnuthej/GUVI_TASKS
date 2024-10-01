"""4)Kindly visit the below URL and convert the UML diagram into a python class and its
 methods: https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md 

Inheritance
TVClass - Base class
LedTV class
PlasmaTV class

Part - A
Create a TV class with properties like brand, channel , price , inches ,
 OnOFF status and volume. Specify brand in a constructor parameter.
   Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels 
so if you try to set channel 60 the TV will stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50.
 (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the 
TV status like: "Panasonic at channel 8, volume 75".

Part - B : LED , Plasma
Inherit a TV class add additional properties like screen thickness, 
 energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , 
Backlight, DisplayDetails , which displays the detailed features of the TV""" 

class TV:
    def __init__(self,brand,price,inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.volume = 50
        self.channel = 1
        self.onoff = False
    
    def increase_volume(self,volume):
        if volume<100:
            volume +=1
        else:
            print("Volume is beyond the maximum")

    def decrease_volume(self,volume):
        if volume >0:
            volume -=1 
        else:
            print("volume is at the minimum range")
    
    def set_channel(self, new_channel):

        if 0 < new_channel < 50:
            print(f"Channel set to channel number{new_channel}")
        else:
            return (self.reset_tv())

    def onoff_status(self,status):
        if self.status== False:
            print("TV turned OFF")
        else: 
            print("TV turned ON")
            print (f"{self.brand}TV Details:\n"
                f"Price: Rs{self.price}, Inches: inches{self.inches}\n"
                f"Screen Thickness: {self.screenthickness}mm\n"
                f"Energy Usage: {self.energyusage}W\n"
                f"Lifespan: {self.lifespan}years \n"
                f"Refresh Rate: {self.ref_rate}HZ\n"
                f"Viewing Angle: {self.view_angle}degrees\n"
                f"Backlight: {self.backlight}\n"
                f"Display:{self.display}")
    def reset_tv(self):
        channel = 1
        volume = 50
        print("TV has been reset successfully\n The channel:1,volume: 50")
#----------------------------------------------------------------------------
#PART B
class LED(TV):
    def __init__(self,brand,price,inches,screenthickness,energyusage,lifespan,ref_rate,view_angle,backlight,display,status):
        super().__init__(brand,price,inches)
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.ref_rate = ref_rate
        self.view_angle = view_angle
        self.backlight = backlight
        self.display = display
        self.status = status

class Plasma(TV):
    def __init__(self, brand,price,inches,screenthickness,energyusage,lifespan,ref_rate,view_angle,backlight,display,status):
        super().__init__(brand,price,inches)
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.ref_rate = ref_rate
        self.view_angle = view_angle
        self.backlight = backlight
        self.display = display
        self.status = status
if __name__ == "__main__":
    child1 = LED("Samsung",30000,50,4,"100watts","9years","@60 HZ","30 degrees","YES","LED light",True)
    child1.onoff_status(True)
    print("-"*50)
    print("Change the channel")
    child1.set_channel(10)
    print("-"*50)
    print("Increase the volume to 25")
    child1.increase_volume(25)
   
    print("-"*100)
    child2= Plasma("LG Plasma",75000,52,2.4,300,"11 years","60Hz","160 degrees","NO","Gas based display",True)
    child2.onoff_status(True)
    print("-"*50)
    print("Decrease the volume to 0")
    child2.decrease_volume(0)
    print("-"*50)
    print("Try to change the channel 54")
    child2.set_channel(54)








    







        