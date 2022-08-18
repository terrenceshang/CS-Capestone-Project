class Admin(Person):
    def __init__(self, access):
        super().__init__(username, name, surname, email, password)
        self.access = access

    def getAccess():
        return self.access
