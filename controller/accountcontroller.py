from model.user import User


class AccountController:
    AllAccounts = []
    logged_in_user = []

    def initial_admin(self):
        """
        creates the admin object with its special role and appends it to the AllAccounts list
        """
        admin = User(1, "Max", "Pfister", "25.09.2001", "mapfi", "Hallowelt123", "Admin")
        self.AllAccounts.append(admin)

    def firstname_validation(self, firstname):
        """
        validates a first name from an input
        :param firstname: the first name to be validated
        :return: True if the validation was successful, false if it was not
        """
        if firstname[0].isupper():
            return True

    def lastname_validation(self, lastname):
        """
        validates a last name from an input
        :param lastname: the last name to be validated
        :return: True if the validation was successful, false if it was not
        """
        if lastname[0].isupper():
            return True

    def password_validation(self, password):
        """
        validates a password from an input
        :param password: the password to be validated
        :return: True if the validation was successful, false if it was not
        """
        numberValidation = False
        upperCaseCheck = False
        lowerCaseCheck = False

        for i in range(0, len(password)):
            if password[i].isnumeric():
                numberValidation = True
            if password[i].isupper():
                upperCaseCheck = True
            if password[i].islower():
                lowerCaseCheck = True

        if numberValidation and upperCaseCheck and lowerCaseCheck:
            return True
        else:
            return False

    def create_user(self, firstname, lastname, birthday, username, password):
        """
        creates a user object and appends it to the list AllAccounts
        :param firstname: a valid first name for the user
        :param lastname: a valid last name for the user
        :param birthday: birthday of the user
        :param username: a username for the user
        :param password: a valid password for the user
        """
        user_id = len(self.AllAccounts) + 1
        new_user = User(ID=user_id, firstname=firstname, lastname=lastname, birthday=birthday, username=username,
                        password=password, role="User")
        self.AllAccounts.append(new_user)

    def login(self, username, password):
        """
        compares whether the user exists; if True then he is append to the list logged_in_user
        :param username: input for a possible username
        :param password: input for a possible password
        :return: the user object with which the username and password match
        """
        for user in self.AllAccounts:
            if user.username == username and user.password == password:
                self.logged_in_user.append(user)
                return user

    def change_user(self, change_attribute, new_value):
        """
        sends the data of the logged in user to the model user to change it
        :param change_attribute: the name of the attribute which should be changed
        :param new_value: new value of the attribute
        """
        self.logged_in_user[0].change_data(change_attribute, new_value)
