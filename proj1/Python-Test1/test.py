import csv, operator

restaurants=set()
restaurants2 = set()
updated=0
inserted=0

print(STRING)

with open("data/all-restaurants.csv") as fileopen:
    csv_reader = csv.reader(fileopen)
    header = next(csv_reader)
    print(header)
    for line in csv_reader:
        restaurants.add((line[0], line[2], line[3], line[4]))



with open("data/2016-food.csv") as outer_fileopen, open("data/all-restaurants.csv") as original, open('data/all-restaurants_new.csv','w') as final:
    reader = csv.DictReader(outer_fileopen, fieldnames=header)
    reader2 = csv.DictReader(original, fieldnames=header)
    writer = csv.DictWriter(final, fieldnames=header)
    next(reader)
    next(reader2)
    writer.writeheader()
    for line in reader:
        if (line['Name'], line['Street'], line['City'], line['State']) in restaurants:
            if (line['Comments']) != '':
                writer.writerow({'Name': line['Name'], 'Price': line['Price'], 'Street': line['Street'], 'City': line['City'], 'State': line['State'], 'Comments': line['Comments']})
                restaurants2.add((line['Name'], line['Street'], line['City'], line['State']))
                inserted += 1
        else:
            writer.writerow(
                {'Name': line['Name'], 'Price': line['Price'], 'Street': line['Street'], 'City': line['City'],
                 'State': line['State'], 'Comments': line['Comments']})
            inserted += 1
    for line2 in reader2:
        if (line2['Name'], line2['Street'], line2['City'], line2['State']) in restaurants2:
            updated += 1
            inserted = inserted-1
            pass
        else:
            writer.writerow(
                {'Name': line2['Name'], 'Price': line2['Price'], 'Street': line2['Street'], 'City': line2['City'], 'State': line2['State'],
                 'Comments': line2['Comments']})

with open('data/all-restaurants_new.csv', 'r') as read, open('data/all-restaurants_final.csv', 'w') as write:
    data2 = csv.DictReader(read, fieldnames=header)
    next(data2)
    sortedCSV = sorted(data2, key=operator.itemgetter("Name"))
    writer = csv.DictWriter(write, fieldnames=header)
    writer.writeheader()
    writer.writerows(sortedCSV)


print(f"Inserted Rows: {inserted}")
print(f"Updated Rows: {updated}")