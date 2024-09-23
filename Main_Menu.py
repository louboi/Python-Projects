print("Welcome to the main menu! :)")
print("1 = Bird-Algorithm.py")
print("2 = Dice-Game.py")
print("3 = ")
print("4 = ")
print("5 = ")
print("6 = ")
print("7 = ")
print("8 = ")
print("9 = ")
print("10 = ")
x = int(input("What project do you want: "))

match x:
    case 1:
        with open("Bird-Algorithm.py") as hello:
            exec(hello.read())
    case 2:
        with open("Dice-Game.py") as hello:
            exec(hello.read())
    case 3:
        with open("oops.py") as hello:
            exec(hello.read())
    case 4:
        with open("oops.py") as hello:
            exec(hello.read())
    case 5:
        with open("oops.py") as hello:
            exec(hello.read())
    case 6:
        with open("oops.py") as hello:
            exec(hello.read())
    case 7:
        with open("oops.py") as hello:
            exec(hello.read())
    case 8:
        with open("oops.py") as hello:
            exec(hello.read())
    case 9:
        with open("oops.py") as hello:
            exec(hello.read())
    case 10:
        with open("oops.py") as hello:
            exec(hello.read())
    case _:
        print("Deleting System32 ....")