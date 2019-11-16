from app import PasswordGenerator, Case

pg = PasswordGenerator()
pg.set_charset(Case.UPPERS_LOWERS_NUMBERS)
print(pg.generate_password())


