import random
import time
board = []
for i in range(3):
    board.append(["3"] * 3)
def pb(board):
    for row in board:
        print(" ".join(row))
board[1][1] = " "
pb(board)
st = "Starting on top Left going clockwise"
print(st)
print("-" * len(st))
total = 0
turns = 0
def roll(x,y):
    nums = 1,2,3,4
    diceroll = random.choice(nums)
    integer = int(board[x][y])
    if board[x][y] == "0":
        pass
    else:
        if diceroll == 1:
            print("Keep")
            global turns
            turns += 1
            pb(board)
        elif diceroll == 2:
            turns += 1
            print("Left")
            if x == 0 and y == 2 or x == 1 and y == 2:
                #Down
                down = int(board[x+1][y])
                board[x][y] = str(integer -1)
                board[x+1][y] = str(down +1)

                pb(board)
            elif x == 2 and y == 2 or x == 2 and y == 1:
                #My Left
                corleft = int(board[x][y-1])
                board[x][y] = str(integer -1)
                board[x][y-1] = str(corleft +1)
                pb(board)
            elif x == 2 and y == 0 or x == 1 and y ==0:
                #Up
                up = int(board[x-1][y])
                board[x][y] = str(integer -1)
                board[x-1][y] = str(up +1)
                pb(board)
            elif x == 0 and y == 0 or x == 0 and y == 1:
                #My Right
                left = int(board[x][y+1])
                board[x][y] = str(integer -1)
                board[x][y+1] = str(left +1)
                pb(board)
        elif diceroll == 3:
            turns += 1
            print("Star")
            board[x][y] = str(integer -1)
            global total
            total += 1
            pb(board)
        elif diceroll == 4:
            turns += 1
            print("Right")
            if x == 0 and y == 0 or x == 1 and y == 0:
                #Down
                down = int(board[x+1][y])
                board[x][y] = str(integer -1)
                board[x+1][y] = str(down +1)
                pb(board)
            elif x == 2 and y == 0 or x == 2 and y == 1:
                #My Right
                left = int(board[x][y+1])
                board[x][y] = str(integer -1)
                board[x][y+1] = str(left +1)
                pb(board)
            elif x == 2 and y == 2 or x == 1 and y == 2:
                #Up
                up = int(board[x-1][y])
                board[x][y] = str(integer -1)
                board[x-1][y] = str(up +1)
                pb(board)
            elif x == 0 and y == 2 or x == 0 and y == 1:
                #My Left
                corleft = int(board[x][y-1])
                board[x][y] = str(integer -1)
                board[x][y-1] = str(corleft +1)
                pb(board)
def Round():
    roll(0,0)
    time.sleep(0.1)
    roll(0,0)
    time.sleep(0.1)
    roll(0,0)
    time.sleep(0.1)
    roll(0,1)
    time.sleep(0.1)
    roll(0,1)
    time.sleep(0.1)
    roll(0,1)
    time.sleep(0.1)
    roll(0,2)
    time.sleep(0.1)
    roll(0,2)
    time.sleep(0.1)
    roll(0,2)
    time.sleep(0.1)
    roll(1,2)
    time.sleep(0.1)
    roll(1,2)
    time.sleep(0.1)
    roll(1,2)
    time.sleep(0.1)
    roll(2,2)
    time.sleep(0.1)
    roll(2,2)
    time.sleep(0.1)
    roll(2,2)
    time.sleep(0.1)
    roll(2,1)
    time.sleep(0.1)
    roll(2,1)
    time.sleep(0.1)
    roll(2,1)
    time.sleep(0.1)
    roll(2,0)
    time.sleep(0.1)
    roll(2,0)
    time.sleep(0.1)
    roll(2,0)
    time.sleep(0.1)
    roll(1,0)
    time.sleep(0.1)
    roll(1,0)
    time.sleep(0.1)
    roll(1,0)
def end():
    while True:
        if total != 24:
            Round()
        else:
            break
ask = input("Ready? ")
end()
print("Turns: " + str(turns))
