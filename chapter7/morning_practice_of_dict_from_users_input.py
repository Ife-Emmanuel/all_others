favourite_languages = {}
#print(favourite_languages)
Active = True
while Active:
    name = input('What is your name : ')
    language = input('Enter your favourite ' +
                     'programming language : ')
    favourite_languages[ name ] = language
    if len(favourite_languages) == 3:
        Active = False

print('The list of attendees and their ' +
      'favourite programmming language')
for index, (name, language) in enumerate(favourite_languages.items()):
    print(str(index + 1) + '. ' + name.title() + '  ::  ' + language)

print(favourite_languages)
#print('The maximum polled language is ' + max(favourite_languages.values(),)
print(list(favourite_languages.values()))
print('The most frequent langauage is ' + max(list(favourite_languages.values()), key= list(favourite_languages.values()).count))
import statistics
print('The most used language is ' + statistics.mode(favourite_languages.values()) )

from collections import Counter
res = Counter(favourite_languages.values())
print(res)
for language, count in res.items():
    print(language + ' :: ' + str(count))

