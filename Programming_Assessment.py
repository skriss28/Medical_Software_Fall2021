# Programming Assessment
# BME 547 - Medical Software Design
# Author: Stevan Kriss
# Last Edited: 8/29/21


#Part One

#hardcode main list
Main_List = ["apple", "banana", "cranberry", "date", "eggplant", "fennel", "guava"]

#empty secondary lists
Short_Word_List = []
Long_Word_List = [];

#iterate through list
for fruit in Main_List:
    if len(fruit) <= 5:
        Short_Word_List.append(fruit)
    else:
        Long_Word_List.append(fruit)

#print output
print(" ")
print("Fruits with 5 Characters or Less:",*Short_Word_List, sep="\n",)
print(" ")
print("Fruits with 6 Characters or More:",*Long_Word_List, sep="\n")
print(" ")


# Part Two


#number sign function
def Positive_Num(Number):
    Number = float(Number)
    if Number > 0:
        true = 1
    else:
        true = 0
    return true

Number = input("Enter a number: ")
Num_Sign = Positive_Num(Number)
if Num_Sign == 1:
    print("Number is positive")
if Num_Sign == 0:
    print("Number is not positive")
print(" ")

#quadratic formula function
def Quad_Form(a,b,c):
    import math
    a = float(a)
    b = float(b)
    c = float(c)
    Solution_One = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    Solution_Two = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return Solution_One,Solution_Two

a = input("Enter a number for a: ")
b = input("Enter a number for b: ")
c = input("Enter a number for c: ")
[Solution_One,Solution_Two] = Quad_Form(a,b,c)
print(" ")
print("Solution #1 = ",Solution_One)
print("Solution #2 = ",Solution_Two)
print(" ")

#determine if roots are the same sign
#combination of the two functions above
a = input("Enter a number for a: ")
b = input("Enter a number for b: ")
c = input("Enter a number for c: ")
print(" ")
[Solution_One,Solution_Two] = Quad_Form(a,b,c)
Sign_One = Positive_Num(Solution_One)
Sign_Two = Positive_Num(Solution_Two)
if Sign_One == Sign_Two:
    print("Roots are the same sign!")
else:
    print("Roots are not the same sign")