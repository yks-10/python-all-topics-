class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number 
        self.__balance = balance 

    def deposit(self, amount):
        try:
            if amount<0:
                raise ValueError("Amount should be Greater than 0")
            super.__balance += amount
        except Exception as e:
            return e 
    def withdraw(self, amount):
        try:
            if amount <1:
                raise ValueError("Amount needs be greater than zero")
            if amount > super.__balance:
                raise valueError("Amount is gretaer than balance")
            super.__balance -= amount
        except Exception as e:
            return e 

    def get_balance(self):
        return super().__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def deposite(self, amount):
        try:
            if amount < 0:
                raise valueError(" value needs be grater than zero")
            self.__balance += amount 
        except Exception as e:
            return str(e)
