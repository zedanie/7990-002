import random

my_seed = float(input('Throw dice by entering a number between 1 and 10: '))
your_bet = input('Bet Big(B) or Small(S): ')

random.seed(my_seed)
a1 = random.randint(1,6)
a2 = random.randint(1,6)
print(f'Dice 1 is {a1}')
print(f'Dice 2 is {a2}')

if a1+a2 >=7 and your_bet == 'B':
    print('You win! It is Big!')
elif a1+a2 < 7 and your_bet == 'S':
    print('You win! It is Small!')
else:
    print('You lost the game!')
