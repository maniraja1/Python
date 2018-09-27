
import csv


def csvreader(filename,args=[]):
        csv_reader=csv.DictReader(filename)
        line=0;
        valuelist=[]
        outdict={}
        for row in csv_reader:
            print(row)
            for key,value in row.items():
                print(key,value)
                print(f"Key:{key},value:{value}")
                if args and args[line]:
                    key = args[line]
                if key in outdict:
                    print(f"outdict:{outdict}")
                    valuelist=outdict[key]
                valuelist.append(value)
                print(f"Value list: {valuelist}")
                outdict[key] = valuelist
                valuelist=[]
            line += 1

        print(outdict)

csvreader(open('./data/data.csv'),['a','b','c'])


