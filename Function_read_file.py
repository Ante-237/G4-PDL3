# Function to read and respond visually

file = open('PositiveVibes.txt', 'r', encoding='utf-8')
p = ["Wrold is luck to have you\n", "You got this:)", "Lovely you are"]
file.write("Hey\n")
file.writelines(p)
file.close()