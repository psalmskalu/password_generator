from app import PasswordGenerator, Case

pg = PasswordGenerator()
pg.set_charset_length(55)
pg.set_charset(Case.UPPERS_LOWERS_NUMBERS)

#print the password generator
print(pg.generate_password())
