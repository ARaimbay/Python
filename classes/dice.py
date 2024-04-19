class Die:
    def __int__(self, sides=6):
        self.sides=sides
    def roll_die(self):
        from random import randint
        randint(1,10)

my_die = Die()
my_die.roll_die()
