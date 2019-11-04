text = """\
object,property,value
ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none"""




class CondenseCSV:

    def condense(self,text,object):
        dd = {}
        columns = [object]
        objects = []
        for line in text.split('\n')[1:]:
            obj = line.split(",")[0]
            col = line.split(",")[1]
            val = line.split(",")[2]
            key = obj + ":" + col
            dd[key] = val

        for key, value in dd.items():
            keyname = key.split(":")[1]
            objectname = key.split(":")[0]
            if keyname not in columns:
                columns.append(keyname)
            if objectname not in objects:
                objects.append(objectname)

        print(*columns)
        for o in objects:
            outstr = o + ", "
            for c in columns:
                keyname = o + ":" + c
                value = (dd.get(keyname))
                if value != None:
                    outstr += value + ", "
            print(outstr)

    def __init__(self,text,id_name='object'):
        self.condense(text,id_name)

from collections import defaultdict
def condense_csv(csv_text, id_name):
    groups = defaultdict(dict)
    for line in csv_text.splitlines():
        identifier, attribute, value = line.split(',')
        groups[identifier][attribute] = value
    headers = [id_name, *groups[identifier].keys()]
    rows = [
        [id_, *attributes.values()]
        for id_, attributes in groups.items()
    ]
    return "\n".join(
        ",".join(row)
        for row in [headers, *rows]
    )

from io import StringIO
import csv
def condense_csv2(csv_text, id_name):
    groups = {}
    csv_reader = csv.reader(StringIO(csv_text))
    for identifier, attribute, value in csv_reader:
        if identifier not in groups:
            groups[identifier] = {id_name: identifier}
        groups[identifier][attribute] = value
    out_file = StringIO()
    writer = csv.writer(out_file)
    writer.writerow(groups[identifier].keys())
    writer.writerows(
        attributes.values()
        for attributes in groups.values()
    )
    print(groups)
    for attributes in groups.values():
        print(*attributes.keys())
    return out_file.getvalue()

from io import StringIO
import csv
def condense_csv3(csv_text, id_name):
    groups = {}
    csv_reader = csv.reader(StringIO(csv_text))
    for identifier, attribute, value in csv_reader:
        if identifier not in groups:
            groups[identifier] = {id_name: identifier}
        groups[identifier][attribute] = value
    rows = list(groups.values())
    out_file = StringIO()
    writer = csv.DictWriter(out_file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
    return out_file.getvalue()

print(condense_csv(text,'shape'))
print(condense_csv2(text,'shape'))
#print(condense_csv3(text,'shape'))
#CondenseCSV(text,'shape')



'''
This exercise is more focused towards dictionary manipulation. 
The common pattern in the functions above is we have a dictionary within dictionary and that's what we use to map 
key value pairs
Defaultdict creates identifier, key=value and if the identifier and key already exists then it updates. 
If you dont use default dict then you have to create the key if it does not exist and append when the key exists
Also wen reading csv line you can map x,y,z=line.split(",")

'''
