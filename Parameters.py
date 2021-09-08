def update(a):
    a[0] = a[0] + 2


def main():
    b = [5]
    x = update(b)
    print(b)
    print(x)


if __name__ == "__main__":
    main()
    
#if parameter is a str, int, float, boolean --> won't change in a function
#if parameter is a list, dictionary --> will change in a function