import random

class ReadAll:

    # A function that displays the SecretVibes title
    def __init__(self):
        pass

    @staticmethod
    def read_title(self):
        print(" This is the Secrete Vibes Room ")
    # A function that reads a file and returns each line of the file#

    @staticmethod
    def read_choice():
        # read_file = open("SecreteVibes.txt", mode='r', encoding='utf-8')
        # get_file = read_file.readline()
        with open("SecreteVibes.txt", "r", encoding='utf-8') as file:
            data = file.readlines()
            get_file = random.choice(data)

            print("\t\t---------------------------------------------")
            print("\t\t", get_file)
            print("\t\t---------------------------------------------")
            """ Close the file"""

    # A function that appends a file secret vibes
    @staticmethod
    def wt_vibes(self):
        # vibe_bank = open("SecreteVibes.txt", mode='a')
        # my_vibe = input(str("Please tell us your vibe: "))
        # vibe_bank.write(my_vibe)
        output = input("\t\t Hey you what is your story : -> : ")
        with open("SecreteVibes.txt", "a", encoding='utf-8') as file:
            file.write(f"\n {output}")
        print("\t\t Thanks for Sharing")
