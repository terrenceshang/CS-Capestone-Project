class Person:
    def __init__(self, username, name, surname, email, password):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def getName(self):
        return self.name
    def getUsername(self):
        return self.username
    def getSurname(self):
        return self.surname
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password
