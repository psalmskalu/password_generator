from app import PasswordGenerator

pg = PasswordGenerator()
pg.set_charset(6)
print(pg.generate_password())


