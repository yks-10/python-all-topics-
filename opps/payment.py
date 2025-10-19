from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        pass 


class PayPalPayment(Payment):
    def make_payment(amount):
        pass 

class CryptoPayment(Payment):

    def make_payment(amount):
        pass 

def process_payment(payment_method, amount):
    payment_method.make_payment(amount)

credit = CreditCardPayment()
paypal = PayPalPayment()
crypto = CryptoPayment()

process_payment(credit, 5000)