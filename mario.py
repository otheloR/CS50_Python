from cs50 import get_int

def main():
    global num
    num = get_int("Height: ")

    while num < 1 or num > 8:
        num = get_int("Height: ")

    printer(num)


def printer(var1):



    # base case

    if var1 == 0:
        return

    # subverter

    printer(var1 - 1)

    # iterator

    for wee in range(num - var1):
        print(" ", end = "")

    for pee in range(var1):
        print("#", end = "")

    print()


  # the whole point is to get to the base case, returning breaks out of subverter, and into iterator




    '''

    if var1 == 1:
        print("#")

    else:
        print("#", end = "")
        printer(var1 - 1)

    '''



main()