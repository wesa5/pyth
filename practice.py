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




