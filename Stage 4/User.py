class User(Person):
    def __innit__(self, history):
        super.__innit__(username, name, surname, email, password)
        self.history = history

    def getHistory():
        return self.history
