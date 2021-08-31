def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        print("1 - HDL Analysis")
        choice = int(input("Enter your choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
    
    
    print(choice)
    return choice

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


interface()