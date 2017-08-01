from random import randint

class Die():
    """Represent a dice generating random numbers."""

    def __init__(self, sides=6):
        """Initialize attributes of die."""
        self.sides = sides

    def roll_die(self):
        """Roll the die to get a random number."""
        print('The result of rolling a {} sided die 10 times.'.format(self.sides))
        for i in range(10):
            print('{} '.format(randint(1,self.sides)),end='  ')
        print('\n')
big_die = Die(20)
big_die.roll_die()

small_die = Die(10)
small_die.roll_die()

