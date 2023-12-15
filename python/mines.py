from graphics import *
from random import randint, seed
from time import sleep, time

class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.bee = False
        self.flagged = False
        self.revealed = False
        self.flooding = False
        self.t = ''
    def show(self):
        if self.flagged:
            self.flagged = False
        if not self.revealed:
            rect = Rectangle(Point(self.col * 75, self.row * 75),Point((self.col+1) * 75, (self.row+1) * 75))
            rect.setFill(color_rgb(170,170,170))
            rect.setWidth(2)
            rect.draw(win)
            self.revealed = True
        if self.bee:
            self.revealed = True
            showall(False)

            alert = GraphWin("You Hit a mine!",300,100)
            txt = Text(Point(150,30),"You lose.")
            retry = Text(Point(150,65), "Retry?(y/n)")
            txt.draw(alert)
            retry.draw(alert)
            while True:
                try:
                    key_input = alert.getKey()
                except:
                    win.close()
                    global playing
                    playing = False
                    return
                if key_input == 'y' or key_input == 'Y':
                    alert.close()
                    win.close()
                    main()
                    break
                elif key_input == 'n' or key_input == 'N':
                    global playing
                    playing = False
                    alert.close() 
                    win.close()
                    break    
        else:
            neighbours = self.countNeighbours()
            if neighbours == 0:
                if not self.flooding:
                    floodfill(self)
            else:
                self.t = Text(Point(37.5 + self.col * 75, 37.5 + self.row * 75), neighbours)
                self.t.setSize(32)
                self.t.draw(win)
    def flag(self):
        if not self.revealed:
            if not self.flagged:
                self.flagged = True
                self.t = Text(Point(37.5 + self.col * 75, 37.5 + self.row * 75), 'F')
                self.t.setSize(32)
                self.t.setFill('red')
                self.t.draw(win)
            else:
                self.t.undraw()
                self.flagged = False

        flag_count = 0
        invalid = False
        for i in grid:
            for j in i:
                if j.flagged and not j.bee:
                    invalid = True
                if j.flagged and j.bee:
                    flag_count += 1

        if flag_count == 6 and not invalid:
            showall(True)
            alert = GraphWin("You WIN!!!",300,100)
            txt = Text(Point(150,30),"You won the game!")
            retry = Text(Point(150,65), "Replay?(y/n)")
            txt.draw(alert)
            retry.draw(alert)
            while True:
                try:
                    key_input = alert.getKey()
                except:
                    win.close()
                    global playing
                    playing = False
                    return
                if key_input == 'y' or key_input == 'Y':
                    alert.close()
                    win.close()
                    main()
                    break
                elif key_input == 'n' or key_input == 'N':
                    global playing
                    playing = False
                    alert.close() 
                    win.close()
                    break
        
    def countNeighbours(self):
        r = self.row
        c = self.col
        n = 0
        for i in [r-1,r,r+1]:
            for j in [c-1,c,c+1]:
                if (not (i == r and j == c)) and i >= 0 and i <= 7 and j >=0 and j <= 7:
                    if grid[i][j].bee:
                        n+=1
        return n


def floodfill(self):
    self.flooding = True
    r = self.row
    c = self.col
    n = 0
    for i in [r-1,r,r+1]:
        for j in [c-1,c,c+1]:
            if i >=0 and i <= 7 and j >=0 and j <= 7 and grid[i][j].revealed == False and grid[i][j].bee == False:
                grid[i][j].show()
                if grid[i][j].countNeighbours() == 0:
                    floodfill(grid[i][j])

def showall(won):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = grid[i][j]
            if not cell.revealed:
                rect = Rectangle(Point(cell.col * 75, cell.row * 75),Point((cell.col+1) * 75, (cell.row+1) * 75))
                rect.setFill(color_rgb(170,170,170))
                rect.setWidth(2)
                rect.draw(win)
                cell.revealed = True
            if cell.bee:
                cell.revealed = True
                rect = Rectangle(Point(cell.col * 75, cell.row * 75),Point((cell.col+1) * 75, (cell.row+1) * 75))
                if won == True:
                    rect.setFill('green')
                else:
                    rect.setFill('red')
                rect.setWidth(2)
                rect.draw(win)
                b = Circle(Point(37.5 + cell.col * 75, 37.5 + cell.row * 75), 18)
                b.setFill('black')
                b.draw(win)
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k == 0 or l == 0:
                            spoke = Line(Point(37.5 + cell.col * 75, 37.5 + cell.row * 75), Point((37.5 + 25 * k) + cell.col * 75, (37.5 + 25 * l) + cell.row * 75))
                        else:
                            spoke = Line(Point(37.5 + cell.col * 75, 37.5 + cell.row * 75), Point((37.5 + 17 * k) + cell.col * 75, (37.5 + 17 * l) + cell.row * 75))
                        spoke.setWidth(5)
                        spoke.draw(win)
                        
            else:
                neighbours = cell.countNeighbours()
                if neighbours == 0:
                    pass
                else:
                    t = Text(Point(37.5 + cell.col * 75, 37.5 + cell.row * 75), neighbours)
                    t.setSize(32)
                    t.draw(win)

def drawboard():
    board = []
    for i in range(9):
        h = Line(Point(0 + 75 * i, 0), Point(0 + 75 * i, 600))
        h.setWidth(2)
        v = Line(Point(0, 0 + 75 * i), Point(600, 0 + 75 * i))
        v.setWidth(2)
        board.append(v)
        board.append(h)
    for k in range(len(board)):
        board[k].draw(win)

def get_input():
    try:
        click = win.getMouse()
    except:
        global playing
        playing = False
        return
    row = int(click.getY() / 75)
    col = int(click.getX() / 75)
    if row > 7:
        row = 7
    if col > 7:
        col = 7
    
    start = time()
    while time() - start < 0.15:
        if win.checkMouse():
            grid[row][col].flag()
            break
    else:
        grid[row][col].show()
    
def main():
    global grid
    global playing
    global win
    grid = []
    playing = True
    for rows in range(8):
        grid.append([])
        for cols in range(8):
            grid[rows].append(Cell(rows, cols))

    seed()
    mine_num = 0
    while mine_num < 6:
        cell_row = randint(0,7)
        cell_col = randint(0,7)
        if not grid[cell_row][cell_col].bee:
            grid[cell_row][cell_col].bee = True
            mine_num+=1
            

    win = GraphWin("Minesweeper",601,601);

    drawboard()

#main
win = None
playing = True
grid = []

main()

while playing:
    get_input()
    
print "Thank you for playing Minesweeper!"
