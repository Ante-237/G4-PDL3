from stephen_function import *
from isaac_functions import *
from Sugira_functions import *
from Gatwaza_readfile import *
from Princess_Functions import *


class MainMenu:

    def __init__(self):
        self.step_class = Messages()  # stephen class
        self.isaac_class = Display()
        self.sugira_class = ReadAll()
        self.gatwaza_class = PositiveMessage()
        self.princess_class = HeadingPart()

    def top_menu_loop(self):
        # create classes
        self.princess_class.display_name_of_app()
        # show top menu  options
        self.isaac_class.top_menu_options()
        # get user input
        user_input = int(input("Enter the Menu options:"))
        while user_input != 4:
            if user_input == 1:
                # call main menu look function
                self.loop_main_menu()
            elif user_input == 2:
                self.step_class.unavailable()
                # call functions which shows about unavailable for now
            elif user_input == 3:
                print("\t\t **------   YOUR DATA IS SAFE   -----**")

                # call function which shows about
            elif user_input not in range(1, 4):
                self.step_class.wrong_input()
                # call function which shows option not available

            # show top menu options
            self.isaac_class.top_menu_options()
            # get user input again
            user_input = int(input(" Enter menu option"))
        # exit while showing message for exit
        self.step_class.exit_function()

        # function to output thanks for using app.
    def loop_main_menu(self):
        # show menu options
        self.princess_class.main_menu_title()  # display heading for main menu
        user_input = int(input("Enter the Menu option:"))
        while user_input != 5:
            # show menu options
            if user_input == 1:
                print("TODO")
                self.secret_room_menu()
                # call secret rooms function
            elif user_input == 2:
                print("TODO")
                self.positive_vibes_menu()
                # call positive vibes room function
            elif user_input == 3:
                print("TODO")
                self.step_class.unavailable()
                # call gallery not available show function
                # draw the entire same screen again
            elif user_input == 4:
                print("TODO")
                self.step_class.unavailable()
                # call lgame room not available function
                # draw the entire same screen again
            elif user_input not in range(1, 6):
                print("TODO")
                self.step_class.wrong_input()
                # call function for invalid options
                # draw the entire same screen again

            # show menu options
            self.isaac_class.main_menu_options()
            # get user input again
            user_input = int(input("Enter the Menu option:"))

        # go to TOP MENU IS exit is entered
        self.step_class.not_available()

    def secret_room_menu(self):
        # show menu options
        self.isaac_class.secret_room_options()
        user_input = int(input("Enter the Menu options: "))
        while user_input != 3:
            if user_input == 1:
                self.sugira_class.read_choice()
                # call function to get a random word from the read list and output to the screen
            if user_input == 2:
                self.sugira_class.wt_vibes()
                # call function that ask user to add their story and adds it to the list
            elif user_input not in range(1, 4):
                self.step_class.wrong_input()
                # call function to show invalid input by user

            # show options for secret room
            user_input = int(input("Enter the Menu options: "))
        # go to MAIN MENU if exit value is entered
        self.step_class.not_available("Here")

    def positive_vibes_menu(self):
        self.princess_class.function_for_pv_title()
        # show menu options
        self.isaac_class.positive_vibes_options()
        user_input = int(input("Enter the Menu options: "))
        while user_input != 2:
            if user_input == 1:
                self.gatwaza_class.read_positive_vibes()
                # call function get and return a random word of encouragement
            elif user_input not in range(1, 3):
                self.step_class.wrong_input()
                # call function to show invalid input by user

            # show menu options for positive vibes
            self.isaac_class.positive_vibes_options()
            user_input = int(input("Enter the Menu options"))

        # go to MAIN MENU if exit value is entered
        self.step_class.not_available("Here")












