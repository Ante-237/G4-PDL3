# A function that displays the SecretVibes title

import random


def read_title():
    print(" This is the Secrete Vibes Room ")

# A function that reads a file and returns each line of the file
#


def read():
    # read_file = open("SecreteVibes.txt", mode='r', encoding='utf-8')
    # get_file = read_file.readline()
    with open("SecreteVibes.txt", "r", encoding='utf-8') as file:
        data = file.readline()
        get_file = random.choice(data)

    print("\t\t---------------------------------------------")
    print(get_file)
    print("\t\t---------------------------------------------")
    """ Close the file"""


# A function that appends a file secret vibes
def wt_vibes(entry):
    # vibe_bank = open("SecreteVibes.txt", mode='a')
    # my_vibe = input(str("Please tell us your vibe: "))
    # vibe_bank.write(my_vibe)
    with open("SecreteVibes.txt", "a", encoding='utf-8') as file:
        file.write("\n"+entry)

