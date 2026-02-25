"""
Python Basics Practice – With Comments & Simulated Output
Author: Brian Wycliff
Description: Beginner-friendly Python code demonstrating strings, lists,
loops, conditionals, dictionaries, tuples, arithmetic operations, and
more, with inline explanations and outputs.
"""

# ============================================================
# SECTION 1: STRING MANIPULATION
# ============================================================

name = 'daisy jackins'  # Assign string
print(name.title())  # Capitalizes first letter of each word
# Output: Daisy Jackins

_message = "i love you so much"
print(_message.upper())  # Converts string to uppercase
# Output: I LOVE YOU SO MUCH

car = 'BENZ'
print(car.lower())  # Converts string to lowercase
# Output: benz

first_name = 'daisy'
last_name = "jackins"
full_name = f'{first_name} {last_name}'  # Combine names using f-string
print(full_name.upper())
# Output: DAISY JACKINS

message = f"I am going to marry you {full_name}"  # Personalized message
print(message.upper())
# Output: I AM GOING TO MARRY YOU DAISY JACKINS

print("I\tam\ninterested\tin\nMercedes Benz")  # Tab & newline
# Output:
# I	am
# interested	in
# Mercedes Benz

print('\tcoding\n\tis\n\tfun')  # Tab & newline formatting
# Output:
# 	coding
# 	is
# 	fun

car = "    mercedes benz amg"
print('|' + car + '|')  # Show original string with spaces
# Output: |    mercedes benz amg|

print(car.lstrip().title())  # Remove leading spaces & capitalize
# Output: Mercedes Benz Amg

phone = 'google pixel 9     '
print(phone.rstrip())  # Remove trailing spaces
# Output: google pixel 9

money = '         US dollars     '
print(money.strip())  # Remove all leading & trailing spaces
# Output: US dollars
print("|" + money.strip() + "|")  # Show cleaned string
# Output: |US dollars|

super_car = 'BMW.concept'
print(super_car.removesuffix('.concept'))  # Remove suffix
# Output: BMW

travel = 'www.travel.emirates fly better.com'
print(travel.removeprefix("www.travel.").title())  # Remove prefix & capitalize
# Output: Emirates Fly Better.Com

# ============================================================
# SECTION 2: NUMBERS AND VARIABLES
# ============================================================

number = 2 + 8 * 5  # Multiplication first
print(number)
# Output: 42

num = 9 / 3
print(num)
# Output: 3.0

salary = 1_000_000  # Readable large number
print(salary)
# Output: 1000000

a, b, c = 1, 2, 3  # Multiple assignment
print(a, b, c)
# Output: 1 2 3

TRUTH = 'Jesus loves you'  # Constant by convention
print(TRUTH)
# Output: Jesus loves you

# ============================================================
# SECTION 3: LISTS AND OPERATIONS
# ============================================================

cars = ["Benz", "BMW", "AUDI"]
print(cars)
# Output: ['Benz', 'BMW', 'AUDI']

print('\n', cars[0].upper())  # First element uppercase
# Output:  BENZ
print(cars[-1])  # Last element
# Output: AUDI

fact = f"My dream car has always been a {cars[0].title()}"
print(fact)
# Output: My dream car has always been a Benz

# Modify elements
cars[0] = "Bentley"
cars[-1] = "Range Rover"
print(cars)
# Output: ['Bentley', 'BMW', 'Range Rover']

# Append & insert
cars.append("Chevrolet")
print(cars)
# Output: ['Bentley', 'BMW', 'Range Rover', 'Chevrolet']

cars.insert(2, 'GLE')
print(cars)
# Output: ['Bentley', 'BMW', 'GLE', 'Range Rover', 'Chevrolet']

# Delete & pop elements
del cars[-2]
print(cars)
# Output: ['Bentley', 'BMW', 'GLE', 'Chevrolet']

cars.pop()
print(cars)
# Output: ['Bentley', 'BMW', 'GLE']

new = f'I love the {cars.pop()} car'
print(new)
# Output: I love the GLE car

gifted = cars.pop(-1)
Say = f'I was gifted a {gifted.upper()} on my birthday'
print(Say)
# Output: I was gifted a BMW on my birthday

# ============================================================
# SECTION 4: LIST REMOVAL AND SORTING
# ============================================================

phones = ['Iphone', 'Samsung', 'Tecno', 'Huwai']
phones.pop(2)
print(phones)
# Output: ['Iphone', 'Samsung', 'Huwai']

phones.remove('Huwai')
print(phones)
# Output: ['Iphone', 'Samsung']

shoes = ['Nike','Jordan','Clarks','Timberland']
shoes.sort()
print(shoes)
# Output: ['Clarks', 'Jordan', 'Nike', 'Timberland']

shoes.sort(reverse=True)
print(shoes)
# Output: ['Timberland', 'Nike', 'Jordan', 'Clarks']

watches = ['Hublot','Ferari','Gemini','Axel']
print(sorted(watches))
# Output: ['Axel', 'Ferari', 'Gemini', 'Hublot']

watches.reverse()
print(watches)
# Output: ['Axel', 'Ferari', 'Gemini', 'Hublot']

print(len(watches))
# Output: 4

# ============================================================
# SECTION 5: LOOPS
# ============================================================

countries = ['UK','Denmark',"USA","France",'Belgium']
for cool in countries:
    print(cool)
# Output:
# UK
# Denmark
# USA
# France
# Belgium

for cool in countries:
    print(f'I love travelling to {cool.upper()}')
    print(f'I cant wait to go to {cool.title()} again\n')
# Output:
# I love travelling to UK
# I cant wait to go to Uk again
# ... (similar for other countries)

# ============================================================
# SECTION 6: RANGE AND NUMBER LISTS
# ============================================================

for value in range(1,15,2):
    print(value)
# Output: 1 3 5 7 9 11 13

# Squares using loop
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Cubes using list comprehension
cubes = [value**3 for value in range(5)]
print(cubes)
# Output: [0, 1, 8, 27, 64]

# ============================================================
# SECTION 7: CONDITIONALS
# ============================================================

Pizza = 'Beef'
if Pizza == 'Beef':
    print('No thanks')
# Output: No thanks

if Pizza != 'Chicken':
    print('Gimme that')
# Output: Gimme that

number = 21
if number >= 20:
    print(True)
# Output: True

# ============================================================
# SECTION 8: DICTIONARIES
# ============================================================

Alien = {'color':'Blue','points':100}
print(Alien['color'])
# Output: Blue

Alien['color'] = 'yellow'
print(f"The alien is now {Alien['color']}")
# Output: The alien is now yellow

Alien['x position'] = 10
Alien['y position'] = 20
print(Alien)
# Output: {'color': 'yellow', 'points': 100, 'x position': 10, 'y position': 20}

# Empty dictionary example
Benz = {}
Benz['AMG'] = 10
Benz['GLE'] = 20
print(Benz)
# Output: {'AMG': 10, 'GLE': 20}

print("Program completed successfully.")
# Output: Program completed successfully.