'''from unicodedata import name


print('Hello world')

name1 = input('input your name  ')
name2 = input('input your name  ')

wes = name1 +  name2
print(wes)'''

'''fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")'''

#PRINTS THE HIGHEST SCORE 
'''student_scores = input("Input a list of students score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")'''

'''new = ""
for i in "Hello":
    if i != "l":
        new += i
print(new)'''

'''squares = list(map(lambda x: x**2, range(10)))
print(squares)

cube = []
for p in range(10):
    print(p, end=",")'''


#TUPLES
'''coms = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(coms)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs)'''

'''matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
        ]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

combs = [[row[i] for row in matrix] for i in range(4)]

print(combs)'''


#PRINTS THE AVERAGE HEIGHT OF A STUDENT
'''student_height = input("Input a list of students score: ").split()
for n in range(0, len(student_height)):
    student_height = int(student_height)
print(student_height)

total_height = 0
for height in student_height:
    total_height =+ height

number_of_students = 0
for student in student_height:
    number_of_students += 1

average_height =round (total_height/number_of_students)
print(average_height)'''

#ADDIND EVENS
'''total_numbers = 0
for total in range(2,101,2):
    print(total, end=",")
    total_numbers += total
print(f'\n{total_numbers}')

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        print(number, end=",")
        total2 += number
print(f'\n{total2}')'''

#FIZZBUZZ
'''for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Buzz")
    elif number % 5 == 0:
        print("Fizz")
    else:
        print(number)'''

#PASSWORD GENERATOR
'''import random
letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K',
        'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','@']

print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input("How many symbols would you like to have?\n"))
user_numbers = int(input("How many numbers would you like to have?\n"))


password = ""
for char in range(1, user_letters + 1):
    password += random.choice(letters)
for char in range(1, user_symbols + 1):
    password += random.choice(symbols)
for char in range(1, user_numbers +1):
    password += random.choice(numbers)

print(f"Here is your password: {password}")

#another way
password_list = []
for char in range(1, user_letters + 1):
    password_list += random.choice(letters)
for char in range(1, user_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, user_numbers +1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password =""
for char in password_list:
    password += char

print(f"Here is your password: {password}")'''

#SIMPLE FUNCTION
'''def greet():
    print("Hello there")
    print("How are you doing?")
    print("What's your name?")
greet()'''

#FUNCTION THAT ALLOWS INPUT
'''def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")
greet_with_name("Francis")'''

#A PAINT CALCULATOR
'''import math
def Paint_calculator(height, width, cover):
    area = height * width
    paint_needed = math.ceil(area/coverage)
    print(f"You'll need {paint_needed} cans of paint")

user_height = int(input("Height of wall: "))
user_width = int(input("width of wall: "))
coverage = 5

Paint_calculator(height= user_height, width=user_width, cover=coverage )'''

#PRIME NUMBER CHECKER
'''def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:   
        print("It's a prime number")
    else:
        print("It's not a prime number")
        
n = int(input("Check this number: "))

prime_checker(number=n)'''

#DICTIONARIES
'''programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "Apiece of code that you can call over and over again",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])'''

'''student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermonie": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)'''

#Dictionaries in lists
'''travel_log = [
    {
        "country": "France",
        "cities visited": ["Paris","Lille", "Dijon"],
        "visits": "12",
    },
    {
        "country": "Germany",
        "cities visited": ["Berlin","Hamburg", "Stuttgart"],
        "visits": "5",
    },
]

def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities visited"] = cities_visited
    new_country["visits"] = times_visited
    
    travel_log.append(new_country)

add_new_country(country_visited="Russia", cities_visited=["Moscow", "Saint Petersburg"], times_visited=2)

print(travel_log)'''

#Function with outputs
'''def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
print(format_name("WESa", "FraNcIS"))'''

#Days in A Month
'''def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_a_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if leap_year(year) and month == 2:
        return 29
    return month_days[month - 1]'''


year = int(input("Enter a Year: "))
month = int(input("Enter a month: "))
days = days_in_a_month(year, month)
print(days)

