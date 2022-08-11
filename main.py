# MAIN APP COMBINE FILE
# ALL CODES WILL BE MERGES HERE
import main_menu_loop as menu_need
import nameofapp_function as appname
import user_interface_designs as ui_design


def run_app():
    # call function to display name of app
    appname.display_name_of_app()

    # call function to display ui  design of app
    ui_design.my_function()

    # call the top menu function
    menu_need.top_menu_loop()


if __name__ == "__main__":
    run_app()