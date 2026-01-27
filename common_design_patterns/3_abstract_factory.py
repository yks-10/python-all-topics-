from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod 
    def pay(self, amount: float) -> str:
        pass 

class Receipt(ABC):
    @abstractmethod
    def generate(self, amount:float) -> str:
        pass


class UPIPayment(Payment):
    def pay(self, amount:float) -> str:
        return f"UPI payment of {amount} successful"

class UPIReceipt(Receipt):
    def generate(self, amount:float) -> str:
        return f"UPI receipt generated for {amount}"


class CardPayment(Payment):
    def pay(self, amount:float) -> str:
        return f"Card Payment of {amount} successfull"

class CardRecipt(Receipt):
    def generate(self, amount:float) -> str:
        return f"UPI receipt generated {amount}"



class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass

    @abstractmethod
    def create_receipt(self) -> Receipt:
        pass

#conceret factories 
class UPIFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return UPIPayment 

    def create_receipt(self) -> Receipt:
        return UPIReceipt 

class CardFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return CardPayment

    def create_receipt(self) -> Receipt:
        return CardReceipt


def process_payment(factory: PaymentFactory, amount: float) -> None:
    payment = factory.create_payment()
    receipt = factory.create_receipt()

    payment.pay(amount)
    receipt.generate(amount)


if __name__ == '__main__':
    choice = input("")
    amount = int(input())

    if choice == "UPI":
        factory = UPIFactory()
    elif choice == "CARD":
        factory = CardFactory()
    else:
        raise ValueError("unknown payment method")

    process_payment(factory, amount)