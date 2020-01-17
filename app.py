from random import randint


class PasswordGenerator:

    # string of upper characters
    upper_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # string of lower characters
    lower_characters = 'abcdefghijklmnopqrstuvwxyz'

    # string of numbers
    numbers = '0123456789'

    # charset
    charset = None

    charset_constants = {
        'UPPERS_ONLY': 1,
        'LOWERS_ONLY': 2,
        'LOWERS_UPPERS': 3,
        'NUMBERS_ONLY': 4,
        'UPPERS_NUMBERS': 5,
        'LOWERS_NUMBERS': 6,
        'UPPERS_LOWERS_NUMBERS': 7
    }

    def set_charset(self, charset):
        """
          Sets the type of character set to be
          used by password geenrator

          Parameters:
          ---------------------
          charset (string) - the charset supplied as an instance of Case
          
        """
        if charset == 1:
            self.charset = self.upper_characters
        elif charset == 2:
            self.charset = self.lower_characters
        elif charset == 3:
            self.charset = self.upper_characters + self.lower_characters
        elif charset == 4:
            self.charset = self.numbers
        elif charset == 5:
            self.charset = self.upper_characters + self.numbers
        elif charset == 6:
            self.charset = self.lower_characters + self.numbers
        elif charset == 7:
            self.charset = self.lower_characters + self.upper_characters + self.numbers
        else:
            self.charset is None
            print('Invalid charset selected')

    def generate_password(self):

        """
        Performs the computation that genarates a
        password

        """

        password = ""
        while True:
            try:
                length = int((input("Enter password length: ")))
                for x in range(length):
                    x = randint(0, (self.charset.__len__() - 1))
                    password += self.charset[x]
                return password
            except ValueError:
                print("Enter whole number")
