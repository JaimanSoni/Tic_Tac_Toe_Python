# Tic Tac Toe
import random
# declaring all variables

List = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
i = 0
X = "X"
O = "O"
count = 0
player = X
gameOver = False


# Creating Functions

def printBoard():

    print(List[0], " |", List[1], " |", List[2])
    print("------------")
    print(List[3], " |", List[4], " |", List[5])
    print("------------")
    print(List[6], " |", List[7], " |", List[8])


def shiftPlayer():
    global i
    global player

    if i % 2 == 0:
        player = X
        i = i + 1
    else:
        player = O
        i = i + 1


def playerInput():
    global i

    if player == X:
        n = int(input("Player 1's chance : "))

        if List[n - 1] == X or List[n - 1] == O:
            print("Enter a valid move")
            i = i - 1
        else:
            List[n - 1] = X
    else:
        print("Computer's chance")
        n = random.randint(1, 9)

        if List[n - 1] == X or List[n - 1] == O:
            print("Enter a valid move")
            i = i - 1
        else:
            List[n - 1] = O


def checkWin():
    global gameOver
    if List[0] == X and List[1] == X and List[2] == X:
        print("Player 1 won")
        gameOver = True
    elif List[3] == X and List[4] == X and List[5] == X:
        print("Player 1 won")
        gameOver = True
    elif List[6] == X and List[7] == X and List[8] == X:
        print("Player 1 won")
        gameOver = True
    elif List[0] == X and List[3] == X and List[6] == X:
        print("Player 1 won")
        gameOver = True
    elif List[1] == X and List[4] == X and List[7] == X:
        print("Player 1 won")
        gameOver = True
    elif List[2] == X and List[5] == X and List[8] == X:
        print("Player 1 won")
        gameOver = True
    elif List[0] == X and List[4] == X and List[8] == X:
        print("Player 1 won")
        gameOver = True
    elif List[2] == X and List[4] == X and List[6] == X:
        print("Player 1 won")
        gameOver = True

    elif List[0] == O and List[1] == O and List[2] == O:
        print("Player 2 won")
        gameOver = True
    elif List[3] == O and List[4] == O and List[5] == O:
        print("Player 2 won")
        gameOver = True
    elif List[6] == O and List[7] == O and List[8] == O:
        print("Player 2 won")
        gameOver = True
    elif List[0] == O and List[3] == O and List[6] == O:
        print("Player 2 won")
        gameOver = True
    elif List[1] == O and List[4] == O and List[7] == O:
        print("Player 2 won")
        gameOver = True
    elif List[2] == O and List[5] == O and List[8] == O:
        print("Player 2 won")
        gameOver = True
    elif List[0] == O and List[4] == O and List[8] == O:
        print("Player 2 won")
        gameOver = True
    elif List[2] == O and List[4] == O and List[6] == O:
        print("Player 2 won")
        gameOver = True


# Main Program Starts

print("Rules")
print("Player 1 = X and Player 2 = O")
print("Enter the index of the box in which you want to enter your move")
print("---------------------------------------------------------------------------------------------------------------")
printBoard()
while not gameOver:

    shiftPlayer()
    playerInput()
    printBoard()
    checkWin()
    count += 1

    if count == 9 or gameOver:
        List = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        i = 0
        count = 0
        ask = str(input("Do you want to play again(y/n) : "))

        if ask == 'y' or ask == 'Y':
            gameOver = False
            printBoard()
        else:
            gameOver = True
