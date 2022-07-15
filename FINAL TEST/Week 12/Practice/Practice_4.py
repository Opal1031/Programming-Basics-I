import random as r

def getPlayerLetter():
    while True:
        letter = input("Do you want be X or O? : ").upper()
        if letter == "X":
            return "X", "O"
        elif letter == "O":
            return "O", "X"

def getFirst():
    isCom1st = r.randint(0, 1)
    who = ["computer", "player"]
    print("The ", who[isCom1st], "will go first.")
    return isCom1st

def drawBoard(board):
    print("+---+---+---+")
    print("ㅣ", board[7], "ㅣ", board[8], "ㅣ", board[9], "ㅣ")
    print("+---+---+---+")
    print("ㅣ", board[4], "ㅣ", board[5], "ㅣ", board[6], "ㅣ")
    print("+---+---+---+")
    print("ㅣ", board[1], "ㅣ", board[2], "ㅣ", board[3], "ㅣ")
    print("+---+---+---+")

def isSpaceFree(board, move):
    return board[move] == " "

def getComMove(board):
    for move in [5, 7, 9, 1, 3, 8, 4, 2, 6]:
        if isSpaceFree(board, move):
            return move

def getPlayerMove(board):
    while True:
        move = input("What is your next move? (1 ~ 9)")
        if move.isdigit():
            move = int(move)
            if move > 0 and move < 10 and isSpaceFree(board, move):
                return move

def makeMove(board, letter, move):
    board[move] = letter

def isSameLetter(board, line):
    return board[line[0]] == board[line[1]] and board[line[1]] == board[line[2]]

def isWin(board, move):
    for line in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9)]:
        if move in line and isSameLetter(board, line):
            return True
        return False


letters = getPlayerLetter()
isComTurn = getFirst()
board = [" "] * 10
drawBoard(board)

for i in range(9):
    if isComTurn:
        move = getComMove(board)
    else:
        drawBoard(board)
        move = getPlayerMove(board)
    makeMove(board, letters[isComTurn], move)
    
    if isWin(board, move):
        if isComTurn:
            print("You lose.")
        else:
            print("You have won the game!")
            break
    
    isComTurn = not isComTurn

else:
    print("The game is a tie!")
    drawBoard(board)