# import json
# def get_stored_username():
#     filename = 'my_username.json'
#     try:
#         with open(filename) as file_object:
#             username = json.load(file_object)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

from collections import Counter
player_details = [('Balikis', ['medium', 1, 'easy', 1]), ('solomon', ['medium', 0]), ('femi', ['easy', 3]), ('subomi', ['easy', 4]), ('favour', ['medium', 0, 'easy', 1]), ('kashamu', ['easy', 2])]
new = Counter(player_details)
print(new)