# import required module
import random

# get message from positive vibes


class PositiveMessage:

    def __init__(self):
        pass

    @staticmethod
    def read_positive_vibes(self):
        with open("PositiveVibes.txt", "r", encoding='utf-8') as file:
            data = file.readline()
            print("\t\t---------------------------------------------")
            print(random.choice(data))
            print("\t\t---------------------------------------------")
