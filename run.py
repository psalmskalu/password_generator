from app import PasswordGenerator

# string of upper characters
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# string of lower characters
lowercase = 'abcdefghijklmnopqrstuvwxyz'

# string of numbers
digits = '0123456789'

# string of special characters
specials = " !|\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

pg = PasswordGenerator()
pg.set_charset(specials, digits, lowercase, uppercase)
print(pg.generate_password())
