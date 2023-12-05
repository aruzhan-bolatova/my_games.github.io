import os
import random

path = os.getcwd() # get the current working directory of the folder this file is stored in
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
TILE_WIDTH = RESOLUTION/NUM_COLS
TILE_HEIGHT = RESOLUTION/NUM_ROWS

# your classes come here
class Tile():
    def __init__(self,row=0, column=0):
        self.row = row
        self.column = column
        self.value = self.row * NUM_COLS + self.column
        self.img = loadImage(path + "/images/" + str(self.value) + ".png")
        
    def display(self):
        if self.value != 15:
            image(self.img, self.column * TILE_HEIGHT, self.row * TILE_WIDTH)
            noFill()
            strokeWeight(5)
            rect(self.column * TILE_HEIGHT, self.row * TILE_WIDTH, TILE_WIDTH, TILE_HEIGHT)
    def swap(self, other):
        tmp_value = self.value
        self.value = other.value
        other.value = tmp_value
        
        tmp_img = self.img
        self.img = other.img
        other.img = tmp_img
        
class Puzzle(list):
    def __init__(self):
        self.tiles_list()
        
    def tiles_list(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r,c))
        self.shuffle()
    def display(self):
        for tile in self:
            tile.display()
    
    def shuffle(self):
        for i in range(30):
            neighbor_dir = random.choice([LEFT, RIGHT, UP, DOWN])
            self.move(neighbor_dir)
            
    def get_empty_tile(self):
        for tile in self:
            if tile.value == 15:
                return tile
    
    def get_tile(self, row, column):
        for tile in self:
            if tile.row == row and tile.column == column:
                return tile
        return None
            
    def move(self, dir):
        empty_tile = self.get_empty_tile()
        if dir == RIGHT:
            neighbor_tile = self.get_tile(empty_tile.row, empty_tile.column - 1)
        elif dir == LEFT:
            neighbor_tile = self.get_tile(empty_tile.row, empty_tile.column + 1)
        elif dir == UP:
            neighbor_tile = self.get_tile(empty_tile.row + 1, empty_tile.column)
        elif dir == DOWN:
            neighbor_tile = self.get_tile(empty_tile.row - 1, empty_tile.column)
        
        if neighbor_tile != None:
            empty_tile.swap(neighbor_tile)
            
    def check_win(self):
        for tile in self:
            if tile.row * NUM_COLS + tile.column != tile.value:
                return False
        return True
    
    
def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)

def draw():
    background(0,0,0)
    puzzle.display()

def keyPressed():
    if keyCode in [LEFT, RIGHT, UP, DOWN]:
        puzzle.move(keyCode)
    
    if puzzle.check_win() == True:
        print("puzzle solved")
puzzle = Puzzle()




    
    
