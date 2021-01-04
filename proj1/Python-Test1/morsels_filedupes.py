import hashlib,os
from collections import defaultdict
from pathlib import Path

def filehash(*args,min_size=0):
    block_size = 2**14
    hashes = defaultdict(list)
    files = []
    for items in args:
        if os.path.isdir(items):
            for x in (Path(items).rglob("*.*")):
                if os.path.getsize(x)>min_size:
                    files.append(x)
        else:
            if os.path.getsize(items):
                files.append(items)

    for file in files:
        file_hash = hashlib.md5()
        print(f"Processing file: {file}")
        with open(file, mode='r') as f:
            while True:
                data = f.read(block_size)
                if not data:
                    break
                file_hash.update(data.encode('utf-8'))

        hashes[file_hash.hexdigest()].append(file)
    i=1
    for key, value, in hashes.items():
        if len(value)> 1:
            print(f"Duplicate Group {i}:")
            for x in value:
                print(x)
            i += 1
            print()
    if i ==1:
        print("No Duplicate Files found")



if not os.getcwd() == '/Users/mrajagopal/Documents':
    os.chdir("../../../../")
#filehash("Configure_Turbo.ps1", "AADAdmin.ps1", "Configure_Turbo.ps1", "AADAdmincopy.ps1")
#filehash("Configure_Turbo.ps1","AADAdmin.ps1")
filehash("Configure_Turbo.ps1","AADAdmin.ps1",'/Users/mrajagopal/Documents/manitest/Code', min_size=6)
'''
x = filehash("Configure_Turbo.ps1")
y = filehash("AADAdmin.ps1")

print(x==y)
'''
