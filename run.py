from app import PasswordGenerator, Case

pg = PasswordGenerator()
pg.set_charset(5)

#print the password generator
print(pg.generate_password())
