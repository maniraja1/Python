import csv
import sys

update = True
updatedreviews = []
sort=True
[filename1, filename2] = ['data/all-restaurants.csv','data/2016-food.csv']


def get_restaurant_id(restaurant_file):
    return {
        (name,street, city, state): [name, price, street, city, state, comments]
        for name, price, street, city, state, comments in csv.reader(restaurant_file)
    }


with open(filename1) as current_file:
    current_reviews = get_restaurant_id(current_file)

with open(filename2) as new_file:
    new_reviews = get_restaurant_id(new_file)

for key,value in new_reviews.items():
    print(key)
    if key in current_reviews and update and value[-1].strip() != '' and key != ('Name', 'Street', 'City', 'State'):
        updatedreviews.append(key)
        current_reviews[key] = value

new_names = [n for n in new_reviews if n not in current_reviews]
for name in new_names:
    current_reviews[name] = new_reviews[name]

for x in sorted(current_reviews):
    if x != ('Name', 'Street', 'City', 'State'):
        print(current_reviews[x])

with open(filename1, mode='wt', newline='') as current_file:
    writer = csv.writer(current_file)
    if sort:
        writer.writerow(('Name', 'Price', 'Street', 'City', 'State', 'Comments'))
        for x in sorted(current_reviews):
            if x != ('Name', 'Street', 'City', 'State'):
                writer.writerow(current_reviews[x])
    else:
        writer.writerows(current_reviews.values())

print(f'Added {len(new_names)} new row(s)')
print(f'Updated {len(updatedreviews)} new row(s)')
print(updatedreviews)


