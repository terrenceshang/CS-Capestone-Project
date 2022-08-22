class Admin(Person):
    def __init__(self, access): #Constructor of the Admin class
        super().__init__(self, username, name, surname, email, password)
        self.access = access

    def getAccess(self): #return Access
        return self.access
    def setAccess(self): #set Access
        access = self
