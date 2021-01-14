import datetime
import random


class User_Log:
	"""
	A class defining user's session in the typing_test game
	along with the methods providing vital information regarding their game session.
	"""
	def __init__(self):
		"""
		Attributes like attempt and correct works as counter for responses.
		Where as log dict is used for username, start_time and end_time stamps.
		"""
		self.log = {}
		self.attempt = 0
		self.correct = 0
		self.pause = False
		self.log['total_time'] = datetime.timedelta()

	def correct_response(self):
		"""correct Attribute of the instance is incremented by 1"""
		self.correct += 1
		return self.correct

	def attempt_response(self):
		"""attempt Attribute of the instance is incremented by 1"""
		self.attempt += 1
		return self.attempt

	def get_username(self, username):
		"""updates the username"""
		self.log.update({'username': username})
		return 'username updated'

	def reset_session(self, message=None, quit=False, reset_counters=True, start_timestamp=False):
		"""This method manages scenarios like quit, restart, pause, resume action of game.
		Argument like message (str) : Prints the message on terminal
		quit (boolean) : makes sure Whether we wont to quit game or not
		reset_counters (boolean) : Makes sure needed parameter are resetted.
		start_timestamp (boolean): Makes sure that start_time is updated."""
		self.log.update({'end_time': datetime.datetime.utcnow()})
		time_played = self.log['end_time'] - self.log['start_time']
		print(f"{self.correct} correct responses out of {self.attempt}")
		print('You have played with {:.0f} correct Letters per Minute!! Keep it Up.'.format(
			60 * self.correct / time_played.total_seconds()))
		if message:
			print(message)
		if reset_counters:
			self.attempt = 0
			self.correct = 0
		if start_timestamp:
			self.log.update({'start_time': datetime.datetime.utcnow()})
		if quit:
			print("Please come back again and have fun meanwhile!!")

	def accuracy(self):
		"""returns the accuracy of the typing out of 100"""
		return self.correct / self.attempt * 100

	def get_letters(self, difficulty_level):
		"""for different difficulty level selected returns the letter"""
		if difficulty_level == 'ADVANCE':
			return chr(random.randint(33, 126))
		elif difficulty_level == 'MEDIUM':
			return chr(random.randint(65, 126))
		else:
			return chr(random.randint(97, 122))
