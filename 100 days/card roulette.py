import random

namesAsCVS = input("Give me everyones name, separated by a comma.")

name = namesAsCVS.split(", ")

num_of_people = len(name)
random_choice = (random.randint(0, num_of_people-1))
person_paying = name[random_choice]

print(f"{person_paying} is the person paying")

