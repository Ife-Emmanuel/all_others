
#players_details = {'tolu' : ['easy', 23],  'bola' : ['medium', 32],  'femi' : ['easy', 2],  'lanre' : ['legend', 22] }
#players_details = list(players_details.items())
#
# players_details = [('Kamil', [1, 3]), ('kemi', [2]), ('adebayo', [2, 1]), ('funke', [3]), ('emmanuel', [3]), ('sina', [3])]
# #print(players_details[1][1])
# a = map(lambda x : x[1][len(x[1])-1], players_details)

a = {'femi' : ['medium', 2], 'kayode' : ['easy', 3], 'sola' : ['legend', 8], 'femi' : ['easy', 2]}
print(a)
a['femi'] = ['easy', 3]
print('=================================================1')
print(a)
a.update({'kayode' : ['medium', 10]})
print('==============================================2')
print(a)



# print('\n' + str(players_details) + '\n')
# #players_details = sorted(players_details, reverse= True, key= lambda player : player[1][1])
# print('================')
# print('\nBelow are the rank of all ' + str(len(players_details)) +  ' : ')
# print(players_details)
#
#
# # print(players_details.items())
# # print('\n' + str(list(players_details.items())[0]))
# # a = (2, 3, 3, 4, 5, 7, 9)
#
# #list_number of top three scorers
# ranked_players = sorted(players_details, reverse=True, key=lambda player: player[1][1])
# first_three = ranked_players[: 3]
# print('Below are the top three scorers : ')
# print('{:<12}{:<12}{:<12}{:<12}'.format('S/N', 'Player', 'Level', 'Score'))
# for i, (player, (level, score)) in enumerate(first_three):
#     print('{:<12}{:<12}{:<12}{:<12}\n'.format(str(i + 1) + '.', player.title(), level, score))
#


