import sys
import random
board = [" "," "," "," "," "," "," "," "," "]

print("1",'|', "2", '|', "3")
print('----------')
print("4",'|', "5", '|', "6")
print('----------')
print("7",'|', "8", '|', "9")
y = input("choose x or o: ")

if y != "o" and y != "O" and y != "X" and y != "x":
    print(y)
    print("Default Value = x")
    y = "x"
    x = "o"
elif y == "o" or y == "O":
    y = "o"
    x = "x"
elif y == "x" or y =="X":
    y = "x"
    x = "o"




def printBoard():
    print(board[0],'|', board[1], '|', board[2])
    print('----------')
    print(board[3],'|', board[4], '|', board[5])
    print('----------')
    print(board[6],'|', board[7], '|', board[8])
    print('\n', '\n')



def CompTurn():
    spaceCheck =[]
    for abc in board:
        if abc != " ":
            spaceCheck.append(abc)
    if len(spaceCheck) == 0:
        print("TIE!")
        sys.exit()
    else:
        corners = [0,2,6,8]
        openCorners = []
        for d in corners:
            if board[d] == " ":
                openCorners.append(d)
        sides = [1,3,5,7]
        openSides = []
        for f in sides:
            if board[f] == " ":
                openSides.append(f)
        if checkGameWin() != "None":
            board[checkGameWin()] = x
        elif stopWin() != "None":
            board[checkGameWinUsr()] = x
        elif len(openCorners) != 0:
            m = random.randint(0, len(openCorners)-1)
            board[openCorners[m]] = x
        elif board[4] == " ":
            board[4] = x
        elif len(openSides) != 0:
            m = random.randint(0, len(openSides)-1)
            board[openSides[m]] = x

def checkGameWinUsr():
    i = 0
    while i <= 8:
        if board[i] == " ":
            board[i] = y
            if checkWin() == True:
                board[i] = " "
                return i
            else:
                board[i] = " "
        i = i+1
    return "None"




def checkGameWin():
    i = 0
    while i <= 8:
        if board[i] == " ":
            board[i] = x
            if checkWin() == True:
                board[i] = " "
                return i
            else:
                board[i] = " "

        i = i+1
    return "None"


def stopWin():
    i = 0
    while i <= 8:
        if board[i] == " ":
            board[i] = y
            if checkWin() == True:
                board[i] = " "
                return i
            else:
                board[i] = " "
        i = i+1
    return "None"

def checkWin():
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True
    elif board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[5] != " ":
        return True
    elif board[0] == board[4] == board[8] and board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        return True
    else:
        return False

def updateBoard():
    usrSquare = input("Enter a place to put %s in: " %(y) )
    usrSquare = int(usrSquare)
    m = []
    i = 0
    while i <= 8:
        if board[i] == " ":
            m.append(i)
        i = i+1
    f = random.randint(0, len(m)-1)
    if board[usrSquare-1] == " ":
        board[usrSquare - 1] = y
    else:
        print("Spot Taken, assigning random")

        board[m[f]] = y
    printBoard()
    CompTurn()
    printBoard()
    if checkWin() == True:
        print("Game Over")
        sys.exit()
    elif len(m) == 0:
        print("Game Over")
        sys.exit()
    else:
        updateBoard()
updateBoard()
