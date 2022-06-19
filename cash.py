from cs50 import get_float

def main():

    var_num = get_float("Changed owed: ")

    while var_num < 0:

        var_num = get_float("Changed owed: ")

    changer(var_num)


def changer(num):

    counter = 0

    while num > 0:

        if num >= .25:
            num -= .25
            num = round(num, 2)
            counter += 1

        elif num >= .10:
            num -= .10
            num = round(num, 2)
            counter += 1

        elif num >= .05:
            num -= .05
            num = round(num, 2)
            counter += 1

        else:
            num -= .01
            num = round(num, 2)
            counter += 1

    print(counter)



main()