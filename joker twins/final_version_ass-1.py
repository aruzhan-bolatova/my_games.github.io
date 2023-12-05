# GLOBAL VARIABLES
PLAYERS_NUM = 2
ROW_NUM = 5
COLUMN_NUM = 5
CELL_NUM = ROW_NUM * COLUMN_NUM
letters_pair = CELL_NUM / 2

import random
import os
import time

column_letters_list = []
for coordinate_letter in range(COLUMN_NUM):
	column_letters_list.append(chr(65+coordinate_letter))
#print(column_letters_list)

row_numbers_list = []
for coordinate_number in range(ROW_NUM):
	row_numbers_list.append(chr(49+coordinate_number))
#print(row_numbers_list)


# CONSTRUCTING A HIDDEN LIST WITH RANDOM ASSIGNMENT OF LETTERS

# FIRST, HIDDEN LIST IS CREATED WITH EMPTY VALUES ACCORDING TO GLOBAL VALUES OF ROW AND COLUMN NUMS
hidden_list = []
for rows in range(int(ROW_NUM)):
	row_list = []
	for columns in range(int(COLUMN_NUM)):
		row_list.append(' ')
	hidden_list.append(row_list)

# SECOND, CONSTRUCTING A HIDDEN LIST WITH RANDOM ASSIGNMENT OF LETTERS DEPENDING ON EVEN/ODD CELL NUMBER 
	# IF EVEN CELL NUM: 
		# CREATES ALPHABET LIST OF UPPER AND LOWER CASES IN RANGE OF LETTER PAIR'S NUMBER
		# CHANGES THE LAST LETTER PAIR TO * 
		# RANDOMLY SHUFFLES THE ALPHABET LIST
		# PUTS THE VALUE FROM SHUFFLED ALPHABET INTO HIDDEN LIST ONE BY ONE
if CELL_NUM % 2 == 0: 
	alphabetUpperLowerCase = []
	for letter in range(int(letters_pair)):
		alphabetUpperLowerCase.append(chr(65 + letter))
		alphabetUpperLowerCase.append(chr(97 + letter))
	alphabetUpperLowerCase[-1] = '*'
	alphabetUpperLowerCase[-2] = '*'
	random.shuffle(alphabetUpperLowerCase)
	for index_row in range(ROW_NUM):
		for index_column in range(COLUMN_NUM):
			hidden_list[index_row][index_column] = alphabetUpperLowerCase[0]
			alphabetUpperLowerCase.pop(0)
	# iF ODD CELL NUM:
		# CREATES ALPHABET LIST OF UPPER AND LOWER CASES IN RANGE OF LETTER PAIR'S NUMBER
		# RANDOMLY SHUFFLES THE ALPHABET LIST
		# RANDOMLY DECIDES THE POSITION OF JOKER AND INSERTS INTO SHUFFLED ALPHABET LIST
		# PUTS THE VALUE FROM SHUFFLED ALPHABET LIST INTO HIDDEN LIST ONE BY ONE
else:
	alphabetUpperLowerCase = []
	for letter in range(int(letters_pair)):
		alphabetUpperLowerCase.append(chr(65 + letter))
		alphabetUpperLowerCase.append(chr(97 + letter))
	alphabetUpperLowerCase[-1] = '*'
	alphabetUpperLowerCase[-2] = '*'
	random.shuffle(alphabetUpperLowerCase)
	joker_1_position = random.randint(0,CELL_NUM-1)
	alphabetUpperLowerCase.insert(joker_1_position, '*')

	for index_row in range(ROW_NUM):
		for index_column in range(COLUMN_NUM):
			hidden_list[index_row][index_column] = alphabetUpperLowerCase[0]
			alphabetUpperLowerCase.pop(0)
	#print(hidden_list)

# PLAYERS' NAMES INPUT
player_1 = input("First player's name: ")
player_2 = input("Second player's name: ")

# DISPLAYING THE SCORE (VARIABLES ARE USED TO BE OVERWRITTEN WHEN TWINS ARE FOUND)
score_player_1 = 0
score_player_2 = 0
print(player_1 + "'s", 'score:' + str(score_player_1))
print(player_2 + "'s", 'score:' + str(score_player_2))

# A BOARD'S 2D LIST DEPENDING ON GLOBAL VARIABLE VALUE (# IN IT)
		# BOARD LIST IS JUST FOR THE VISUAL REPRESENTATION OF TABLE
board = []
for rows in range(ROW_NUM):
	row_list = []
	for columns in range(COLUMN_NUM):
		row_list.append('#')
	board.append(row_list)
# print(board)   #CAN INDICATE THIS BOARD AS GLOBAL?


# PRINTING THE 2D LIST BOARD SO IT DISPLAYS AND USER REFERENCES TO IT 
for column in range(COLUMN_NUM):
	print('   ' + column_letters_list[column], end='')
print("\n +" + "---+" * COLUMN_NUM)

for row in range(ROW_NUM):
	print(row_numbers_list[row] + '| ' , end='')
	for column in range(COLUMN_NUM):
		print(board[row][column] + ' | ', end='')
	print("\n +" + "---+" * COLUMN_NUM)


# VARIABLE FOR CHECKING THE END OF THE GAME, IF THIS VARIABLE == 0 THE WHILE LOOP BREAKS
the_game_ends = CELL_NUM

# RANDOMIZER ASSIGNS THE TURNS 
turn = random.randint(1, PLAYERS_NUM)
score_player_1 = 0
score_player_2 = 0

# THE MAIN GAME EXECUTION PART WHICH RUNS UNTIL THERE ARE NO CARDS LEFT ON BOARD
while the_game_ends != 0:

	currently_open_card_row_coordinate = ROW_NUM+1 #I want these variables to be 0/None, I did not use 0 because A1 cell gives [0][0] index
	card_currently_open_column_index = COLUMN_NUM+1

		# n is for every guess by one player in one round
	for n in range(2):
		if turn == 1:
			print(player_1, end=": ")
			coordinate = input("Enter a coordinate (e.g. A3):")

		else:
			print(player_2, end=": ")
			coordinate = input("Enter a coordinate (e.g. A3):")

		    # CHECKING IF THE INPUT COORDINATE IS VALID 

		# while len(coordinate) != 2:
		# 	coordinate = input("Enter a valid coordinate: ")

		# while True:
		# 	if 65 <= ord(coordinate[0]) < 65+COLUMN_NUM:
		# 		if 49 <= ord(coordinate[1]) < 49+ROW_NUM:
		# 			break
		# 	coordinate = input("Enter a valid coordinate (uppercase column letter and row number): ")


		# while True:
		# 	index_row = row_numbers_list.index(coordinate[1])
		# 	index_column = column_letters_list.index(coordinate[0])
		# 	if board[index_row][index_column] != " ":
		# 		break
		# 	coordinate = input("This cell is empty. Enter a valid coordinate: ")

		# while currently_open_card_row_coordinate == index_row and card_currently_open_column_index == index_column:
		# 	coordinate = input("This card is currently open. Enter a valid coordinate: ")



			# CHECKING IF THE INPUT COORDINATE IS VALID 

		while True:
			if len(coordinate) == 2:
				if 65 <= ord(coordinate[0]) < 65+COLUMN_NUM:
					if 49 <= ord(coordinate[1]) < 49+ROW_NUM:
						index_row = row_numbers_list.index(coordinate[1])
						index_column = column_letters_list.index(coordinate[0])
						# print(index_row , index_column)
						if board[index_row][index_column] != " ":
							if currently_open_card_row_coordinate != index_row or card_currently_open_column_index != index_column:
								# value = True
								break
							else: 
								coordinate = input("This card is currently open. Enter a valid coordinate: ")
						else:
							coordinate = input("This cell is empty. Enter a valid coordinate: ")
					else: 
						coordinate = input("Enter a valid coordinate (valid uppercase column letter and row number): ")
				else: 
					coordinate = input("Enter a valid coordinate (valid uppercase column letter and row number): ")
			else: 
				coordinate = input("Enter a valid coordinate: ")

			# IF 1st GUESS, OPEN THAT CARD
		if n == 0:
			currently_open_card_row_coordinate = row_numbers_list.index(coordinate[1])
			card_currently_open_column_index = column_letters_list.index(coordinate[0])
			# print(currently_open_card_row_coordinate, card_currently_open_column_index)

			row_number_index_1 = row_numbers_list.index(coordinate[1])
			column_letter_index_1 = column_letters_list.index(coordinate[0])

			# print(row_number_index_1, end=' ')
			# print(column_letter_index_1)

			# TEMPORARY BOARD IS COPIED FROM BOARD IN ORDER NOT ALTER THE BOARD PERMANENTLY WHEN TURNING THE CARD OVER AFTER EACH GUESS
			temporary_board = []
			for r in range(ROW_NUM):
				temporary_board_inner = []
				for c in range(COLUMN_NUM):
					temporary_board_inner.append(board[r][c])
				temporary_board.append(temporary_board_inner)
			temporary_board[row_number_index_1][column_letter_index_1] = hidden_list[row_number_index_1][column_letter_index_1]

			# PRINTING THE TEMPORARY BOARD(VISUAL REPRESENTATION)
			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(temporary_board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)

			#IF 2nd GUESS (IN THE SAME ROUND), KEEP 1st CARD OPEN AND OPEN ONE MOR
		else:
			row_number_index_2 = row_numbers_list.index(coordinate[1])
			column_letter_index_2 = column_letters_list.index(coordinate[0])

			# print(row_number_index_2, end=' ')
			# print(column_letter_index_2)

			temporary_board[row_number_index_2][column_letter_index_2] = hidden_list[row_number_index_2][column_letter_index_2]

			# PRINTING THE TEMPORARY BOARD(VISUAL REPRESENTATION)
			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(temporary_board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)


		# CHECKING 2 CARDS 
	checking_if_twins = abs(ord(hidden_list[row_number_index_1][column_letter_index_1]) - ord(hidden_list[row_number_index_2][column_letter_index_2]))
		
		# CARDS ARE TWINS IF THE DIFFERENCE IN ASCII TABLE VALUES EQUALS 32 OR BOTH CARDS ARE *
	if checking_if_twins == 32 or hidden_list[row_number_index_1][column_letter_index_1] == hidden_list[row_number_index_2][column_letter_index_2]:
		board[row_number_index_1][column_letter_index_1] = " "
		board[row_number_index_2][column_letter_index_2] = " "

		if turn == 1:
			score_player_1 = score_player_1 + 1
			# print(score_player_1)
		else:
			score_player_2 = score_player_2 + 1
			# print(score_player_2)

		time.sleep(2)
		os.system("clear")

		print(player_1 + "'s", 'score:' + str(score_player_1))
		print(player_2 + "'s", 'score:' + str(score_player_2))


		for column in range(COLUMN_NUM):
			print('   ' + column_letters_list[column], end='')
		print("\n +" + "---+" * COLUMN_NUM)

		for row in range(ROW_NUM):
			print(row_numbers_list[row] + '| ' , end='')
			for column in range(COLUMN_NUM):
				print(board[row][column] + ' | ', end='')
			print("\n +" + "---+" * COLUMN_NUM)

		the_game_ends = the_game_ends - 2
	
		# IF THE 1st GUESS IS * AND 2nd IS LETTER, FIND THE TWIN OF THE LETTER AND REMOVE ALL 3 (2 POINTS)
	elif hidden_list[row_number_index_1][column_letter_index_1] == "*":
		letter_ord = ord(hidden_list[row_number_index_2][column_letter_index_2])
		if 65 <= letter_ord <= 90:
			# for row in hidden_list:
			# 	for item in row:
			# 		if item == chr(ord(letter) + 32):
			# 			second_twin_index_1 = row[0] 
			# 			second_twin_index_2 = item[0]

			for r in range(ROW_NUM):
				for c in range(COLUMN_NUM):
					if hidden_list[r][c] == chr(letter_ord + 32):
						second_twin_index_1 = r 
						second_twin_index_2 = c
			board[second_twin_index_1][second_twin_index_2] = chr(letter_ord + 32)

			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)

			time.sleep(2)
			os.system("clear")

		else:
			for r in range(ROW_NUM):
				for c in range(COLUMN_NUM):
					if hidden_list[r][c] == chr(letter_ord - 32):
						second_twin_index_1 = r 
						second_twin_index_2 = c
			board[second_twin_index_1][second_twin_index_2] = chr(letter_ord - 32)

			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)

			time.sleep(2)
			os.system("clear")

			# second_twin = hidden_list.index(chr(ord(letter) - 22))
		board[row_number_index_1][column_letter_index_1] = " "
		board[row_number_index_2][column_letter_index_2] = " "
		board[second_twin_index_1][second_twin_index_2] = " "


		if turn == 1:
			score_player_1 = score_player_1 + 2
			# print(score_player_1)
		else:
			score_player_2 = score_player_2 + 2
			# print(score_player_2)

		print(player_1 + "'s", 'score:' + str(score_player_1))
		print(player_2 + "'s", 'score:' + str(score_player_2))

		for column in range(COLUMN_NUM):
			print('   ' + column_letters_list[column], end='')
		print("\n +" + "---+" * COLUMN_NUM)

		for row in range(ROW_NUM):
			print(row_numbers_list[row] + '| ' , end='')
			for column in range(COLUMN_NUM):
				print(board[row][column] + ' | ', end='')
			print("\n +" + "---+" * COLUMN_NUM)

		the_game_ends = the_game_ends - 3

		# IF THE 2nd GUESS IS * AND 1st IS LETTER, FIND THE TWIN OF THE LETTER AND REMOVE ALL 3 (2 POINTS)
	elif hidden_list[row_number_index_2][column_letter_index_2] == "*":
		letter_ord = ord(hidden_list[row_number_index_1][column_letter_index_1])
		if 65 <= letter_ord <= 90:
			for r in range(ROW_NUM):
				for c in range(COLUMN_NUM):
					if hidden_list[r][c] == chr(letter_ord + 32):
						second_twin_index_1 = r 
						second_twin_index_2 = c
			board[second_twin_index_1][second_twin_index_2] = chr(letter_ord + 32)

			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)

			time.sleep(2)
			os.system("clear")

		else:
			for r in range(ROW_NUM):
				for c in range(COLUMN_NUM):
					if hidden_list[r][c] == chr(letter_ord - 32):
						second_twin_index_1 = r 
						second_twin_index_2 = c
			board[second_twin_index_1][second_twin_index_2] = chr(letter_ord - 32)

			for column in range(COLUMN_NUM):
				print('   ' + column_letters_list[column], end='')
			print("\n +" + "---+" * COLUMN_NUM)

			for row in range(ROW_NUM):
				print(row_numbers_list[row] + '| ' , end='')
				for column in range(COLUMN_NUM):
					print(board[row][column] + ' | ', end='')
				print("\n +" + "---+" * COLUMN_NUM)

			time.sleep(2)
			os.system("clear")

		board[row_number_index_1][column_letter_index_1] = " "
		board[row_number_index_2][column_letter_index_2] = " "
		board[second_twin_index_1][second_twin_index_2] = " "

		if turn == 1:
			score_player_1 = score_player_1 + 2
			# print(score_player_1)
		else:
			score_player_2 = score_player_2 + 2
			# print(score_player_2)

		print(player_1 + "'s", 'score:' + str(score_player_1))
		print(player_2 + "'s", 'score:' + str(score_player_2))

		for column in range(COLUMN_NUM):
			print('   ' + column_letters_list[column], end='')
		print("\n +" + "---+" * COLUMN_NUM)

		for row in range(ROW_NUM):
			print(row_numbers_list[row] + '| ' , end='')
			for column in range(COLUMN_NUM):
				print(board[row][column] + ' | ', end='')
			print("\n +" + "---+" * COLUMN_NUM)

		the_game_ends = the_game_ends - 3

		# IF 2 GUESSES ARE NOT TWINS OR *, CLOSE THE CARDS AND CONTINUE WITH SECOND PLAYER
	else:

		time.sleep(2)
		os.system("clear")

		for column in range(COLUMN_NUM):
			print('   ' + column_letters_list[column], end='')
		print("\n +" + "---+" * COLUMN_NUM)

		for row in range(ROW_NUM):
			print(row_numbers_list[row] + '| ' , end='')
			for column in range(COLUMN_NUM):
				print(board[row][column] + ' | ', end='')
			print("\n +" + "---+" * COLUMN_NUM)

		print(player_1 + "'s", 'score:' + str(score_player_1))
		print(player_2 + "'s", 'score:' + str(score_player_2))

		turn = (turn+1) % PLAYERS_NUM

		#WINNER IDENTIFICATION
if score_player_1 > score_player_2: 
	print("Congratulations!", player_1, "has won the game!")
else:
	print("Congratulations!", player_2, "has won the game!")
