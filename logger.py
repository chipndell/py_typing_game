import time
import random

class User_Log:
	'''
	A class defining user's session in the typing_test game
	along with the methods providing vital information regarding their game session.
	'''


	def __init__(self):
		'''Attributes like attempt and correct works as counter for reposeses.
		Where as log dict is used for username, start_time and end_time stamps.
		'''
		self.log = {}
		self.attempt = 0
		self.correct = 0

	def correct_response(self):
		'correct Attribute of the instance is incremented by 1'
		self.correct += 1
		return self.correct

	def attempt_response(self):
		'attempt Attribute of the instance is incremented by 1'
		self.attempt += 1
		return self.attempt

	def get_username(self, username):
		'updates the username'
		self.log.update({'username': username})
		return 'username updated'


	def reset_session(self, message=None, quit=False):
		'returns score in, a out of b format'
		self.log.update({'end_time':time.time()})		
		time_played = self.log['end_time'] - self.log['start_time']
		print(f"{self.correct} correct responses out of {self.attempt}")
		print('You have played with {:.0f} correct Letters per Minute!! Keep it Up.'.format(60 * self.correct / time_played))
		if message:
			print(message)
		self.log.update({'start_time':time.time()})
		self.attempt = 0
		self.correct = 0
		if quit:
			print("Please come back again and have fun meanwhile!!")
	
	def accuracy(self):
		'returns the accuracy of the typing out of 100'
		return self.correct/self.attempt * 100


	def get_letters(self, dificulty_level):
		'for diffivult  level selected returns the letter'
		if dificulty_level == 'ADVANCE':
			return chr(random.randint(33,126))
		elif dificulty_level == 'MEDIUM':
			return chr(random.randint(65,126))
		else:
			return chr(random.randint(97,122))
