"""Using my usermade json-module to store and retrieve
users data"""
import json_data_retrieval
import random
import decorator_function
#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.

players_details = {}
active = True
while active:
    profile = []     #for appending the level(easy/medium/legend) used for the round of a game.
    json_data_retrieval.welcome_user()
        while True:
            try:
                response = int(input())

            # except ValueError:
            #     pass
            except Exception:
                print('make sure you read clearly the information and '
                      'input your response again')
                response = int(input())
            else:
                if response == 1:
                    username = input('Enter the new player\'s name. : ') ## Emmanuel, note here that you wrote username instead of name which is probably correct too
                    json_file_data_storage.data_storage('username', username.title()) ## Read comment written above.
                    print('Welcome ' + username.title() + '. Your name will be remembered when next you log in.')
                    break
                elif response == 2:
                    break
    well = True
    while well:

        response_2 = input('Start game now ? (1/2) : ')# Initial question
        print('\n===============================================================================\n')

        # Now for the game: A number guess game.
        if response_2 == '1':
            #If response to initial question is 1, game will play.

            total_guesses = []   #total guesses is the list of all user's guesses both valid and invalid.
            valid_guesses = []  # Valid guesses is the list of user's guess that end up being thesame as the computer correct guess.

            decorator_function.game_prompt()  # Imported decorated function to prompt player of GAME START
            print('\nChoose difficulty level : ')
            status = True
            print('Enter "1" for easy, "2" for medium and "3" for legend : ')
            while status:
                try:
                    level_option = int(input())
                except ValueError:
                    status = True
                else:
                    if level_option == 1:
                        list_number = 2
                        level = 'easy'
                    elif level_option == 2:
                        list_number = 3
                        level = 'medium'
                    elif level_option == 3:
                        list_number = 4
                        level = 'legend'
                    profile.append(level)
                    status = False

            print('\nWhenever you want to quit, please enter "0".\n')
            good = True
            while good:
                another_good = True #Flag that determines whether the just following loop runs unstop
                # due to user innocent error of entering number less than potential number options of a level option
                while another_good:
                    try:
                        entered_number = int(input('Enter a number : '))
                        if entered_number == 0:
                            break
                        condition_1 = level_option == 1 and entered_number < 2
                        condition_2 = level_option == 2 and entered_number < 3
                        condition_3 = level_option == 3 and entered_number < 4
                        if condition_1 :
                            print('Enter a number that is equal or more than 2!')
                            continue
                        elif condition_2:
                            print('Enter a number that is equal or more than 3! ')
                            continue
                        elif condition_3:
                            print('Enter a number that is equal or more than 4! ')
                            continue

                    except ValueError:
                        print('Enter numbers not letters! ')

                    else:
                        number_list = [(i + 1) for i in range(entered_number)]
                        listing = random.sample(number_list, list_number) #number_list is the iteratable list of elements in range of list_number.
                        another_good = False  #False flag to stop the loop once there is
                        #no user innocent error of entering number less than potential number options of each option

                print(username.title() + ', you will have ' + str(list_number) + ' numbers! '
                                'from 1 to ' + str(entered_number))
                print('Here is the list of numbers. >>>>Guess the one golden number.')
                for number in listing:
                    print(number)
                random.shuffle(listing)
                correct_guess = listing[1] # Correct guess is the guess produced by the computer upon using the random.shuffle() function
                status_here = True
                while status_here:
                    try:
                        user_guess = int(input('Enter your guess : '))
                    except ValueError:
                        print('Enter a number not letter')
                        continue
                    else:
                        if user_guess == 0:
                            end_response = input('Are you sure you want to stop this game? If yes press "1", else press "2".')
                            if end_response == 1:
                                good = False
                            elif end_response == 2:
                                good = True
                        total_guesses.append(user_guess)
                        if len(total_guesses) == 5:
                            good = False

                        if user_guess == correct_guess:
                            print('Wow! you got it.')
                            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                            valid_guesses.append(user_guess)
                        else:
                            print('oops you missed it.\n'
                                  'You can play again.')
                            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
                        status_here = False

            valid_score = len(valid_guesses)
            profile.append(valid_score)
            total_score = len(total_guesses)
            players_details[username] = profile
            print(username.title() + ' Your score in Guess game is ' + str(valid_score) +
                  ' out of ' + str(total_score) + ' attempted guesses.')

            #Another question for a user who has just finished playing.

            question_status = True
            while question_status:
                response_3 = input('Do you want to play again : ')
                if response_3 == '1':
                    well = True
                    question_status = False
                elif response_3 == '2':
                    well = False
                    question_status = False
                else:
                    question_status = True

        #Action if user says no to initial question
        elif response_2 == '2':
            continue
        elif response_2 == '0':
            well = False
        else:
            print('Enter a valid number (1 or 2)')
            continue

    #Asking question if user wants to finally quit game
    response_4 = (input('Quit Game ? : '))
    if response_4 == '1':
        active = False
    elif response_4 == '2':
        active = True

##GAME CONCLUSION
print('\n=====================================================================')
print(username.title() + ', You have successfully closed Guess Game!!!')
print('=====================================================================\n')

print('==========================================================')
print(players_details + '\n')
players_details = list(players_details.items()) #Converting the dictionary into a list

print('=================================================================')
print(players_details)
#list_number of top three scorers
print('\n==========================================================================')
ranked_players = sorted(players_details, reverse=True, key=lambda player: player[1][1])
first_three = ranked_players[: 3]
decorator_function.top_winners() # Imported decorated function of top three players
print('Below are the top three scorers : ')
print('{:<12}{:<12}{:<12}{:<12}'.format('S/N', 'Player', 'Level', 'Score'))
for i, (player, (level, score)) in enumerate(first_three):
    print('{:<12}{:<12}{:<12}{:<12}\n'.format(str(i + 1) + '.', player.title(), level, score))
print('=====================================================================\n')

## If we were to rank the all the players.

ranked_players = sorted(players_details, reverse=True, key=lambda x : x[1][len(x[1])-1])
print('\nBelow is the rank of all ' + str(len(players_details)) +  ' : \n')
print('{:<12}{:<12}{:<12}{:<12}'.format('S/N', 'Player', 'Level', 'Score'))
for i, (player, (level, score)) in enumerate(ranked_players):
    print('{:<12}{:<12}{:<12}{:<12}\n'.format(str(i + 1) + '.', player.title(), level, score))
print('=======================================================================')