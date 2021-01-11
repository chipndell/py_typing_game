import re

def parse_user_input(user_input, iterable_obj):
	'A helper method to map user input to predefined set of choice or returns None'
	for item in iterable_obj:
		match_string = re.search(user_input.upper(), item)
		if match_string:
			return match_string.string
