from random import randint
from math import sqrt
board = []

for x in range(5):
    board.append(["O"] * 5)
  
def print_board(board):
    for row in board:
        print(' '.join(row))

print ("Let's play Battleship!")
print ("You have 8 turns to sink my ship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row+1)
print (ship_col+1)

for turn in range(8): 
    print ("Turn", str(turn+1))
    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print ("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print ("You guessed that one already.")
        elif round(sqrt((guess_row-ship_row)**2+(guess_col-ship_col)**2))<=1:
            print ("You just missed, your shot landed right beside my ship!")
            board[guess_row][guess_col] = "X"
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn==7:
        print ("You took too long!")
        print ("Game Over!")
        board[ship_row][ship_col] = "S"
    print_board(board)
        
