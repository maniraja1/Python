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

#### Multiple ways to sort
#### Using lambda and row(n) works only with one column sorting
n = int(column_number)
sorted(rows, key=lambda row: row[n]) ### when you have a single column

##### Using lambda and row(n) works only with one column sorting
numbers=[1,2]
sorted(reader, key=lambda row: [row[n] for n in numbers])

##### This is the one from theexample above, works with any number of columns
sort=[1,2]
sorted(csv_reader, key=operator.itemgetter(*sort))


