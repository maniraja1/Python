import json
def processfile(filename):
    with open(filename,mode='r') as read_file:
        data = json.load(read_file)
        return data

def writefile(filename):
    data={
            'name': 'John',
            'shares': 100,
            'price': 1230.23
        }
    with open(filename,mode='w') as filename:
        json.dump(data, filename, indent=4)