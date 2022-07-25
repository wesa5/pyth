#for i in range(2, 10, 2):
 #   print(i, end=" ")

"""word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")"""

'''for i in range(97, 123):
print("{}".format(chr(i)), end="")'''

'''def my_function(counter=89):
    return counter + 1

print(my_function())'''

#__import__("sys").stdout.write("#pythoniscool\n")

'''def my_function(counter=89):
    print("Counter: {}".format(counter))

my_function(12)'''

'''a = "Python is cool"
print(a[7:-5])'''

'''a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
print(a.get('friends')[-1].get("name"))'''

'''a = [1, 2, 3, 4]
a[2] = 10
print(a)'''

'''a = 12
if a > 2:
    if a % 2 == 0:
        print("Tech")
    else:
        print("C is fun")
else:
    print("School")'''

'''print("{:d} Mission street, {}".format(972, "San Francisco"))'''


'''class Person:
    pass  # An empty block

p = Person()
print(p)'''

'''def my_function(counter=89):
     return counter + 1
 
print(my_function())'''

'''for i in range(2, 10, 2):
    print(i, end=" ")'''


'''class Person:
    def say_hi(self):
        print('Hello, how are you?')

Person().say_hi()'''

'''class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Initializing {self.name}")
        Robot.population += 1
    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} working")
    def say_hi(self):
        print(f"Greetings my Masters call me {self.name}")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

droid1.die()
droid2.die()

Robot.how_many()'''

'''class User:
     id = 89
     name = "no name"
     __password = None
     
     def __init__(self, new_name=None):
         self.is_new = True
         if new_name is not None:
             self.name = new_name
 
u = User()
print(u.name)'''

'''def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list'''

'''class User:
    id = 1


u =User()
u.id = 89
User.id = 98
print(u.id)'''

'''a = [1, 2, 3, ]
id(a)
"""139926795932424"""

a = a + [4]
print(id(a))'''

'''class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)'''

#Card ROULETTE PRACTICE
'''import random

names = input("Give me everyones name, separated by a coma: ")

person_paying = names.split(",")

# number_of_people = len(person_paying)
# random_choice = random.randint(0, number_of_people - 1)
# payer = person_paying[random_choice]
payer = random.choice(person_paying)
print(f"{payer} is the peron paying")'''

#HEADS OR TAILS PRACTICE
'''import random

number_selected = input("create a number: ")

random_choice = random.randint(0,1)

if random_choice == 0:
    print("Heads")
else:
    print("Tails")'''

