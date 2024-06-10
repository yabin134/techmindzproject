#tick tac toe game
board=[" " for x in range(9)]
def printboard():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
   


    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def playermove(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print("Your turn player {}".format(number))
    choice=int(input("Enter your move (1-9): "))
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("That space is already occupied!")


def win(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or (board[3]==icon and board[4]==icon and board[5]==icon) or (board[6]==icon and board[7]==icon and board[8]==icon) or (board[0]==icon and board[3]==icon and board[6]==icon) or (board[1]==icon and board[4]==icon and board[7]==icon) or (board[2]==icon and board[5]==icon and board[8]==icon) or (board[0]==icon and board[4]==icon and board[8]==icon) or (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
    
def draw():
    if " " not in board:
        return True
    else:
        return False
    
while True:
    printboard()
    playermove("X")
    printboard()
    if win("X"):
        print(" Player 1 wins! Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break
    playermove("O")
    if win("O"):
        printboard()
        print("Player 2 wins Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break