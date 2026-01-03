from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod 
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount) -> str:
        return f"UPIPaymnet amount paid {amount}" 

class CardPayment(Payment):
    def pay(self, amount) -> str:
        return f"CardPayment amount paid {amount}"


class PaymentFactory(ABC):
    def create_payment(self):
        raise NotImplementedError

class UPIFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return UPIPayment()

class CardFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return CardPayment()


def process_payment(factory: PaymentFactory, amount: float) -> str:
    payment = factory.create_payment()
    return payment.pay(amount)

if __name__ == "__main__":
    choice = input()
    amount = int(input())

    if choice == "UPI":
        factory = UPIFactory()
    elif choice == "CARD":
        factory = CardFactory()
    else:
        raise ValueError("Unknown paymnet")
    result = process_payment(factory, amount)
    print(result)