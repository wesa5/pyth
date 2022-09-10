fruits = ['apple', 'pear', 'orange']

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + "pie")


make_pie(4)
