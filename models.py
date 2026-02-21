#!/usr/bin/env python3
import random
import json 
import time 
from datetime import datetime, timedelta

class Account:
    def __init__(self, name, surname, fin, pin, card_number=None, balance=0, expiry=None):
        self.name = name
        self.surname = surname
        self.fin = fin
        self.pin = pin 
        self.balance = balance 
        self.card_number = card_number if card_number else self.generate_card()
        self.expiry = expiry if expiry else self.generate_expiry()


    def generate_card(self):
        card_no = ""
        for _ in range(16):
            card_no += str(random.randint(0, 9))
        return card_no

    def generate_expiry(self):
        return (datetime.now() + timedelta(days=730)).strftime("%m/%y")

    def to_dict(self):
        # This method returns all class objects as a dictionary
        return {
            "name": self.name,
            "surname": self.surname,
            "fin": self.fin,
            "pin": self.pin,
            "balance": self.balance,
            "card_number": self.card_number,
            "expiry": self.expiry
        }
    def get_azn_to_usd_balance(self):
        return self.balance / 1.70

    def get_usd_to_azn_balance(self):
        return self.balance * 1.70

    def get_azn_to_euro_balance(self):
        return self.balance / 2

    def get_euro_to_azn_balance(self):
        return self.balance * 2

