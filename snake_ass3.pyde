import os, random
import time

path = os.getcwd()
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
TILE_WIDTH = 30
TILE_HEIGHT = 30
NUM_COLS = CANVAS_WIDTH / TILE_WIDTH   #20 columns
NUM_ROWS = CANVAS_HEIGHT / TILE_HEIGHT  #20 rows
key_enabled = False
snake_alive = False
def setup():
    size(CANVAS_WIDTH, CANVAS_HEIGHT)
    background(205)
    
def draw():
    if frameCount % 12 == 0:
        background(205)
        game.display()
        
        
class SnakeElement:  #snake element attributes are initialized here
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.dir = dir
                
class Head(SnakeElement): #inherits from SnakeElements and displays head based on direction
    def __init__(self, column, row, dir):
        SnakeElement.__init__(self, NUM_COLS//2, NUM_ROWS//2)
        self.dir = dir
        self.img1 = loadImage(path + "/snake_images/head_left.png")
        self.img2 = loadImage(path + "/snake_images/head_up.png")
        
    def display(self): #display of head image based on direction 
        if self.dir == RIGHT:
            image(self.img1, self.column * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT, 30, 0, 0, 30)
        elif self.dir == LEFT:
            image(self.img1, self.column * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        elif self.dir == UP:
            image(self.img2, self.column * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        elif self.dir == DOWN:
            image(self.img2, self.column * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT, 30, 30, 0, 0)
    
class Tail(SnakeElement): #inherits from SnakeElements and siaplayed based on colors
    def __init__(self, column, row, tail_color): 
        SnakeElement.__init__(self, column, row)
        self.tail_color = tail_color
        self.tail_colors = ['green', 'red', 'yellow']
        
    def display(self): 
        if self.tail_color == 'green':
            noStroke()
            fill(80, 153, 32)
        elif self.tail_color == 'red':
            noStroke()
            fill(173, 48, 32)
        elif self.tail_color == 'yellow':
            noStroke()
            fill(251, 226, 76)
        ellipse(self.column * TILE_WIDTH + 15, self.row * TILE_HEIGHT + 15, TILE_WIDTH, TILE_HEIGHT)
        
class Snake: #gathers all snake elements and saves in elements_list
    def __init__(self):
        head = Head(NUM_COLS//2, NUM_ROWS//2, RIGHT)
        tail1 = Tail(NUM_COLS//2 - 1, NUM_ROWS//2, 'green')
        tail2 = Tail(NUM_COLS//2 - 2, NUM_ROWS//2, 'green')
        self.elements_list = [head, tail1, tail2]
        self.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}  
        
    def display(self): #display of each element - whole snake display
        for element in self.elements_list:
            element.display()
            
    def move(self, dir_col, dir_row):  #moving snake starting from last element (copies the coordinates)
        global snake_alive
        if snake_alive == True:      
            for i in range(len(self.elements_list) - 1, 0, -1):
                self.elements_list[i].column = self.elements_list[i-1].column
                self.elements_list[i].row = self.elements_list[i-1].row
            self.elements_list[0].column += dir_col
            self.elements_list[0].row += dir_row
        
    def change_dir(self): #changes directions and enables the key handler (direction) so the snake moves
        if self.key_handler[LEFT] == True:
            self.elements_list[0].dir = LEFT
            self.move(-1,0)

        elif self.key_handler[RIGHT] == True:
            self.elements_list[0].dir = RIGHT
            # while snake.elements_list[0].column != NUM_COLS:
            self.move(1,0)
            
        elif self.key_handler[UP] == True:
            self.elements_list[0].dir = UP
            self.move(0,-1)
            
        elif self.key_handler[DOWN] == True:
            self.elements_list[0].dir = DOWN
            self.move(0,1)
        

class Fruit: #creates fruits
    def __init__(self): 
        self.img_apple = loadImage(path + "/snake_images/apple.png")
        self.img_banana = loadImage(path + "/snake_images/banana.png")
        self.value = random.randint(0,1)
        self.col = random.randint(0,NUM_COLS-1) 
        self.row = random.randint(0,NUM_ROWS-1) 
        
    def display(self): #fruit is displayed randomly except it does not overlap with snake element
        for i in range(len(game.snake.elements_list)): 
            if game.snake.elements_list[i].column == self.col and game.snake.elements_list[i].row == self.row:
                self.col = random.randint(0,NUM_COLS-1) 
                self.row = random.randint(0,NUM_ROWS-1)
            else:
                if self.value == 0:
                    image(self.img_apple, self.col * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                else:
                    image(self.img_banana, self.col * TILE_WIDTH, self.row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        
class Game: #whole game is controlled here
    def __init__(self):
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT
        self.num_rows = NUM_ROWS
        self.num_cols = NUM_COLS
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0

    def display(self): #called in draw fucntions (5 times per second)
        fill(0)
        textSize(20)
        text("Score: " + str(self.score), 500, 20)
        self.snake.display()
        self.fruit.display()
        self.snake.change_dir()
        self.check_collision()  
        self.full_board()
        self.self_collision()
        self.wall_collision()

    #CHECKING HEAD COLLISION WITH A FRUIT    
    def check_collision(self): 
        if self.snake.elements_list[0].column == self.fruit.col and self.snake.elements_list[0].row == self.fruit.row:
            self.current_fruit_value = self.fruit.value
            self.fruit = Fruit()  #new fruit
            
            if self.current_fruit_value == 0:   #appending a new tail (with according color)
                self.snake.elements_list.append(Tail(self.snake.elements_list[-1].column, self.snake.elements_list[-1].row, 'red'))
            elif self.current_fruit_value == 1:
                self.snake.elements_list.append(Tail(self.snake.elements_list[-1].column, self.snake.elements_list[-1].row, 'yellow'))
            
            self.score += 1  #increments score by one after each collision and it is displayed on right upper corner 
            
    def full_board(self): #game over if snake takes the whole board
        if len(game.snake.elements_list)== NUM_COLS*NUM_ROWS:
            self.game_over()
            
    def self_collision(self): #game over if head collides with some other snake element
        for i in range(1,len(self.snake.elements_list)):
            if self.snake.elements_list[0].column == self.snake.elements_list[i].column and self.snake.elements_list[0].row == self.snake.elements_list[i].row:
                self.game_over()
                
    def wall_collision(self): #game over if head collides with the wall
        if 0 <= self.snake.elements_list[0].column < NUM_COLS and 0 <= self.snake.elements_list[0].row < NUM_ROWS:    
            global snake_alive
            snake_alive = True
        else: 
            snake_alive = False
            self.snake.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
            self.game_over()
        
    def game_over(self):
        self.snake.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
        global key_enabled
        key_enabled = False
        
        fill(0)
        textSize(30)
        text("Game Over", 230, 285)
        text("Final Score:" + str(self.score), 230, 315)
        # self.snake = Snake()
        
def mouseClicked():
    game.snake = Snake()
    global key_enabled
    key_enabled = True
    game.snake.key_handler[RIGHT] = True
    global snake_alive 
    snake_alive = True
    game.score = 0
    
    
def keyPressed():
    if key_enabled == True:
        game.snake.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
        if keyCode == UP and game.snake.elements_list[0].dir != DOWN:
            game.snake.key_handler[UP] = True
            
        elif keyCode == UP and game.snake.elements_list[0].dir == DOWN:
            game.snake.key_handler[DOWN] = True
            
        elif keyCode == DOWN and game.snake.elements_list[0].dir != UP:
            game.snake.key_handler[DOWN] = True
            
        elif keyCode == DOWN and game.snake.elements_list[0].dir == UP:
            game.snake.key_handler[UP] = True
        
        elif keyCode == RIGHT and game.snake.elements_list[0].dir != LEFT:
            game.snake.key_handler[RIGHT] = True
        
        elif keyCode == RIGHT and game.snake.elements_list[0].dir == LEFT:
            game.snake.key_handler[LEFT] = True
        
        elif keyCode == LEFT and game.snake.elements_list[0].dir != RIGHT:
            game.snake.key_handler[LEFT] = True
            
        elif keyCode == LEFT and game.snake.elements_list[0].dir == RIGHT:
            game.snake.key_handler[RIGHT] = True


game = Game()


            
