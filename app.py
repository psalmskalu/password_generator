from random import randint


class PasswordGenerator:

    def set_charset(self, *args):
        self.charset = ''.join(str(string) for string in args)

    def generate_password(self):
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
