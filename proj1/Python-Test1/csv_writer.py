import csv
import pandas


def writecsv_noheader():
    with open('./data/datawrite.csv', mode='w') as csvfile:
        csvwriter=csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['firstname', 'lastname'])
        csvwriter.writerow(['John', 'smith'])
        csvwriter.writerow(['Jane', 'Doe'])

def writecsv_header():
    with open('./data/datawrite2.csv', mode='w') as csvfile:
        fieldname=['firstname', 'lastname']
        csvwriter=csv.DictWriter(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldname)
        csvwriter.writeheader()
        csvwriter.writerow({'firstname': 'John', 'lastname': 'smith'})
        csvwriter.writerow({'firstname':'Jane', 'lastname':'Doe'})

writecsv_noheader()
writecsv_header()


df=pandas.read_csv('./data/data.csv')
print(df)

df=pandas.read_csv('./data/data.csv',index_col='h1')
print(df)


df=pandas.read_csv('./data/data.csv', index_col='h1')
df.to_csv('./data/datawrite3.csv')

