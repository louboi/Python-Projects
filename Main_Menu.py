print("Welcome to the main menu! :)")
print("1 = Bird-Algorithm.py")
print("2 = Dice-Game.py")
print("3 = Juggling-Problem.py")
print("4 = Time-Traveler-Portal-Tracker.py")
print("5 = Class-Example.py")
print("6 = fish.py")
print("7 = Queues.py")
print("8 = car.py")
print("9 = list.py")
print("10 = Dictionary.py")
print("11 = Complex-Numbers.py")
x = int(input("What project do you want: "))

match x:
    case 1:
        with open("Procedural/Bird-Algorithm.py") as hello:
            exec(hello.read())
    case 2:
        with open("Procedural/Dice-Game.py") as hello:
            exec(hello.read())
    case 3:
        with open("Procedural/Juggling-Problem.py") as hello:
            exec(hello.read())
    case 4:
        with open("Object-Orientated/Time-Traveler-Portal-Tracker.py") as hello:
            exec(hello.read())
    case 5:
        with open("Object-Orientated/Class-Example.py") as hello:
            exec(hello.read())
    case 6:
        with open("Object-Orientated/fish.py") as hello:
            exec(hello.read())
    case 7:
        with open("Object-Orientated/Queues.py") as hello:
            exec(hello.read())
    case 8:
        with open("Object-Orientated/car.py") as hello:
            exec(hello.read())
    case 9:
        with open("Procedural/list.py") as hello:
            exec(hello.read())
    case 10:
        with open("Procedural/Dictionary.py") as hello:
            exec(hello.read())
    case 11:
        with open("Procedural/Complex-Numbers.py") as hello:
            exec(hello.read())
    case _:
        print("Deleting System32 ....")