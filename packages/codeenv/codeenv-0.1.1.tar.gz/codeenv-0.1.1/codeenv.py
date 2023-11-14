import os
import time
import threading
from git import Repo


def print_loading_bar():
    while cloning:
        for i in range(21):
            s = '[' + '#' * i + ' ' * (20 - i) + ']'
            print('\r' + s, end='')
            time.sleep(0.1)


def clone_gist():
    # Read the folder name from standard input
    folder = input("Coding environment name: ")

    # Construct the git clone command
    command = "https://gist.github.com/bac0ea59fa9c5f55e75a9d1a18b82ab8.git"

    # Start the loading bar
    global cloning
    cloning = True
    t = threading.Thread(target=print_loading_bar)
    t.start()

    # Run the git clone command
    Repo.clone_from(command, folder)

    # Stop the loading bar
    cloning = False
    t.join()  # Wait for the loading bar to finish

    # Clear the terminal again
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Successfully cloned the std:Makefile into the folder", folder)

    # Change directory
    os.chdir(folder)
    print("Environment ready! You can start coding by changing the direcory ( cd", folder, ")")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Automatic coding environment generator for basic development")
    print("\033[32mAuthor: //ap0// https://github.com/rares9301\033[0m")  # Green text
    print("Choose a coding language.")
    print("------------------------------------------------------------------------")
    print("\033[34m1. C/C++\033[0m")  # Blue text
    print("2. (not implemented)")
    print("3. (not implemented)")
    print("------------------------------------------------------------------------")

    option = input("Enter your choice: ")
    if option == '1':
        clone_gist()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
