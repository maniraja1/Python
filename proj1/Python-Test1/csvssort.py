import csv
import pandas
import operator

#### Exmaple with Pandas
# df=pandas.read_csv('./data/colors.csv',header='infer' )
# print(df.sort_values(by=['rank']))



def csvsort(filename,*args):
    with open(filename) as fileopen:
        csv_reader=csv.reader(fileopen)
        # Skip  first row
        header = next(csv_reader)
        sort=[]
        for a in args:
            sort.append(a)
        print(sort)
        # You need to unpack the list to be able to pass multiple column indices to the sorted method
        for rows in (sorted(csv_reader, key=operator.itemgetter(*sort))):
            print(f"{rows[0]} {rows[1]}")




csvsort ('./data/colors.csv',0,1)

