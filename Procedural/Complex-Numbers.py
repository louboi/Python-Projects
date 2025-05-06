r1 = int(input("Input the real part: "))
i1 = int(input("Input the imaginary part: "))
print("your number is: " + str(r1) + "+" + str(i1) + "i")
print("")
print("------------------------------------")
print("")
r2 = int(input("Input the real part: "))
i2 = int(input("Input the imaginary part: "))
print("your number is: " + str(r2) + "+" + str(i2) + "i")

rt = 0
it = 0

def add(r1, r2, rt, i1, i2, it):
    rt = r1 + r2
    it = i1 + i2
    print("your number is: " + str(rt) + "+" + str(it) + "i")

def multiply(r1, r2, rt, i1, i2, it):
    rt = (r1 * r2) - (i1 * i2)
    it = (r1 * i2) + (r2 * i1)
    print("your number is: " + str(rt) + "+" + str(it) + "i")

def negation(r1, r2, rt, i1, i2, it):
    rt = r1 - r2
    it = i1 - i2
    print("your number is: " + str(rt) + "+" + str(it) + "i")

def main():
    print("What do you want from the list below:")
    print("1) Addition")
    print("2) Multiplication")
    print("3) Negation")
    print("4) Inversion")
    c = int(input("Input the number: "))
    match c:
        case 1:
            add(r1, r2, rt, i2, i2, it)
        case 2:
            multiply(r1, r2, rt, i1, i2, it)
        case 3:
            negation(r1, r2, rt, i1, i2, it)
        case 4:
            print("4")

main()