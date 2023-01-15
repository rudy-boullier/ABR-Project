from Abr import *


def main():
    """
    Main function
    """
    values = [5, 7, 6, 18, 3, 19, 6, 7, 8, 0, 1, 2, 4, 8, 9]
    abr = initAbr(values)
    print("Prefix: ", prefix(abr))
    print("Postfix: ", postfix(abr))
    print("Infix: ", infix(abr))
    print("Width: ", width(abr))


main()
