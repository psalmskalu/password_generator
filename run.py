from app import PasswordGenerator

pg = PasswordGenerator()
pg.set_charset(7)
print(pg.generate_password())


