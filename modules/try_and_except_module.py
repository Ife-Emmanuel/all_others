def try_except_func(data_name, data_value, else_content= None):
    """Now customizing the try and except block here for json_file_
        loading and dumping.   data_name(string_form), data_value(args)"""
    import json_data_retrieval
    import json_file_data_storage

    try:
        data_value = json_data_retrieval.data_retriever(data_name)
    except:
        json_file_data_storage.data_storage(data_name, data_value)
        print('Hello ' + data_name + ' has not been entered.\n'
                     'It will be remembered the next you enter.\n')
    else:
        print(data_name + ' :: ' + str(data_value) + '\n')

data_dictionary = {'username': 'kolawole', 'english_score': 22, 'math_score': 32}
for data_name, data_value in data_dictionary.items():
    try_except_func(data_name, data_value)