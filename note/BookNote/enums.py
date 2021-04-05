from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9

    kitten = 1
    puppy = 2


Animal = namedtuple("Animal", "name, age, type")
perry = Animal(name="Preey", age=31, type=Species.cat)
print(perry)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
print(charlie.type)
print(Species(1))
print(Species["cat"])
print(Species.cat)
print(dir())
my_list = [1, 2, 3]
print(dir(my_list))



try:
    file = open("test.txt", "rb")
except IOError as e:
    print("An IOError occured!")
    # raise e

my_dict = {"name": "yasoob", "age": "undefined"}
print(my_dict)

from pprint import pprint

pprint(my_dict)