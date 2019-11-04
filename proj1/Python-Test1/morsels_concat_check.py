import sys
from tokenize import tokenize, STRING, NUMBER, NL



filenames=['data/concat_file1']
for name in filenames:
    with open(name, mode='rb') as f:
        prev = None
        for token in tokenize(f.readline):
            #print(token)
            if prev and token.type == prev.type == STRING:
                print(f"{name}, line {token.start[0]}: implicit concatenation")
                print(f"{prev.string} + {token.string}")
            if token.type != NL:
                prev = token
