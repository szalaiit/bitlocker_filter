from colorama import Fore, Back, Style


print("Plesase Choose a Mode:")

def Selection():
    print("1. Asphalt\n")
    print("2. Mixed\n")
    print("3. Off Road\n")
Selection()


while True:
    choice = str(input("Selected: "))

    if  choice == "1":
        print("Asphalt Selected")
        break
    if choice == "2":
        print("Mixed Selected")
        break
    if choice == "3":
        print("OffRoad Selected")
        break
    else:
        print("\nPlease select a valid choice:\n")
        Selection()


class Forza(object):
    #default values for Racing parts
    ARBarsMin = float(1) #Anti-Roll Bars Minimum value
    ARBarsMax = float(65) #Anti-Roll Bars Maximum value
    RStiffnessMinRace = float(3) #Rebound Stiffness Minimum value
    RStiffnessMaxRace = float(20) #Rebound Stiffness Maximum value
    RStiffnessMinRally = float(1) #Rebound Stiffness Minimum value
    RStiffnessMaxRally = float(10) #Rebound Stiffness Maximum value
    ATuningV = 0.11 #Asphalt percision tuning value
    MTuningVF = 0.12 #Mixed percision tuning value Front
    MTuningVR = 0.02 #Mixed percision tuning value Rear
    OTuningVF = 0.12 #Off Rado percision tuning value Front
    OTuningVR = 0.02 #Off Road percision tuning value Rear

    #Count middle values by ((Max - Min) * W + Min)
    def Common(self):

        self.wdf = float(input("Weight Distribution of your car: ")) #Front Weight Distripution of the car
        self.wdr = 100 - self.wdf #Rear Weight Disribution of the car
        self.SpringsMin = float(input("Min Springs: ")) #Minimum Value of the Springs
        self.SpringsMax = float(input("Max Springs: ")) #Maximum Value of the Springs

        #Counted Middle Value of the Anti-Roll Bars
        self.ARBarsFrontMV = (((self.ARBarsMax - self.ARBarsMin) * (self.wdf / 100)) + self.ARBarsMin)
        self.ARBarsRearMV = (((self.ARBarsMax - self.ARBarsMin) * (self.wdr / 100)) + self.ARBarsMin)

        #Counted Middle Value of the Springs
        self.SpringsFrontMV = (((self.SpringsMax - self.SpringsMin) * (self.wdf / 100)) + self.SpringsMin)
        self.SpringsRearMV = (((self.SpringsMax - self.SpringsMin) * (self.wdr / 100)) + self.SpringsMin)


    def Asphalt(self):

        self.ARBarsFrontRV = (self.ARBarsFrontMV - (self.ARBarsFrontMV * self.ATuningV))
        self.ARBarsRearRV = self.ARBarsRearMV

        self.SpringsFrontRV = (self.SpringsFrontMV - (self.SpringsFrontMV * self.ATuningV))
        self.SpringsRearRV = self.SpringsRearMV

        # Counted Middle Value of the Rebound Stiffness
        self.RStiffnesFrontMV = (((self.RStiffnessMaxRace - self.RStiffnessMinRace) * (self.wdf / 100))
                                 + self.RStiffnessMinRace)
        self.RStiffnessRearMV = (((self.RStiffnessMaxRace - self.RStiffnessMinRace) * (self.wdr / 100))
                                 + self.RStiffnessMinRace)

        self.RStiffnessFrontRV = (self.RStiffnesFrontMV - (self.RStiffnesFrontMV * self.ATuningV))
        self.RStiffnessRearRV = (self.RStiffnessRearMV - (self.RStiffnessRearMV * self.ATuningV))

        # Counted Middle Value of the Bound Stiffness
        self.BStiffnesFrontMV = (self.RStiffnesFrontMV * 0.5)
        self.BStiffnesRearMV = (self.RStiffnessRearMV * 0.5)

        self.BStiffnesFrontRV = (self.BStiffnesFrontMV + (self.BStiffnesFrontMV * 0.05))
        self.BStiffnesRearRV = self.BStiffnesRearMV

    def Mixed(self):

        self.ARBarsFrontRV = (self.ARBarsFrontMV - (self.ARBarsFrontMV * self.MTuningVF))
        self.ARBarsRearRV = (self.ARBarsRearMV - (self.ARBarsRearMV * self.MTuningVR))

        self.SpringsFrontRV = (self.SpringsFrontMV - (self.SpringsFrontMV * self.MTuningVF))
        self.SpringsRearRV = (self.SpringsRearMV - (self.SpringsRearMV * self.MTuningVR))

        self.RStiffnesFrontMV = (((self.RStiffnessMaxRally - self.RStiffnessMinRally) * (self.wdf / 100))
                                 + self.RStiffnessMinRally)
        self.RStiffnessRearMV = (((self.RStiffnessMaxRally - self.RStiffnessMinRally) * (self.wdr / 100))
                                 + self.RStiffnessMinRally)

        # Counted Middle Value of the Bound Stiffness
        self.BStiffnesFrontMV = (self.RStiffnesFrontMV * 0.45)
        self.BStiffnesRearMV = (self.RStiffnessRearMV * 0.4)

        self.RStiffnessFrontRV = (self.RStiffnesFrontMV - (self.RStiffnesFrontMV * self.MTuningVF))
        self.RStiffnessRearRV = (self.RStiffnessRearMV - (self.RStiffnessRearMV * self.MTuningVR))
        self.BStiffnesFrontRV = (self.BStiffnesFrontMV - (self.BStiffnesFrontMV * self.MTuningVF))
        self.BStiffnesRearRV = (self.BStiffnesRearMV - (self.BStiffnesRearMV * self.MTuningVR))

    def OffRoad(self):
        self.ARBarsFrontRV = (self.ARBarsFrontMV - (self.ARBarsFrontMV * self.OTuningVF))
        self.ARBarsRearRV = (self.ARBarsRearMV - (self.ARBarsRearMV * self.OTuningVR))

        self.SpringsFrontRV = (self.SpringsFrontMV - (self.SpringsFrontMV * self.OTuningVF))
        self.SpringsRearRV = (self.SpringsRearMV - (self.SpringsRearMV * self.OTuningVR))

        self.RStiffnesFrontMV = (((self.RStiffnessMaxRally - self.RStiffnessMinRally) * (self.wdf / 100))
                                 + self.RStiffnessMinRally)
        self.RStiffnessRearMV = (((self.RStiffnessMaxRally - self.RStiffnessMinRally) * (self.wdr / 100))
                                 + self.RStiffnessMinRally)

        # Counted Middle Value of the Bound Stiffness
        self.BStiffnesFrontMV = (self.RStiffnesFrontMV * 0.45)
        self.BStiffnesRearMV = (self.RStiffnessRearMV * 0.4)

        self.RStiffnessFrontRV = (self.RStiffnesFrontMV - (self.RStiffnesFrontMV * self.OTuningVF))
        self.RStiffnessRearRV = (self.RStiffnessRearMV - (self.RStiffnessRearMV * self.OTuningVR))
        self.BStiffnesFrontRV = (self.BStiffnesFrontMV - (self.BStiffnesFrontMV * self.OTuningVF))
        self.BStiffnesRearRV = (self.BStiffnesRearMV - (self.BStiffnesRearMV * self.OTuningVR))

    #def NotCool(self):
       # print ("Please select a valid choice")

# Alias Forza class
cls = Forza()

#Run Common function anyway to count the Middle Values
{
    "1":    cls.Common,
    "2":    cls.Common,
    "3":    cls.Common
}.get(choice)() # if you want to run 'NotCool" function: }.get(choice, cls.NotCool)()

#Run Selected function to count the Recomended Valuea
{
    "1":    cls.Asphalt,
    "2":    cls.Mixed,
    "3":    cls.OffRoad
}.get(choice)() # if you want to run 'NotCool" function: }.get(choice, cls.NotCool)()

print("\n-------------------------------------------------------------------\n")
print("Anti-Roll Bars Front Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.ARBarsFrontMV) + Style.RESET_ALL)
print("Anti-Roll Bars Front Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.ARBarsFrontRV) + Style.RESET_ALL)
print("Anti-Roll Bars Rear Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.ARBarsRearMV) + Style.RESET_ALL)
print("Anti-Roll Bars Rear Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.ARBarsRearRV) + Style.RESET_ALL)
print("-------------------------------------------------------------------\n")
print("Springs Front Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.SpringsFrontMV) + Style.RESET_ALL)
print("Springs Front Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.SpringsFrontRV) + Style.RESET_ALL)
print("Springs Rear Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.SpringsRearMV) + Style.RESET_ALL)
print("Springs Rear Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.SpringsRearRV) + Style.RESET_ALL)
print("-------------------------------------------------------------------\n")
print("Rebound Stiffness Front Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.RStiffnesFrontMV) + Style.RESET_ALL)
print("Rebound Stiffness Front Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.RStiffnessFrontRV) + Style.RESET_ALL)
print("Rebound Stiffness Rear Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.RStiffnessRearMV) + Style.RESET_ALL)
print("Rebound Stiffness Rear Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.RStiffnessRearRV) + Style.RESET_ALL)
print("Bump Stiffness Front Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.BStiffnesFrontMV) + Style.RESET_ALL)
print("Bump Stiffness Front Recommended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.BStiffnesFrontRV) + Style.RESET_ALL)
print("Bump Stiffness Rear Middle Value: ", Fore.BLUE + Style.BRIGHT +
      "{:.2f}\n".format(cls.BStiffnesRearMV) + Style.RESET_ALL)
print("Bump Stiffness Rear Recomended Value: ", Fore.RED + Style.BRIGHT +
      "{:.2f}\n".format(cls.BStiffnesRearRV) + Style.RESET_ALL)
print("-------------------------------------------------------------------")