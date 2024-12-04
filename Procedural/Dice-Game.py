import random

# Menu choises
def menuChoice():
    print("Option 1: Display rules")
    print("Option 2: Start new game")
    print("Option 3: Quit")
    choice = int(input("What is your choice? "))
    while choice < 1 or choice > 3:
        print("Idiot! ")
        choice = int(input("What is your choice? "))
    return choice

def displayRules():
    print("The rules of the game are as follows: \n\
Players take turns to throw two dice. \n\
If the throw is a ‘double’, i.e. two 2s, two 3s, etc., \
the player’s score reverts to zero  and their turn ends (etc.)")

def playerTurn(player,score):
    print("Your turn, ", player)
    anotherGo = "Y"
    scoreThisTurn = 0
    while anotherGo == "Y" or anotherGo == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("You rolled " + str(die1) + "and " + str(die2))
        if die1 == die2:
            scoreThisTurn = 0
            cumulativeScore = 0
            print("Bad luck! Press any key to continue")
            anyKey = input()
            anotherGo = "N"
        else:
            scoreThisTurn += die1+ die2
            cumulativeScore = score + scoreThisTurn
            print("Your score this turn is " + str(scoreThisTurn))
            print(str(player) + " Your cumulative score is " + str(cumulativeScore))
            if cumulativeScore >= 50:
                anotherGo = "N"
            else:
                print("Another go? (answer Y or N)")
                anotherGo = input()
    return cumulativeScore

def playGame():
    score1 = 0
    score2 = 0
    print("Enter player 1’s name: ")
    player1 = input()
    print("Enter player 2’s name: ")
    player2 = input()
    while score1 < 50 and score2 < 50:
        score1 = playerTurn(player1, score1)
        if score1 >= 50:
            print("You win!")
        else:
            score2 = playerTurn(player2, score2)
            if score2 >= 50:
                print("You win!")

#main program starts here
menuChoice()
choice = menuChoice
while choice != 3:
    if choice == 1:
        displayRules()
    else:
        playGame()
choice = menuChoice
print("Bye bitch :)")
