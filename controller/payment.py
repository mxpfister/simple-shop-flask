class PaymentController:

    def street_validation(self, street):
        """
        validates the street from an input
        :param street: the given input for the street
        :return: True if the validation was successful, false if it was not
        """
        sizeValidation = len(street) >= 3
        first_uppercase = False

        if street[0].isupper():
            first_uppercase = True

        if sizeValidation and first_uppercase:
            return True
        else:
            return False
