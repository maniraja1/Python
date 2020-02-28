import os
i =0
for root, dire, files in os.walk('/Users/mrajagopal/Documents/git-zarga/ZargaEndpoint/Code'):
    print(files)
    i += 1
    if i >0:
        break


print(next(os.walk('/Users/mrajagopal/Documents/git-zarga/ZargaEndpoint/Code'))[2])