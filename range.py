from random import randrange

def number_random():
  (randrange(50, 80, 10) for index in range(4))

print(number_random())