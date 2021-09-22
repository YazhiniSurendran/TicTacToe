#Project Self Created
from random import randrange

def display_board(board):
    print("+-----" *3,"+",sep="")
    for row in range(3):
        print("|     " * 3, "|",sep = "")
        for col in range(3):
            print("|  ",board[row][col],"  ",sep = "", end = "")
        print("|")
        print("|     " * 3, "|",sep = "")
        print("+-----"*3,"+",sep="")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    usr_ip = False
    while not usr_ip:
        user_move = input("Enter your Move ")
        usr_ip = len(user_move) == 1 and user_move.isnumeric() and user_move != '0'
        if not usr_ip:
            print("Invalid option \nRetry")
            continue
        user_move = int(user_move) -1
        row = user_move // 3
        col = user_move % 3
        sign = board[row][col]
        usr_ip = sign not in ["O","X"]
        if not usr_ip:
            print("Field already occupied")
            continue
    board[row][col] = "O"
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] not in ['X','O']:
                free.append((i,j))
    return free
            
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    if sign == "O":
        who = 'You'
    elif sign == "X":
        who = 'I'
    else:
        who = None
    cross1 =cross2 = True
    for i in range(3):
        if board[i][0]==sign and board[i][1]==sign and board[i][2]==sign:
            return who
        if board[0][i]==sign and board[1][i]==sign and board[2][i]==sign:
            return who
        if board[i][i] != sign:
            cross1 = False
        if board[2-i][2-i] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None
        
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    free = make_list_of_free_fields(board)
    if len(free)>0:
        cp_move = randrange(len(free))
        row,col = free[cp_move]
        board[row][col] = "X"
    # The function draws the computer's move and updates the board.


gameBrd = [[3*j+i for i in range(1,4)] for j in range(3)]
gameBrd[1][1] = "X"
free = make_list_of_free_fields(gameBrd)

humanTurn = True

while len(free):
    display_board(gameBrd)
    if humanTurn:
        enter_move(gameBrd)
        victor = victory_for(gameBrd,"O")
    else:
        draw_move(gameBrd)
        victor = victory_for(gameBrd,"X")
    if victor != None:
        break
    humanTurn = not humanTurn
    free = make_list_of_free_fields(gameBrd)

display_board(gameBrd)
if victor == 'You':
    print("You won")
elif victor =='I':
    print("I won")
else:
    print("Tie!")



















