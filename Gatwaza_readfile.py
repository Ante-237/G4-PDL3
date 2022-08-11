# import required module
import random

# take two values from user
name = input("Enter your Name: ")
Positive_room = input("Enter any positive word: ")

# Display all values on screen
print("\n")
print("Printing Individual Details")
print("Name", "Positive_room")
print(name, Positive_room)

# print random word
print(random.choice(open("PositiveVibes.txt", "r").readline().split()))
