import re


def parse_user_input(user_input, iterable_obj):
    """This func assigns choice selection by matching character patters or calls verify_user_input function"""
    user_selection_list = []
    for item in iterable_obj:
        match_obj = re.match('^' + user_input.upper(), item)
        if match_obj is not None:
            user_selection_list.append(match_obj.string)
    if len(user_selection_list) == 1:
        print(">>>You selected : {}".format(user_selection_list[0]))
        return user_selection_list[0]
    elif len(user_selection_list) == 0:
        ask_again = input(">>>Please enter valid response from {}.\n$".format(iterable_obj))
        return match_user_input(ask_again, iterable_obj)
    elif len(user_selection_list) > 1:
        ask_again = input(">>>Which one do you mean {}? Please provide valid response.\n$".format(user_selection_list))
        return match_user_input(ask_again, iterable_obj)


def pause_game(user_log_obj, iterable_obj):
    total_time = user_log_obj.log['end_time'] - user_log_obj.log['start_time']
    user_log_obj.log['total_time'] += total_time
