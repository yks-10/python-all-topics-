from abc import ABC, abstractmethod
class User:
    def __init__(self, name, id, salary):
        self.name = name 
        self.id = id 
        self.salary = salary 
    @abstractmethod
    def action(self):

class Doctor(User):
    def __init__(self, name, id, salary, specilist):
        super().__init__(name, id, salary)
        self.specilist = specilist
    
    def action(self):
        pass

class Nurse(User):
    def __init__(self, name, id, salary, assist_doctor_id):
        super().__init__(name, id, salary)
        self.assist_doctor_id = assist_doctor_id
    
    def action(self):
        pass

class Admin(User):
    def __init__(self, name, id, salary, appoinment):
        super().__init__(name, id, salary)
        self.appoinment = appoinment
    
    def action(self):
        pass

