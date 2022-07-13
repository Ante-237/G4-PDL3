

def loop_main_menu():
#   show menu options
    user_input = int(input("Enter the Menu option:"))
    while user_input != 5:
#   show menu options
        if user_input == 1:
#   call secret rooms function
        elif user_input == 2:
# call positive vibes room function
        elif user_input == 3:
# call gallery not available show function
# draw the entire same screen again
        elif user_input == 4:

# call lgame room not avaible function
# draw the entire same screen again
        elif user_input not in range(0, 6):

# call function for invalid options
# draw the entire same screen again

        # get user input again
    user_input = int(input("Enter the Menu option:"))

    #go to TOP MENU IS exit is entered



