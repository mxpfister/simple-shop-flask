class User:
    ID = None
    role = None
    firstname = None
    lastname = None
    birthday = None
    username = None
    password = None

    def __init__(self, ID, firstname, lastname, birthday, username, password, role):
        """
        Constructor
        :param ID: ID of the user
        :param firstname: firstname of the user
        :param lastname: lastname of the user
        :param birthday: birthday of the user
        :param username: username of the user
        :param password: password of the user
        :param role: role of the user
        """
        self.ID = ID
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.username = username
        self.password = password

    def change_data(self, attribute, new_value):
        """
        changes the values of a user attribute
        :param attribute: the entered attribute of an user
        :param new_value: the new value that the entered attribute should have
        """
        if attribute == "first name":
            self.firstname = new_value
        elif attribute == "last name":
            self.lastname = new_value
        elif attribute == "birthday":
            self.birthday = new_value
        elif attribute == "username":
            self.username = new_value
        elif attribute == "password":
            self.password = new_value
