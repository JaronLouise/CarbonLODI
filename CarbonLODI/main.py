import os
import Security

logo = '''
   ______           __                   __    ____  ____  ____
  / ____/___ ______/ /_  ____  ____     / /   / __ \/ __ \/  _/
 / /   / __ `/ ___/ __ \/ __ \/ __ \   / /   / / / / / / // /  
/ /___/ /_/ / /  / /_/ / /_/ / / / /  / /___/ /_/ / /_/ // /   
\____/\__,_/_/  /_.___/\____/_/ /_/  /_____/\____/_____/___/   

                                                               '''

main_menu = '''
                         Main Menu

                        1 - Register
                        2 - Login
                        0 - Exit
Response: '''

while True:
    os.system('cls')
    print(logo)
    choice = input(main_menu)

    os.system('cls')  # clear screen before processing user choice

    if choice == '1':
        Security.AccountManager().register()
        input("Press Enter to continue...")
    elif choice == '2':
        account_manager = Security.AccountManager()
        account_manager.load_users()
        account_manager.login()
        input("Press Enter to continue...")
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

