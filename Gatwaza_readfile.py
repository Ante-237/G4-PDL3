# import required module
import random

# get message from positive vibes


class PositiveMessage:

    def __init__(self):
        pass

    @staticmethod
    def read_positive_vibes():
        with open("PositiveVibes.txt", "r", encoding='utf-8') as file:
            data = file.readlines()
            print("\t\t---------------------------------------------")
            print("\t\t", random.choice(data))
            print("\t\t---------------------------------------------")
