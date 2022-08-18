class Admin(Person):
    def __init__(self, access):
        super().__init__(self, username, name, surname, email, password)
        self.access = access

    def getAccess(self):
        return self.access
