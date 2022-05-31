import random

test_seed = int(input('create your a number: '))
random.seed(test_seed)

random_side = random.randint(0,1)

if random_side == 0:
    print('Heads')
else:
    print('Tails')