'''
Concept
    This is an assignment operator typically used when dealing with
    generators,
    assigning and evaluating expensive expression
    reducing lines of code where you evaluate an expression and later use the same expression inside if or while loop


'''

if (match := 2) > 1:
    print(match)

a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

sample_data = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True}
]

print("With Python 3.8 Walrus Operator:")
for entry in sample_data:
    if name := entry.get("name"):
        print(f'Found name: "{name}"') 