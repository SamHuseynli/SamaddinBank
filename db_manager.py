#!/usr/bin/env python3
from models import Account
import json
import time 
from datetime import datetime 

def load_data():
    try: 
        with open('database.json', 'r') as file:
            data = json.load(file)
            return [Account(**user) for user in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

all_accounts = load_data()


def save_data(all_accounts):
    ready_to_save = [] 
    for acc in all_accounts:
        ready_to_save.append(acc.to_dict())

    with open('database.json', 'w') as file:
        json.dump(ready_to_save, file, indent=4)

def log_operation(card_number, operation_type):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] Card: {card_number} | Operation: {operation_type}\n"

    with open("ophist.log", "a") as log_file:
        log_file.write(log_entry)


