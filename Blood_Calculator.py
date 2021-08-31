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

interface()