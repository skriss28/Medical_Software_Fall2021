# print("This is the Blood_Calculator.py module")
# print("It's name is {}".format(__name__))

#interface
def interface():
    print("")
    print("Blood Calculator")
    print("")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("3 - Cholesterol Analysis")
        print("9 - Quit")
        print("")
        choice = int(input("Enter your choice: "))
        #print(type(choice))
        print("")
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        elif choice == 3:
            Cholesterol_Driver()

    print(choice)
    return choice

#HDL functions
def HDL_Driver():
    HDL_Value = HDL_Input()
    HDL_Character = HDL_Analysis(HDL_Value)
    HDL_Output(HDL_Value, HDL_Character)

def HDL_Input():
    HDL_Value = int(input("Enter HDL Value: "))
    return HDL_Value

def HDL_Analysis(HDL_Value):
    if HDL_Value >= 60:
        return "Normal"
    elif 40 <= HDL_Value < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_Output(HDL_Value, HDL_Character):
    print("The HDL value of {} is considered {}".format(HDL_Value, HDL_Character))
    print("")
    
#LDL functions
def LDL_Driver():
    LDL_Value = LDL_Input()
    LDL_Character = LDL_Analysis(LDL_Value)
    LDL_Output(LDL_Value, LDL_Character)

def LDL_Input():
    LDL_Value = int(input("Enter LDL Value: "))
    return LDL_Value

def LDL_Analysis(LDL_Value):
    if LDL_Value >= 190:
        return "Very High"
    elif 160 <= LDL_Value < 190:
        return "High"
    elif 130 <= LDL_Value < 160:
        return "Borderline High"
    else:
        return "Normal"

def LDL_Output(LDL_Value, LDL_Character):
    print("The LDL value of {} is considered {}".format(LDL_Value, LDL_Character))
    print("")


# This is cholesterol analysis code from Alex Thomason
# Choleserol functions
def Cholesterol_Input():
    Cholesterol_Value = int(input("Enter Cholesterol Value: "))
    return Cholesterol_Value

def Cholesterol_Driver():
    Cholesterol_Value = Cholesterol_Input()
    Cholesterol_Character = Cholesterol_Analysis(Cholesterol_Value)
    Cholesterol_Output(Cholesterol_Value,Cholesterol_Character)

def Cholesterol_Analysis(Cholesterol_Value):
    if Cholesterol_Value < 200:
        return "Normal"
    elif 200 <= Cholesterol_Value <= 239:
        return "Borderline High"
    else :
        return "High"

def Cholesterol_Output(Cholesterol_Value, Cholesterol_Character) :
    print("The cholesterol value of {} is considered {}".format(Cholesterol_Value,Cholesterol_Character))
    print("")

if __name__ == "__main__":
    interface()