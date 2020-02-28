from app import PasswordGenerator, Case

pg = PasswordGenerator()
pg.set_charset(Case.LOWERS_NUMBERS)

#print the password generator
print(pg.generate_password())
