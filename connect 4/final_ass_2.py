import random, os, time

# GLOBAL VARIABLES
COLUMN_NUM = 7
ROW_NUM = 6
CELL_NUM = COLUMN_NUM * ROW_NUM
PLAYERS_NUM = 2

# ASSIGNING PLAYERS WITH CHECKERS (KEY = turn/player?)
checkers_dictionary = {0: "X", 1: "O", 2: "V", 3: "H", 4: "M"} 

# COLUMN LETTERS which depends on the COLUMN_NUM, so is printed with board and can be referenced
column_letters_list = []
for coordinate_letter in range(COLUMN_NUM):
	column_letters_list.append(chr(65+coordinate_letter))

# CREATING THE 2D LIST BOARD 
board = []
for rows in range(ROW_NUM):
	row_list = []
	for columns in range(COLUMN_NUM):
		row_list.append(' ')
	board.append(row_list)

#FUNCTION FOR PRINTING THE 2D LIST BOARD (SO IT DISPLAYS AND USER CAN REFERENCE TO IT)
def board_print():
	for column in range(COLUMN_NUM):
		print('   ' + column_letters_list[column], end='')
	print("\n +" + "---+" * COLUMN_NUM)

	for row in range(ROW_NUM):
		print(' | ', end='')
		for column in range(COLUMN_NUM):
			print(board[row][column] + ' | ', end='')
		print("\n +" + "---+" * COLUMN_NUM)

#FUNCTION FOR ASKING THE USER (COLUMN) INPUT AND CHECKING IF THE INPUT IS VALID 
def player(checker):
	print("Player", checker, end= "" )
	user_input = input(", please enter a column: ")

	while True:
		if len(user_input) == 1:
			if 65 <= ord(user_input) < 65+COLUMN_NUM:
				break
			else:
				user_input = input("Enter a valid coordinate (within the range of the board): ")
		else:
			user_input = input("Enter a valid coordinate: ")
	return user_input

#FUNCTION FOR PLACING THE CHECKERS INTO THE LOWEST POSSIBLE ROW IN THE COLIMN CHOSEN
def placinig_checker(player):
	for r in range(ROW_NUM-1, -1, -1):
		if board[r][column_letters_list.index(column_input)] == " ":
			board[r][column_letters_list.index(column_input)]= checkers_dictionary[player]
			board_print()
			break
		else:
			continue		

#FUNCTIONS CHECKING FOR THE CONNECT 4 AFTER EACH TURN: (if one is true, then run = False and game stops)

	#FUNCTION FOR CHECKING IF THE VERTICAL CONNECT IS REACHED 
def checking_vertical_connect(checker_key):
	for row in range(ROW_NUM-3):
		for column in range(COLUMN_NUM):
			if board[row][column] == checkers_dictionary[checker_key] and board[row+1][column] == checkers_dictionary[checker_key] and board[row+2][column] == checkers_dictionary[checker_key] and board[row+3][column] == checkers_dictionary[checker_key]:
				print("Player" , checkers_dictionary[checker_key], "has won!")
				return False
	return True

	#FUNCTION FOR CHECKING IF THE HORIZONTAL CONNECT IS REACHED 
def checking_horizontal_connect(checker_key):
	for row in range(ROW_NUM):
		for column in range(COLUMN_NUM-3):
			if board[row][column] == checkers_dictionary[checker_key] and board[row][column+1] == checkers_dictionary[checker_key] and board[row][column+2] == checkers_dictionary[checker_key] and board[row][column+3] == checkers_dictionary[checker_key]:
				print("Player" , checkers_dictionary[checker_key], "has won!")
				return False
	return True

	#FUNCTION FOR CHECKING IF THE DIAGONAL (POSITIVE SLOPE) CONNECT IS REACHED 
def checking_diagonal_positive_connect(checker_key): 	#to the right and up
	for row in range(3, ROW_NUM):
		for column in range(COLUMN_NUM-3):
			if board[row][column] == checkers_dictionary[checker_key] and board[row-1][column+1] == checkers_dictionary[checker_key] and board[row-2][column+2] == checkers_dictionary[checker_key] and board[row-3][column+3] == checkers_dictionary[checker_key]:
				print("Player" , checkers_dictionary[checker_key], "has won!")
				return False
	return True

	#FUNCTION FOR CHECKING IF THE DIAGONAL (NEGATIVE SLOPE) CONNECT IS REACHED 
def checking_diagonal_negative_connect(checker_key):	 # to the right and bottom
	for row in range(ROW_NUM-3):
		for column in range(COLUMN_NUM-3):
			if board[row][column] == checkers_dictionary[checker_key] and board[row+1][column+1] == checkers_dictionary[checker_key] and board[row+2][column+2] == checkers_dictionary[checker_key] and board[row+3][column+3] == checkers_dictionary[checker_key]:
				print("Player" , checkers_dictionary[checker_key], "has won!")
				return False
	return True

#FUNCTION FOR CHECKING IF THE GAME IS DRAW
def checking_draw():
	draw = 0
	for row in range(ROW_NUM):
		for column in range(COLUMN_NUM):
			if board[row][column] != " ":
				draw += 1
				if draw == CELL_NUM:
					print("The game is a DRAW, no winner!")
					return False
	return True
#INITIAL PRINT OF THE BOARD
board_print()	

# RANDOMIZER ASSIGNS THE FIRST PLAYER
turn = random.randint(0, PLAYERS_NUM-1)

#EXECUTION OF THE GAME (GAME ENDS WHEN RUN=FALSE DETERMINED BY FUNCTIONS THAT CHECK CONNECT 4 OR WHEN THE GAME IS DRAW)
run = True
while run:
	if turn == 0:
		column_input = player(checkers_dictionary[0])
		placinig_checker(0)

		if checking_vertical_connect(0) == False:
			break
		elif checking_horizontal_connect(0) == False:
			break
		elif checking_diagonal_positive_connect(0) == False:
			break
		elif checking_diagonal_negative_connect(0) == False:
			break
		elif checking_draw() == False:
			break
		else:
			run = True

		turn = (turn+1) % PLAYERS_NUM #for alternating between players

	elif turn == 1:
		column_input = player(checkers_dictionary[1])
		placinig_checker(1)
		
		if checking_vertical_connect(1) == False:
			break
		elif checking_horizontal_connect(1) == False:
			break
		elif checking_diagonal_positive_connect(1) == False:
			break
		elif checking_diagonal_negative_connect(1) == False:
			break
		elif checking_draw() == False:
			break
		else:
			run = True

		turn = (turn+1) % PLAYERS_NUM

	elif turn == 2:
		column_input = player(checkers_dictionary[2])
		placinig_checker(2)
		
		if checking_vertical_connect(2) == False:
			break
		elif checking_horizontal_connect(2) == False:
			break
		elif checking_diagonal_positive_connect(2) == False:
			break
		elif checking_diagonal_negative_connect(2) == False:
			break
		elif checking_draw() == False:
			break
		else:
			run = True

		turn = (turn+1) % PLAYERS_NUM

	elif turn == 3:
		column_input = player(checkers_dictionary[3])
		placinig_checker(3)

		if checking_vertical_connect(3) == False:
			break
		elif checking_horizontal_connect(3) == False:
			break
		elif checking_diagonal_positive_connect(3) == False:
			break
		elif checking_diagonal_negative_connect(3) == False:
			break
		elif checking_draw() == False:
			break
		else:
			run = True

		turn = (turn+1) % PLAYERS_NUM

	elif turn == 4:
		column_input = player(checkers_dictionary[4])
		placinig_checker(4)

		if checking_vertical_connect(4) == False:
			break
		elif checking_horizontal_connect(4) == False:
			break
		elif checking_diagonal_positive_connect(4) == False:
			break
		elif checking_diagonal_negative_connect(4) == False:
			break
		elif checking_draw() == False:
			break
		else:
			run = True
			
		turn = (turn+1) % PLAYERS_NUM









