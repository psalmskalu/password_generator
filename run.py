from app import PasswordGenerator

pg = PasswordGenerator()

pg.set_charset_length(length = 5)
pg.set_charset_types(type= ['numbers', 'specials'])

#print the password generator
print(pg.generate_password())
