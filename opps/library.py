class Item:
    def __init__(self, name, author, item_id):
        self.name = name 
        self.author = author
        self.item_id = item_id

class Books(Item):
    def __init__(self, name, author,item_id, pages):
        super().__init__(name, author, item_id)
        self.pages = pages
    def display(self):
        pass
    
class Magazines(Item):
    def __init__(self, name, author, item_id, category):
        super().__init__(name, author, item_id)
        self.category = category

    def display(self):
        pass

    
class DVD(Item):
    def __init__(self, name,  item_id, duration):
        super().__init__(name, author, item_id)
        self.duration = duration

    def display(self):
        pass