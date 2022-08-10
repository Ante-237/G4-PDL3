# A function that reads a file and returns each line of the file
def read():
    read_file = open("SecreteVibes.txt", mode='r', encoding='utf-8')
    get_file = read_file.readline()
    print("\t\t---------------------------------------------")
    print(get_file)
    print("\t\t---------------------------------------------")

# A function that appends a file
def wt_vibes():
    vibe_bank = open("SecreteVibes.txt", mode='a')
    my_vibe = input(str("Please tell us your vibe: "))
    vibe_bank.write(my_vibe)
read()
wt_vibes()
