print("Welcome to Number Guessing Game!")
number=35
playerNumbers=int(input("Guess a number between 0 to 50:"))
chance=3
while True:
    if chance!=0:
        if playerNumbers>number:
            print("You have",chance,"left")
            playerNumbers=int(input("Select a smaller number:"))
        elif playerNumbers<number:
            chance-=1
            print("You have",chance,"left")
            playerNumbers=int(input("Enter a bigger number:"))
        if playerNumbers==number:
            print("Congratulations. You won the game.")
            break
    if chance==0:
        print("Sorry, you lost the game")
        break
