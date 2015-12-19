import random
import time
import sys

class Dice:

    representations=(
        'none',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six'
    )

    def __init__(self):
        self.status=1

    def __str__(self):
        return self.representations[self.status]

    def roll(self):
        self.countdown()
        self.status=random.randint(1,6)
        return self.status

    def countdown(self):
        count=3
        while count > 0:
            print 'extraction starts in %s seconds' % count
            time.sleep(1)
            count-=1


if __name__ == '__main__':

    dice1 = Dice()
    dice2 = Dice()

    while True:
        dice1.roll()
        dice2.roll()
        if dice1.status == dice2.status:
            print dice1.status,dice2.status
            print 'same number'
            break

        print dice1,dice2