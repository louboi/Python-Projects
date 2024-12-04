class Animal:
    def __init__(self, s, n):
        self.state = s
        self.size = n

    def feed(self):
        self.size += 1
        if self.size == 5:
            self.state = "FISH"

    def getstate(self):
        return self.state
    
    def getsize(self):
        return self.size
    
thisfish = Animal("Fish", 1)

print(thisfish.getstate() + " is the size of " + str(thisfish.getsize()))

while thisfish.getstate() != "FISH":
    thisfish.feed()

print("It is now a big " + thisfish.getstate())