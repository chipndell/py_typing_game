import time
import sys

from logger import User_Log
from helper import parse_user_input

level_selection_choice = ['BEGINNER', 'MEDIUM', 'ADVANCE',]
game_choice = ['RESTART', 'QUIT',]


def initialize_gamesession():
	'this function receives the vital info. before starting game. and returns user_Log object'
	print('''
		Type 'restart' to restart game,
		'quit' to quit game.
	''')

	user_log = User_Log()

	name = input("Please enter your name:")
	print(f"Welcome {name}!")
	user_log.get_username(name)

	print("""Choose the difficulty level:
		Advance
		Medium
		Beginner
		""")

	level_selection_input = input("Please select the difficulty level:")
	level_selection = parse_user_input(level_selection_input, level_selection_choice)

	while level_selection is None:
		print("Please provide valid entry for selection.")
		level_selection_input = input("Please select the difficulty level:")
		level_selection = parse_user_input(level_selection_input, level_selection_choice)
	else:
		user_log.log.update({'dificulty_level': level_selection.upper()})
		print(f"{name}, You have selected {level_selection} level.")
		user_log.log.update({'start_time':time.time()})
	return user_log


def play_game(user_log):
	'this func takes the User_Log object as arguement and runs game making changes as needed.'
	dificulty_level = user_log.log['dificulty_level']
	while dificulty_level is not None:	
		letter = user_log.get_letters(dificulty_level)
		sys.stdout.write(letter)
		input_str = input('\n>')
		if len(input_str) < 2 and input_str == letter:
			user_log.correct_response()
			user_log.attempt_response()
		elif len(input_str) == 1 and input_str != letter:
			user_log.attempt_response()
		elif parse_user_input(input_str, game_choice) == 'QUIT':
			user_log.reset_session(quit=True)
			break
		elif parse_user_input(input_str, game_choice) == 'RESTART':
			user_log.reset_session(message="Restarting")
		else:
			user_log.attempt_response()
