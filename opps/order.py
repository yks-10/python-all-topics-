from abc import ABC, abstractmethod 

class Product(ABC):
    def __init__(self, name, id):
        self.name = name 
        self.id = id 

    @abstarct_method
    def get_product(self):
        pass

class ProductMangement(Product):
    def __init__(self, name, id):
        self.name = name 
        self.id = id 



class Order:
    def __init__(self, order_id, product: Product):
        self.order_id = order_id 
        self.product = product 

    def get_order(self):
        return f"order {self.id}"

class OrderStatus:
    def __init__(self, odr: order, status):
        self.odr = odr
        self._status = status

    @property
    def status(self):
        return self.status

    @status.setter
    def set_status(self, value):
        self.status = value 

    @status.getter
    def get_status(self):
        return f"status is {self.status}"

class OrderPayment:
    def __init__(self, odr: order, payment_status):
        self.odr = odr
        self._payment_status = payment_status 

    @property
    def payment_status(self):
        return self.status

    @payment_status.setter
    def set_status(self, value):
        self._payment_status = value 

    @payment_status.getter
    def get_status(self):
        return f"status is {self.status}"

    
