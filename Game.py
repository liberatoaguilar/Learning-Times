board = []
for x in range(7):
    board.append(["0"] * 7)
def pb(board):
    for r in board:
        print(" ".join(r))
class Hero(object):
    health = "100"
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    def openpack(self):
        pack = [self.weapon]
        print(pack)
    def move(self):
        
         board[5][3] = "1"
nameask = input("What is your name? ")
weaponask = input("What is your weapon of choice? ")
hero = Hero(nameask, weaponask)
hero.move()
pb(board)
packq = input("Open Pack? (y/n) ")
if packq == "y":
    hero.openpack()
    def close():
        global closepack
        closepack = input("Close? (y/n) ")
        if closepack == "y":
            pb(board)
        else:
            close()
    close()
else:
    None
