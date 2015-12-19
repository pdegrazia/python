"""
This is a simulation of scrap
PLayer throws two dice, if total is 2,3,or 12, player looses
If total is 7 or 11, player wins
If total is any other number, players keep on rolling the dice
if the same number is thrown again, then player wins,
if a 7 is rolled, then player loses
"""
import random


class Die:

    representation = [
     '***\n***\n***\n',
     '\n*\n',
     '\n*\n*\n',
     '\n*\n*\n*\n',
     '\n* *\n* *\n',
     '\n* *\n * \n* *\n',
     '\n* *\n* *\n* *\n'
    ]

    def __init__(self):
        self.generator = random.Random()
        self.value = 1

    def __str__(self):
        return Die.representation[self.value]

    def roll(self):
        self.value = self.generator.randint(1,6)
        return self.value

if __name__ == '__main__':

    first_dice = Die()
    second_dice = Die()
    print first_dice, second_dice

    total = first_dice.roll() + second_dice.roll()
    print first_dice, second_dice

    if total == 7 or total == 11:
        print 'win! you rolled %s ' % total
    elif total == 2 or total == 3 or total == 12:
        print 'loose..you rolled %s ' % total
    else:
        while True:
            print 'try to match %s ' % total
            throw = first_dice.roll() + second_dice.roll()
            print first_dice,second_dice
            if throw == 7: print 'loose...you rolled 7';break
            elif throw == total: print 'win! you rolled %s again!' % throw;break

            print 'nothing done...roll again!'
