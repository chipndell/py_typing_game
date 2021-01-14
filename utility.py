import datetime

from helper import match_user_input, pause_game
from logger import User_Log

level_selection_choice = ['BEGINNER', 'MEDIUM', 'ADVANCE', ]
game_choice = ['RESTART', 'QUIT', 'PAUSE', 'RESUME', ]


def initialize_gamesession():
    """this function receives the vital info. before starting game. and returns user_Log object"""
    print('''
		Type 'restart' to restart game,
		'quit' to quit game,
		'pause' to pause the game and
		'resume' to resume the game
	''')

    user_log = User_Log()

    name = input(">>>Please enter your name:\n$")
    print(f">>>Welcome {name}!\n")
    user_log.get_username(name)

    print(""">>>Choose the difficulty level:
		Advance
		Medium
		Beginner
		""")

    level_selection_input = input(">>>Please select the difficulty level:\n$")
    level_selection = match_user_input(level_selection_input, level_selection_choice)
    user_log.log.update({'difficulty_level': level_selection})
    user_log.log.update({'start_time': datetime.datetime.utcnow()})
    return user_log


def play_game(user_log):
    """this func. takes the User_Log object as arguement and runs game."""
    difficulty_level = user_log.log['difficulty_level']
    while True:
        letter = user_log.get_letters(difficulty_level)
        print(">>>", letter)
        input_str = input('$')
        if len(input_str) == 1 and input_str == letter:
            user_log.correct_response()
            user_log.attempt_response()
        elif len(input_str) == 1 and input_str != letter:
            user_log.attempt_response()
        elif len(input_str) > 1:
            user_action = match_user_input(input_str, game_choice)
            if user_action == "QUIT":
                user_log.reset_session(quit=True)
                break
            elif user_action == 'RESTART':
                user_log.reset_session(message="Restarting")
            elif user_action == 'PAUSE':
                user_log.reset_session(message="Game is Paused", start_timestamp=True, reset_counters=False)
                pause_game(user_log, game_choice)
                user_log.pause = True
            elif user_action == "RESUME" and user_log.pause == True:
                print(">>>Game has resumed.")
                user_log.log.update({'start_time': datetime.datetime.utcnow()})
