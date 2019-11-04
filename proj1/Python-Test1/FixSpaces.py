import os
destdir = "/Users/mrajagopal/Documents/ConfigMasterDB/Rollback Scripts"
filename = [f for f in os.listdir(destdir)]
for i in filename:
        if os.path.isfile(os.path.join(destdir,i)) and i != '.DS_Store':
            orig = i
            new = i.replace("-", "").replace(",", "").replace(" ","_").replace("__", "_").replace(".ps1","_Rollback.ps1")
            print(orig, new)
            os.rename(os.path.join(destdir,orig),os.path.join(destdir,new))

filename = [f for f in os.listdir(destdir)]
for i in filename:
    print(i)