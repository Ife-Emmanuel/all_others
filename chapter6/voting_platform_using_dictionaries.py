##################################################################
##################################################################
##YOU STILL HAVE TO READ ON DATA STRUCTURES ON THE SAVED ON OPERAMINI
### IN YOUR PHONE
### ALSO...COMPLETE THE VOTING PLATFORM AND FIND BETTER MEANS TO SOLVE
### WHILE HAVING COMPLETED OTHER TOPICS
###################################################################
#######################################################################
voters_list = []
name = input('Enter your name: ')
print('Hi %s, you are welcome to the voting portal\nPlease ensure you vote'
      'wisely and for the candidate of your choice.' %name)
print('INSTRUCTION: Please enter the index of the candidate you want to vote for.\n'
      'Thankyou.')
voters_list.append(name)
a = president_vote = []
b = social_director_vote = []
c = Treasurer_vote = []
pres_candidates = ['Olakunle Abass','Adebayo Taiwo','Osobi David']
social_candidates = ['Kesington Oluwatoba','Abass Kehinde','Oseni Quadri']
treas_candidates = ['Okanlawon Paul','Balogun Taiwo','Ileri Simon']

if voters_list:
    for name in voters_list:
        print('Hi ' + name + '. Welcome to the       school\'s '
         'voting platform.\nEnter the number beside each '
         'candidates to vote for them.')
        print('President')
        print('1. ' + pres_candidates[0] + '\n2. ' + pres_candidates[1] + '\n3. ' + pres_candidates[2])
        president = int(input('::'))
        president_vote.append(president)

        print('Social Director')
        print('1. ' + social_candidates[0] + '\n2. ' + social_candidates[1] + '\n3. ' + social_candidates[2])
        social_director = int(input('::'))
        social_director_vote.append(social_director)

        print('Treasurer')
        print('1. ' + Treasurer_vote[0] + '\n2. ' + Treasurer_vote[1] + '\n3. ' + Treasurer_vote[2])
        Treasurer = int(input('::'))
        Treasurer_vote.append(Treasurer)

post_vote_lists = [a, b, c]
from collections import Counter

def result_determiner(post_vote):
    first_third = Counter(post_vote).most_common(3)
    first_position = first_third[0]
    second_position = first_third[1]
    third_position = first_third[2]

    firstpole_count = first_position[1]
    secondpole_count = first_position[1]
    thirdpole_count = first_position[1]

    if first_position == 1

result_dict = {'president':()}

if post_vote_lists:
    for post_vote in post_vote_lists:






