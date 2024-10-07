x = 0
y = 0
z = 0
done = False

# Check rule 1
def rule1(x,y,z,done):
    if ((x + y + z) % 3) == 0:
        return False
    else:
        return True

# Check rule 2
def rule2(x,y,z,done):
    if x == z - 1:
        return True
    elif y == x - 1:
        return True
    elif z == y - 1:
        return True

# Main program
while done == False:
    x = int(input("Give me value 1: "))
    y = int(input("Give me value 2: "))
    z = int(input("Give me value 3: "))
    if rule1(x,y,z,done) == True:
        print("Invalid Pattern (Rule 1)")
    elif rule2(x,y,z,done) == True:
        print("Invalid Pattern (Rule 2)")
    else:
        quit()