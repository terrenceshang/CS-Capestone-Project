from xml.dom.expatbuilder import InternalSubsetExtractor


class Person:
    isUser = True

    def __init__(self, username, name, surname, email, password): #Constructor for Person
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def getName(self): #get Name
        return self.name
    def setName (line): #set Name
        name = line

    def getUsername(self): #get Username
        return self.username
    def setUsername(line): #set Username
        username = line

    def getSurname(self): #get Surname
        return self.surname
    def setSurname(line): #set Surname
        surname = line

    def getEmail(self): #get Email
        return self.email
    def setEmail(line): #set Email
        email = line

    def getPassword(self): #get Password
        return self.password
    def setPassword(line): #set Password
        password = line

    def getIsUser(self): #get isUser
        return self.isUser
    def setIsUser (line): #set isUser
        isUser = line
    