from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, customer_id, balance, account_type):
        self.account_number = account_number
        self.customer_id = customer_id 
        self.__balance = balance 
        self.account_type = account_type

class AccountManagment:
    def __init__(self, account):
        self.account = account


    @abstractmethod
    def get_balance(self):
        return self.account.__balance 

    @property
    def balance(self):
        return self.account.__balance 

    @balance.setter
    def add_balance(self, amount):
        try:
            if amount < 0:
                raise ValueError("Value needs to be greater than zero")
            self.account.__balance += amount 
        except Exception as e:
            return str(e)

    def withdraw_amount(self, amount):
        try:
            if amount > self.account.__balance:
                raise "Insufficent Balance"
            return amount 
        except Exception as e:
            return str(e)
    

class AccountStatus:
    def __init__(self, account, status):
        self.account = account 
        self.__status = sattus

    @property
    def status(self):
        return self.__status 

    @status.setter
    def set_status(self, new_status):
        self.__status = new_status
        return "Status Updated"

class Card:
    def __init__(self, card_number, cvv, exp_date, pin, account):
        self.card_number = card_number
        self.cvv = cvv
        self.exp_date = exp_date
        self.__pin = pin
        self.account = account 


    @property 
    def pin(self):
        return self.__pin

    @pin.setter
    def set_pin(self, pin):
        if len(pin) < 4 or str(pin) is str(pin).is_alpha():
            return "Invalid PIN"
        self.__pin = pin 
        return "Pin setted succesfully Successfully "

