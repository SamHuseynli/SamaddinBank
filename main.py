#!/usr/bin/env python3
from models import Account
from db_manager import load_data, save_data, log_operation
import time

all_accounts = load_data()

def sign_up():
    name = input("Enter Your Name: ")
    surname = input("Enter Your Surname: ")
    fin = input("Enter Your FIN code: ")
    pin = input("Enter the PIN that consists 4 digit number for accessing to your card")
    is_exist = False

    for acc in all_accounts:
        if acc.fin == fin:
            is_exist = True
            break 
    if is_exist:
        print(f"Error: There is already account exists that belongs to {fin}")
    else:
        new_user = Account(name, surname, fin, pin)
        all_accounts.append(new_user)
        save_data(all_accounts)
        log_operation(new_user.card_number, "SIGN UP SUCCESFUL")
        print(f"Congratulation {name}! Your new card: {new_user.card_number}")
    return new_user

def log_in():
    card_number = input("Enter 16 digit card number: ")

    current_user = None
    for acc in all_accounts:
        if acc.card_number == card_number:
            current_user = acc
            break
    if current_user is None:
        print("Eroor: Card number not found!")
        return

    attempts = 0
    while attempts < 3:
        pin = input("Enter 4 digit pin code: ")

        if current_user.pin == pin:
            log_operation(current_user.card_number, "LOGIN_SUCCESFULL")
            print(f"Congratulations, {current_user.name}! Successful login.")
            return current_user
        else:
            attempts += 1
            log_operation(current_user.card_numbmer, "UNSUCCESFULL PIN ENTRY")
            print(f"Wrong PIN! Reamaining attempts: {3 - attempts}")

    print("You've been blocked for 1 minute.")
    time.sleep(60)


while True: 
    u_choise = input("Welcome to SamaddinBank,\n1) Log In\n2) Sign Up\nChoose the appropriate option to you: ")
    try: 
        if u_choise == "1":
            user = log_in()
            if user:
                while True: 
                    print(f"Welcome {user.name}!")
                    op_choise = input("1. Show Balance\n2. Cash Out\n3. Enter cash to balance\n4. Exit\n Choose the appropriate option to you: ")

                    try:
                        if op_choise == "1":
                            currency = input("1. AZN\n2. USD\n3. EURO\nIn which currency do you want to view your balance: ")
                            if currency == "1":
                                log_operation(user.card_number, "VIEWED BALANCE IN AZN")
                                print(user.balance, "AZN")
                            elif currency == "2":
                                log_operation(user.card_number, "VIEWED BALANCE IN USD")
                                print(f"{user.get_azn_to_usd_balance():.2f}", "USD")
                            elif currency == "3":
                                log_operation(user.card_number, "VIEWED BALANCE IN EURO")
                                print(f"{user.get_azn_to_euro_balance():.2f}", "EURO")
                            else:
                                print("Invalid Input")
                                continue 
                        elif op_choise == "2":
                            amount = int(input("Amount: "))
                            if user.balance >= amount:
                                user.balance -= amount
                                time.sleep(5)
                                save_data(all_accounts)
                                log_operation(user.card_number, f"WITHDRAWAL: {amount} AZN")
                                print(f"Dear {user.name}, your reamining balance: {user.balance}")
                            else:
                                print("Enter valid amount to cash out!")
                                continue
                        elif op_choise == "3":
                            amount = int(input("Amount: "))
                            user.balance += amount
                            time.sleep(5)
                            save_data(all_accounts)
                            log_operation(user.card_number, f"DEPOSIT: {amount} AZN")
                            print(f"Dear {user.name}, your reamining balance: {user.balance}")
                        elif op_choise == "4":
                            break
                    except (TypeError, ValueError):
                        print("Invalid Input!")
        elif u_choise == "2":
            user = sign_up()
            print(f"Welcome to our bank {user.name}")
            print("For the verification, log in to your account, then enjoy from our system")
            save_data(all_accounts)
        elif u_choise == "3":
            break
    except (TypeError, ValueError):
        print("Invalid Input")

