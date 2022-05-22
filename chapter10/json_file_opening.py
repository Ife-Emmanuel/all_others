import json
def data_retriever(filename):
    filename = filename + '.json'
    with open(filename) as file_object:
        data_value = json.load(file_object)
    return data_value
