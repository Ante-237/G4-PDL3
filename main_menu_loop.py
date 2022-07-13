

def top_menu_loop():
    # show menu options
    user_input = int(input("Enter the Menu options:"))
    while user_input != 4:
        if user_input == 1:
            # call main menu look funciton
            loop_main_menu()
        elif user_input == 2:
            print("TODO")
            # call functions which shows about unavailable for now
        elif user_input == 3:
            print("TODO")
            # call function which shows about
        elif user_input not in range(1, 4):
            print("TODO")
            # call function which shows option not available

        # show top menu options
        # get user input again
        user_input = int(input(" Enter menu option"))

    # function to output thanks for using app.



def loop_main_menu():
    # show menu options
    user_input = int(input("Enter the Menu option:"))
    while user_input != 5:
        # show menu options
        if user_input == 1:
            print("TODO")
            secret_room_menu()
            # call secret rooms function
        elif user_input == 2:
            print("TODO")
            positive_vibes_menu()
            # call positive vibes room function
        elif user_input == 3:
            print("TODO")
            # call gallery not available show function
            # draw the entire same screen again
        elif user_input == 4:
            print("TODO")
            # call lgame room not available function
            # draw the entire same screen again
        elif user_input not in range(1, 6):
            print("TODO")

            # call function for invalid options
            # draw the entire same screen again
        # show menu options
        # get user input again
    user_input = int(input("Enter the Menu option:"))

    # go to TOP MENU IS exit is entered


def secret_room_menu():
    # show menu options
    user_input = int(input("Enter the Menu options: "))
    while user_input != 3:
        print("TODO")
        if user_input == 1:
            print("TODO")
            # call function to get a random word from the read list and output to the screen
        if user_input == 2:
            print("TODO")
            # call function that ask user to add their story and adds it to the list
        elif user_input not in range(1, 4):
            print("TODO")
            # call function to show invalid input by user

        # show options for secret room
        user_input = int(input("Enter the Menu options: "))

    # go to MAIN MENU if exit value is entered


def positive_vibes_menu():
    # show menu options
    user_input = int(input("Enter the Menu options: "))
    while user_input != 2:
        print("TODO")
        if user_input == 1:
            print("TODO")
            # call function get and return a random word of encouragement
        elif user_input not in range(1, 3):
            print("TODO")
            # call function to show invalid input by user

        # show menu options for positive vibes
        user_input = int(input("Enter the Menu options"))

    # go to MAIN MENU if exit value is entered












