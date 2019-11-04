import sys
from time import sleep
def fancy_input(question,validatior,error_message="Invalid arguments"):
    validresponse=False
    while not validresponse:
        request = input(f"{question}:  ")
        try:
            request_response = validatior(request)
            validresponse=True
        except Exception:
            print(f"\n{error_message}\n")

    return request_response

''' python morsels 
'''
def fancy_input2(question,validatior,error_message="Invalid arguments"):
    validresponse=False
    while not validresponse:
        request = input(f"{question}:  ")
        try:
            request_response = validatior(request)
            validresponse=True
        except Exception:
            sys.stderr.write(f"\n{error_message}\n")
    return request_response



def fancy_input3(question,validatior,error_message="Invalid arguments"):
    validresponse=False
    while not validresponse:
        request = input(f"{question}:  ")
        try:
            request_response = validatior(request)
            validresponse=True
        except Exception:
            print(f"\n{error_message}\n",file=sys.stderr)
            sleep(1)
    return request_response

def booleanprompt(question,default=False):
    question=question+"? [y/n]: "
    request=input(question)

    if request.lower() == 'y' or request.lower()=='yes':
        return True
    elif request.lower() == 'n' or request.lower()=='no':
        return False
    elif request is None:
        return default
    else:
        return default



'''
response = fancy_input3("What is your favorite number?", int)
print(response)
'''
response = booleanprompt("Do you like Python")
print(response)
'''
def parse_number(string):
    return int(string.replace(',', ''))

n = fancy_input("What is your favorite number?", parse_number)
print("Neat!", n, "is a nice number")
'''