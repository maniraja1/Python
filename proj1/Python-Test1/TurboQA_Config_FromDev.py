import json
from pathlib import Path
files = Path('/Users/mrajagopal/Documents/turbo-qa/Turbo-Configs-dev').rglob('*.json')
destination = Path('/Users/mrajagopal/Documents/turbo-qa/Turbo-Configs-dev2')
for file in files:
    newfilename = file.name.replace("dev","dev2").replace("s101", "s101")
    print(f"Old file: {file.name} - New file: {newfilename}")
    with open(file, mode='r') as read:
        rep = read.read()
        rep = rep.replace("dev1","dev2").replace("dev","dev2").replace("s101", "s101").replace("101","101")\
            .replace("sfmc1","sfmc").replace("azrdatatiersa2","azrdev2westus2sas101sa1")

        if "607_" in newfilename:
            print("607")
            rep = " \
{    \"TargetDBIsUp\": \"1\" " \
"}"
            with open(Path(destination, newfilename),mode='w', encoding="utf-8") as write:
                write.write(rep)

        if "610_" in newfilename:
            print("610")
            rep = ""

            with open(Path(destination, newfilename),mode='w', encoding="utf-8") as write:
                write.write(rep)

        if "610_" in newfilename:
            newfilename = newfilename.replace('610', '612')
            print(newfilename)
            with open(Path(destination, newfilename), mode='w', encoding="utf-8") as write:
                write.write(rep)

        if "612_" in newfilename:
            newfilename = newfilename.replace('612', '605')
            print(newfilename)
            with open(Path(destination, newfilename), mode='w', encoding="utf-8") as write:
                write.write(rep)

        if "AsyncAPIScaleS101D001" in newfilename:
            newfilename = newfilename.replace('AsyncAPIScaleS101D001', 'AsyncAPIScaleS101D003')
            print(newfilename)
            with open(Path(destination, newfilename), mode='w', encoding="utf-8") as write:
                if len(rep)>0:
                    write.write(rep)
                else:
                    write.write("")

        if "AsyncAPIScaleS101D002" in newfilename:
            newfilename = newfilename.replace('AsyncAPIScaleS101D002', 'AsyncAPIScaleS101D004')
            print(newfilename)
            with open(Path(destination, newfilename), mode='w', encoding="utf-8") as write:
                if len(rep)>0:
                    write.write(rep)
                else:
                    write.write(" ")

        if "ConfigMasterDB" in newfilename:
            newfilename = newfilename.replace('i3', 'i2')
            print(newfilename)
            with open(Path(destination, newfilename), mode='w', encoding="utf-8") as write:
                if len(rep)>0:
                    write.write(rep)
                else:
                    write.write(" ")









