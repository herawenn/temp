import os
import sys
import requests
import json
from time import sleep
from colorama import init, Fore

# Setting console dimensions
os.system("mode con cols=80 lines=25")

# Function to clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initializing color codes
init()
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
P = Fore.MAGENTA
C = Fore.CYAN
X = Fore.RESET

# Function to generate emails
def fetch_email(count):
    print(" Email Generated: "+requests.get(f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}").text)

# Function to fetch emails from inbox
def fetch_mail(email_user, email_domain):
    print(" Recent Inboxs: \n " + requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email_user}&domain={email_domain}").text)

# Function to fetch raw emails
def fetch_raw_mail(email_user, email_domain, id):
    print(" Raw Email: \n "+requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={email_user}&domain={email_domain}&id={id}").text)


# Main function
def main():
    init()
    clear_console()
    # Loop until user chooses to exit    
    while True:
        print(f"  _____               __  __      _ _ {X}")
        print(f" |_   _|__ _ __  _ __|  \/  |__ _(_) |{X}")
        print(f"   | |/ -_) '  \| '_ \ |\/| / _` | | |{X}")
        print(f"   |_|\___|_|_|_| .__/_|  |_\__,_|_|_|{X}")
        print(f"                |_|     {G}H {C}e {B}r {Y}a {P}w {R}e {G}n {X}")
        print("")
        print(f" {G}[{P}1{G}]{X} Inbox")
        print(f" {G}[{P}2{G}]{X} Raw Mail")
        print(f" {G}[{P}3{G}]{X} Generate")
        print(f" {G}[{P}4{G}]{X} Exit")

        try:
            choice = int(input(f"\n {P}//{G}: {X}"))
        except ValueError:
            print(" Please enter a valid option (1-4)")
            continue

        # Fetch emails from inbox
        if choice == 1:
            email_user = input(" Enter the username of email: ")
            email_domain = input(" Enter the domain of email: ")
            fetch_mail(email_user, email_domain)
            
        # Fetch raw emails
        elif choice == 2:
            email_user = input(" Enter the username of email: ")
            email_domain = input(" Enter the domain of email: ")
            id = int(input(" Enter the id of the inbox:"))
            fetch_raw_mail(email_user, email_domain, id)
            
        # Generate emails or fetch domain list
        elif choice == 3:
            clear_console()
            print(f"\n 1secmail.com {Y}/{X} 1secmail.org {Y}/{X} 1secmail.net \n icznn.com {Y}/{X} ezztt.com {Y}/{X} vjuum.com {Y}/{X} laafd.com {Y}/{X} txcct.com\n")                   
            count = int(input("\n Generate how many addresses: "))
            fetch_email(count)

        # Exit
        elif choice == 4:
            sys.exit(f" {Y}Exiting{X}...")
        else:
            print(" Please enter a valid option (1-4)")

# Run the main function when script is executed
if __name__ == "__main__":
    main()
