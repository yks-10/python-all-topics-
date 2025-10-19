from abc import ABC, abstractmethod
class User:
    def __init__(self, name, phone_number, user_id, user_type):
        self.name = name 
        self.phone_number = phone_number 
        self.user_id = user_id
        self.user_type = user_type

class Restaurant:
    def __init__(self, name, menu_item):
        self.name = name 
        self.menu_item = menu_item


class Order(ABC):
    def __init__(self, items, order_id, status, consumer):
        self.items = items
        self.order_id = order_id
        self.status = status 
        self.consumer = consumer
    
    @abstractmethod
    def get_status(self, order_id):
        pass

    def set_status(self, new_status):
        self.__status = new_status

class Delivery(Order):
    def __init__(self, order, delivery_agent):
        super().__init__(order.items, order.order_id, order._Order__status, order.consumer)
        self.delivery_agent = delivery_agent

    def get_status(self, order_id):
        pass

