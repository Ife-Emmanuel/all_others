with open('firstpractice.txt') as file_object:
    file_content = file_object.read()
    #print(file_content)
    words = file_content.split()
for word in range(len(words)//10):
    portion = words[:10]
    with open('arranged.txt', 'a') as file_object:
        arranged = ' '.join(portion)
        file_object.write(arranged +  '\n')
    remaining = set(words) - set(portion)
    words = list(remaining)
