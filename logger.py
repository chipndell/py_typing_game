import time

class User_Log:
	'''
	A class defining user's session in the typing_test game
	along with the methods providing vital information regarding their game session.
	'''


	def __init__(self):
		'''attempt and correct holds for counter for reposeses.
		Where as log dict is used for username, start_time and end_time stamps.
		'''
		self.log = {}
		self.attempt = 0
		self.correct = 0

	def correct_response(self):
		'for each correct response adds 1 to the current value'
		self.correct += 1
		return self.correct

	def attempt_response(self):
		'for each response adds 1 to the current value'
		self.attempt += 1
		return self.attempt

	def get_username(self, username):
		'updates the username'
		self.log.update({'username': username})

	def accuracy(self):
		'returns the accuracy of the typing out of 100'
		return self.correct/self.attempt * 100

	def score(self):
		'returns score in, a out of b format'
		print(f"{self.correct} correct responses out of {self.attempt}")

	def time_played(self):
		'returns time played by player in '
		return self.log['end_time'] - self.log['start_time']

	def quit(self):
		'returns the message indicating quitting the game'
		print("Please come back again and have fun meanwhile!!")

	def restart(self):
		'returns the restarting message'
		print('restarting')
		self.log.update({'start_time':time.time()})
		self.attempt = 0
		self.correct = 0

	def speed(self):
		'Returns the typing speed in letter per minute format'
		time_played = self.time_played()
		print('You have played with {:.0f} correct Letters per Minute!! Keep it Up.'.format(60 * self.correct / time_played))