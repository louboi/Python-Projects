birdname = ["robin","blackbird","pigeon","magpie","bluetit","thrush","wren","starling"]
birdcount = [0,0,0,0,0,0,0,0]
bird = input("Please input the name of the bird (x to end): ")
birdfound = False
birdsobserved = 0


while bird != "x":
    birdfound = False
    for count in range(8):
        if bird == birdname[count]:
            birdfound = True
            birdsobserved = int(input(("Number observed")))
            birdcount[count] += birdsobserved
    if birdfound == False:
        print("Man you on some strong drugs!")
    bird = input("Please input the name of the bird (x to end): ")

for count in range(8):
    print(birdname[count], birdcount[count])