# A function that reads a file and returns each line of the file
def read():
    read_file = open("SecreteVibes.txt", mode='r', encoding='utf-8')
    for i in read_file:
        print(read_file, end="")