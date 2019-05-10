class Account(object):

    def __init__(self,total):
        self.total = total

    def withdraw(self,value):
        if value > self.total:
            raise Exception("not enough money")
        
        else:
            return "operation completed"
    
    def deposit(self,value):
        self.total = self.total + value
        return self.total