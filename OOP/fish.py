def feed(state, size):
    size += 1
    print("Fish fed")
    if size == 5:
        state = "FISH"
    return state, size

thisfishstate = "Fish"
thisfishsize = 1

print(thisfishstate + " is of size " + str(thisfishsize))

while thisfishstate != "FISH":
    thisfishstate, thisfishsize = feed(thisfishstate, thisfishsize)

print("It is now a big " + thisfishstate)