import time
import random
import sys

from logger import User_Log


print('''
	Type 'restart' to restart game,
	'quit' to quit game.
''')

name = input("Please enter your name:")
user_log = User_Log()
user_log.log.update({'start_time':time.time()})
user_log.get_username(name)

while True:
	
	a = random.randint(65,122)
	sys.stdout.writelines(chr(a))
	b = str(input('\n>'))

	if len(b) < 2 and a == ord(b):
		user_log.correct_response()
	elif b.lower() == 'quit':
		user_log.log.update({'end_time':time.time()})
		user_log.score()
		user_log.speed()
		user_log.quit()
		break
	elif b.lower() == 'restart':
		user_log.log.update({'end_time':time.time()})
		user_log.score()
		user_log.speed()
		user_log.restart()
	else:
		pass
	user_log.attempt_response()

