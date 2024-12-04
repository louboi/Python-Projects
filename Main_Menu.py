print("Welcome to the main menu! :)")
print("1 = Bird-Algorithm.py")
print("2 = Dice-Game.py")
print("3 = Juggling-Problem.py")
print("4 = Time-Traveler-Portal-Tracker.py")
print("5 = Class-Example.py")
print("6 = fish.py")
print("7 = Queues.py")
print("8 = car.py")
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
        with open("Juggling-Problem.py") as hello:
            exec(hello.read())
    case 4:
        with open("OOP/Time-Traveler-Portal-Tracker.py") as hello:
            exec(hello.read())
    case 5:
        with open("OOP/Class-Example.py") as hello:
            exec(hello.read())
    case 6:
        with open("OOP/fish.py") as hello:
            exec(hello.read())
    case 7:
        with open("OOP/Queues.py") as hello:
            exec(hello.read())
    case 8:
        with open("OOP/car.py") as hello:
            exec(hello.read())
    case 9:
        with open("oops.py") as hello:
            exec(hello.read())
    case 10:
        with open("oops.py") as hello:
            exec(hello.read())
    case _:
        print("Deleting System32 ....")
