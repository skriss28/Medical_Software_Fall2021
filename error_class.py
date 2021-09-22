# a = "The sky is blue"
# print(a)

# for letter in a:
#    print(letter)

def function_name():
    
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt
    
    x = sqrt(4)
    print(x)
    
    try:
        string = "German Shepherd"
        dog = int(string)
        print(dog)
    except ValueError:
        print("Cannot convert string to an int")


def add_positive_integers(a, b):
    if a < 0 or b < 0:
        raise ValueError("Cannot add negative numbers")
    if type(a) is not int or type(b) is not int:
        raise TypeError("Cannot add non-integers")
    return a + b


def main():
    function_name()
    try:
        x = add_positive_integers(-2, 3)
        print(x)
    except ValueError:
        print("Got Value Error")
    except TypeError:
        print("Got Type Error")
    except:
        print("All Other Error")


if __name__ == "__main__":
    main()